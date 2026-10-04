# Particle 3D v1

Schema ID: `mml.particle_3d.v1`

Use for animated 3D particle snapshots.

```text
# MML_SCHEMA mml.particle_3d.v1
PARTICLE_SIMULATION_DATA_3D
Width: <extent-x>
Height: <extent-y>
Depth: <extent-z>
NumBalls: <n>
<name-1> <color> <radius>
...
NumSteps: <m>
Step <step-index> <time>
<particle-index> <x> <y> <z>
...
```

Sample: `sample-data/ParticleVisualizer3D/two-particles.mml`.
