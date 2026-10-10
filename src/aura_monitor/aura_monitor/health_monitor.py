import time
import math

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_msgs.msg import Float32


class HealthMonitor(Node):

    def __init__(self):
        super().__init__('aura_health_monitor')

        self.last_scan_time = None
        self.last_odom_time = None
        self.last_filtered_time = None
        self.last_amcl_time = None

        self.raw_x = None
        self.raw_y = None

        self.filtered_x = None
        self.filtered_y = None

        self.scan_valid_ratio = 0.0
        self.min_obstacle_distance = math.inf
        self.localization_covariance = math.inf

        self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.create_subscription(
            Odometry,
            '/odometry/filtered',
            self.filtered_callback,
            10
        )

        self.create_subscription(
            PoseWithCovarianceStamped,
            '/amcl_pose',
            self.amcl_callback,
            10
        )

        self.health_pub = self.create_publisher(
            Float32,
            '/aura/health_score',
            10
        )

        self.create_timer(1.0, self.evaluate_health)

        self.get_logger().info(
            'AURA Health Monitor V2 started'
        )

    def scan_callback(self, msg):

        self.last_scan_time = time.time()

        valid_ranges = [
            r for r in msg.ranges
            if math.isfinite(r)
            and msg.range_min <= r <= msg.range_max
        ]

        if len(msg.ranges) > 0:
            self.scan_valid_ratio = (
                len(valid_ranges) / len(msg.ranges)
            )

        if valid_ranges:
            self.min_obstacle_distance = min(valid_ranges)

    def odom_callback(self, msg):

        self.last_odom_time = time.time()

        self.raw_x = msg.pose.pose.position.x
        self.raw_y = msg.pose.pose.position.y

    def filtered_callback(self, msg):

        self.last_filtered_time = time.time()

        self.filtered_x = msg.pose.pose.position.x
        self.filtered_y = msg.pose.pose.position.y

    def amcl_callback(self, msg):

        self.last_amcl_time = time.time()

        covariance = msg.pose.covariance

        x_var = covariance[0]
        y_var = covariance[7]
        yaw_var = covariance[35]

        self.localization_covariance = (
            x_var + y_var + yaw_var
        )

    def age(self, timestamp):

        if timestamp is None:
            return math.inf

        return time.time() - timestamp

    def evaluate_health(self):

        scan_age = self.age(self.last_scan_time)
        odom_age = self.age(self.last_odom_time)
        filtered_age = self.age(self.last_filtered_time)
        amcl_age = self.age(self.last_amcl_time)

        odom_disagreement = math.inf

        if (
            self.raw_x is not None
            and self.filtered_x is not None
        ):
            dx = self.raw_x - self.filtered_x
            dy = self.raw_y - self.filtered_y

            odom_disagreement = math.sqrt(
                dx * dx + dy * dy
            )

        lidar_health = 1.0

        if scan_age > 1.0:
            lidar_health -= 0.6

        if self.scan_valid_ratio < 0.7:
            lidar_health -= 0.4

        lidar_health = max(0.0, lidar_health)

        state_health = 1.0

        if odom_age > 1.0:
            state_health -= 0.3

        if filtered_age > 1.0:
            state_health -= 0.4

        if (
            math.isfinite(odom_disagreement)
            and odom_disagreement > 0.5
        ):
            state_health -= 0.3

        state_health = max(0.0, state_health)

        localization_health = 1.0

        if amcl_age > 1.0:
            localization_health -= 0.5

        if (
            math.isfinite(self.localization_covariance)
            and self.localization_covariance > 1.0
        ):
            localization_health -= 0.5

        localization_health = max(
            0.0,
            localization_health
        )

        overall_health = (
            0.35 * lidar_health
            + 0.35 * state_health
            + 0.30 * localization_health
        )

        health_msg = Float32()
        health_msg.data = float(overall_health)

        self.health_pub.publish(health_msg)

        self.get_logger().info(
            f'AURA={overall_health:.2f} | '
            f'LiDAR={lidar_health:.2f} | '
            f'State={state_health:.2f} | '
            f'Localization={localization_health:.2f} | '
            f'ValidScan={self.scan_valid_ratio:.2f} | '
            f'MinObs={self.min_obstacle_distance:.2f}m | '
            f'OdomDiff={odom_disagreement:.3f}m | '
            f'LocCov={self.localization_covariance:.3f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = HealthMonitor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
