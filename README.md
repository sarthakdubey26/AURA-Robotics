<div align="center">

# AURA

### Adaptive Uncertainty-Aware Robotic Autonomy

**A ROS 2 research framework for autonomous robots that detect degraded sensing and localization and adapt their behavior before uncertainty becomes failure.**

![ROS2](https://img.shields.io/badge/ROS%202-Jazzy-22314E)
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-E95420)
![Gazebo](https://img.shields.io/badge/Gazebo-Harmonic-F58113)
![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

</div>

---

## Overview

Autonomous robots often assume that their sensors, perception models and localization systems remain reliable.

AURA explores a different idea:

> The robot should continuously estimate how much it can trust its own autonomy stack.

AURA monitors LiDAR, odometry, IMU, localization and state-estimation quality, then uses that information to adapt navigation and control behavior.

---

## System Architecture

```text
LiDAR ────────────────┐
                      │
Odometry ──┐          │
           ├── EKF ───┤
IMU ───────┘          │
                      ▼
                AURA Monitor
                      │
                Health State
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
 Rule-Based Policy             PPO Policy
         │                         │
         └────────────┬────────────┘
                      ▼
                     Nav2
                      │
                      ▼
                 TurtleBot3
