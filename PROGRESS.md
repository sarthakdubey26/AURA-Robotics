# AURA Development Log

## Current Progress

### ✅ Completed

- Ubuntu 24.04 ARM64 setup
- ROS 2 Jazzy installation
- Gazebo Harmonic
- TurtleBot3 simulation
- Nav2 navigation
- LiDAR integration
- Odometry integration
- IMU integration
- AURA ROS 2 workspace
- AURA package architecture
- Health Monitor V1
- Health Monitor V2
- Initial EKF sensor fusion integration

---

## 🔧 Currently Working On

### EKF State Estimation

Current goal:

- stabilize `/odometry/filtered`
- verify wheel odometry + IMU fusion
- remove physically impossible estimates
- compare raw odometry with fused odometry

An early EKF configuration produced an unrealistic state disagreement:

```text
OdomDiff ≈ 7.1e15 m
