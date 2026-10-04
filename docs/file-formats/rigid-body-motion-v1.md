# Rigid Body Motion v1

Schema ID: `mml.rigid_body_motion.v1`

Use for one rigid body trajectory with pose, linear velocity, and angular velocity samples.

```text
# MML_SCHEMA mml.rigid_body_motion.v1
RIGID_BODY_TRAJECTORY_3D
# comments are allowed
Type: <BOX|SPHERE|...>
Name: <display-name>
Mass: <mass>
HalfExtents: <hx> <hy> <hz>
Color: <color>
Container: <size>
NumFrames: <n>
# time, x, y, z, qw, qx, qy, qz, vx, vy, vz, wx, wy, wz
<time>, <x>, <y>, <z>, <qw>, <qx>, <qy>, <qz>, <vx>, <vy>, <vz>, <wx>, <wy>, <wz>
...
```

Quaternions are scalar-first: `qw, qx, qy, qz`.

Sample: `sample-data/RigidBodyMovement/spinning-box.mml`.
