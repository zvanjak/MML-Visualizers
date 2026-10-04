# Vector Field 2D v1

Schema ID: `mml.vector_field_2d.v1`

Use for sampled vector fields in the plane.

```text
# MML_SCHEMA mml.vector_field_2d.v1
# columns: x y vx vy
VECTOR_FIELD_2D_CARTESIAN
<title>
<x> <y> <vx> <vy>
...
```

The current visualizers infer the field extent from the supplied sample positions.

Sample: `sample-data/VectorField2D/rotation.mml`.
