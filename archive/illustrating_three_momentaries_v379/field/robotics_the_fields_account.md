# Robotics now, the field's account, in its own words

Sentences in the field's standard terms for how a robot arrives at its next action, to be seated at the six things beside all things.

The controller runs at a fixed control rate, reading the sensors, estimating the state, and commanding the actuators at each tick of its clock.
A state estimator such as a Kalman filter fuses the sensor readings with a motion model to maintain an estimate of the robot's position and velocity, stored and updated at each step.
Odometry integrates wheel or inertial measurements over time, and its error accumulates without bound until a loop closure or an external fix corrects the drift.
Simultaneous localization and mapping builds and stores a map of the environment while estimating the robot's pose within it, and the map is the reference the robot plans against.
A trajectory is planned in advance from the current state to a goal, and a tracking controller drives the error between the planned and the measured state toward zero.
A policy learned in simulation is transferred to the physical robot, and the sim-to-real gap is the accumulated mismatch between the simulated and the physical dynamics, contacts and sensing.
In imitation learning the policy's small errors compound along the rollout, carrying the robot into states its training never covered.
A robot swarm receives a common program and a target shape, four seed robots establish the coordinate origin, and each robot localizes by distance estimates to its neighbors while retaining the shape and its coordinates.
A world model predicts the next observation from the stored latent state and the chosen action, and cumulative errors in long-term interactions limit the horizon it can plan over.
An event-based vision sensor has no frames: each pixel emits an ON or OFF event asynchronously, only when its log intensity changes past a threshold.
