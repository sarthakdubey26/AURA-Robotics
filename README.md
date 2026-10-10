<div align="center">

# AURA

### Adaptive Uncertainty-Aware Robotic Autonomy

**A health-aware autonomous robotics framework that detects when its own sensing, perception, and localization become unreliable — and adapts before uncertainty becomes failure.**

<br>

![ROS 2](https://img.shields.io/badge/ROS%202-Jazzy-22314E?style=for-the-badge&logo=ros)
![Gazebo](https://img.shields.io/badge/Gazebo-Harmonic-F58113?style=for-the-badge)
![Isaac Sim](https://img.shields.io/badge/NVIDIA-Isaac%20Sim-76B900?style=for-the-badge&logo=nvidia)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python)

<br>

![Nav2](https://img.shields.io/badge/Navigation-Nav2-4C8BF5?style=flat-square)
![RL](https://img.shields.io/badge/Reinforcement%20Learning-PPO-8A2BE2?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active%20Development-F5A623?style=flat-square)

<br><br>

`Gazebo` • `Isaac Sim` • `Sensor Fusion` • `Fault Injection` • `Computer Vision` • `Adaptive Control` • `Reinforcement Learning`

</div>

---

## Why AURA?

Most autonomous robots answer:

> **What is happening around me?**

AURA adds a second question:

> **How much should I trust what I currently know?**

AURA continuously monitors the reliability of its sensing, localization, perception, and state-estimation stack and uses that information to adapt robot behavior online.

---

## System at a Glance

```mermaid
flowchart LR

    S["Sensors"] --> H["Health + Uncertainty Monitor"]

    H --> R["Reliability State"]

    R --> RB["Rule-Based Policy"]
    R --> RL["PPO Policy"]

    RB --> A["Adaptive Decision Layer"]
    RL --> A

    A --> N["Nav2"]
    N --> ROBOT["Robot"]

    ROBOT --> S
