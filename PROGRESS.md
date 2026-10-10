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

---

# Full AURA Roadmap

## Simulation

- [x] Gazebo Harmonic
- [x] TurtleBot3
- [x] Nav2
- [ ] NVIDIA Isaac Sim
- [ ] High-fidelity camera simulation
- [ ] High-fidelity LiDAR simulation
- [ ] Synthetic perception data
- [ ] Domain randomization

## State Estimation

- [x] Raw odometry
- [x] IMU
- [ ] Stable EKF fusion
- [ ] `/odometry/filtered`
- [ ] AMCL covariance monitoring
- [ ] estimator sanity checking

## Health Monitoring

- [x] Health Monitor V1
- [x] Health Monitor V2
- [ ] unified reliability state
- [ ] perception latency
- [ ] perception confidence
- [ ] localization reliability
- [ ] sensor disagreement detection

## Fault Injection

- [ ] LiDAR dropout
- [ ] LiDAR noise
- [ ] LiDAR occlusion
- [ ] odometry drift
- [ ] wheel slip
- [ ] IMU noise
- [ ] IMU bias
- [ ] camera dropout
- [ ] camera latency
- [ ] perception latency
- [ ] localization degradation
- [ ] compound faults

## Computer Vision

- [ ] camera pipeline
- [ ] object / obstacle perception
- [ ] confidence estimation
- [ ] latency measurement
- [ ] multiple perception modes
- [ ] Isaac Sim synthetic data

## Adaptive Control

- [ ] rule-based adaptive policy
- [ ] velocity adaptation
- [ ] safety margin adaptation
- [ ] perception mode switching
- [ ] recovery behavior
- [ ] emergency safe stop

## Reinforcement Learning

- [ ] RL observation space
- [ ] action space
- [ ] reward function
- [ ] training environment
- [ ] PPO training
- [ ] policy checkpointing
- [ ] ROS 2 inference node
- [ ] Gazebo evaluation
- [ ] Isaac Sim evaluation

## Experiments

- [ ] Standard Nav2 baseline
- [ ] Rule-Based AURA
- [ ] PPO AURA
- [ ] single-fault evaluation
- [ ] compound-fault evaluation
- [ ] unseen fault combinations
- [ ] trajectory comparison
- [ ] collision analysis
- [ ] completion-time analysis
- [ ] safety analysis
- [ ] compute-cost analysis

## Final Output

- [ ] Gazebo demo
- [ ] Isaac Sim demo
- [ ] animated README demo
- [ ] GitHub Pages visualization
- [ ] architecture diagram
- [ ] experiment plots
- [ ] results tables
- [ ] technical README
- [ ] research report / paper
- [ ] final portfolio presentation

