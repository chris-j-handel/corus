# Animation now, the field's account, in its own words

Sentences gathered from the field's own accounts of how a frame follows a frame, each kept as the field says it, to be seated at the six things beside all things.

## Keyframe and timeline animation
The animator sets keyframes on a timeline, each a fixed pose at a fixed time, and the software interpolates the frames between them by a curve.
Each frame is rendered at a constant frame rate, the timeline a global clock over every object in the scene.
The scene graph stores every object's position, rotation and scale, and each frame reads the stored state and writes the next.

## Physics and game loops
Every frame, you deposit the elapsed real time into a bucket, the accumulator, then you withdraw fixed-size chunks, your physics timestep, and run the simulation until the bucket no longer has enough for another step.
The integrator always receives exactly 0.0166 seconds, ensuring identical simulation behavior across different hardware.
Between frames the system stores both the previous and current physics states, and if the accumulator contains half a timestep's worth of time, alpha is 0.5 and you render the object exactly halfway between its previous and current positions.
The render loop runs as fast as the hardware allows, and the physics loop runs at a strict, fixed interval, ensuring stable integration.
The engine computes each body's next state from its current state and the forces summed on it, momentum and energy conserved by the integrator, and collisions resolved by a solver that detects contacts and applies impulses.

## AI video generation and world models
Most state-of-the-art models operate in the latent space of a pre-trained variational autoencoder, applying iterative denoising across entire sequences simultaneously.
Autoregressive models decompose video as token sequences, each frame depending on prior context, p(x) = ∏ p(x_i | x_<i), which enables frame-by-frame controllable generation but becomes computationally expensive for long videos.
A causal or streaming diffusion model generates frames or chunks incrementally without relying on future context, through temporal causal attention or block-causal design.
Between steps the model stores keyframes or semi-compressed historical frames, point clouds or meshes, latent vectors from state-space models, and KV caches of attention tensors.
An action-conditioned world model takes the user's action at each step and predicts the next frame from the stored state and the action.
The stated limits are severe train-test mismatch and error accumulation in continuous rollout, cumulative errors in long-term interactions, and struggles with spatial, logical and physical consistency over extended sequences.
