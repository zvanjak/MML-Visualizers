# Particle 2D v1

Schema ID: `mml.particle_2d.v1`

Use for animated 2D particle snapshots. Public files retain the current visualizer layout: a particle catalog followed by time steps.

```text
# MML_SCHEMA mml.particle_2d.v1
MML_PARTICLE_SIMULATION_DATA_2D
VERSION: 1
Width: <viewport-width>
Height: <viewport-height>
NumBalls: <n>
<name-1> <color> <radius>
...
NumSteps: <m>
Step <step-index> <time>
<particle-index> <x> <y>
...
```

Particle indices in step blocks are zero-based visualizer indices. Catalog names are display names.

Sample: `sample-data/ParticleVisualizer2D/two-particles.mml`.
