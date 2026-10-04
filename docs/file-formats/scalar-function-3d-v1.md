# Scalar Function 3D v1

Schema ID: `mml.scalar_function_3d.v1`

Use for sampled volumetric scalar fields.

```text
# MML_SCHEMA mml.scalar_function_3d.v1
# columns: x y z value
SCALAR_FUNCTION_CARTESIAN_3D
<title>
x1: <min-x>
x2: <max-x>
NumPointsX: <nx>
y1: <min-y>
y2: <max-y>
NumPointsY: <ny>
z1: <min-z>
z2: <max-z>
NumPointsZ: <nz>
<x> <y> <z> <value>
...
```

Sample: `sample-data/ScalarFunction3D/gaussian-blob.mml`.
