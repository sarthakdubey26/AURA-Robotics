<div align="center">

# AURA

### Adaptive Uncertainty-Aware Robotic Autonomy

**A research-oriented ROS 2 framework for robots that adapt their perception, navigation, and control behavior when sensors become unreliable, delayed, or uncertain.**

![ROS2](https://img.shields.io/badge/ROS%202-Jazzy-22314E)
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-E95420)
![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![Gazebo](https://img.shields.io/badge/Gazebo-Harmonic-F58113)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

</div>

---

## Overview

Modern autonomous robots usually assume that perception and localization remain reliable.

Real robots do not have that luxury.

Cameras experience latency. LiDAR measurements degrade. Odometry drifts. Localization becomes uncertain. A highly accurate perception model may even become dangerous when its output arrives too late.

**AURA studies how a robot can detect these conditions and adapt its operating strategy online.**

The final system compares:

**Standard Nav2 → Rule-Based Adaptation → PPO-Based Adaptive Autonomy**

under identical sensor faults and compound degradation scenarios.

---

## Core Idea

```text
Sensors
   ↓
Health & Uncertainty Monitoring
   ↓
AURA Observation State
   ↓
Adaptive Decision Layer
   ↓
Perception / Navigation / Safety Configuration
   ↓
Robot
