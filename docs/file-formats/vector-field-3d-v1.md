# Vector Field 3D v1

Schema ID: `mml.vector_field_3d.v1`

Use for sampled vector fields in 3D.

```text
# MML_SCHEMA mml.vector_field_3d.v1
# columns: x y z vx vy vz
VECTOR_FIELD_3D_CARTESIAN
<title>
<x> <y> <z> <vx> <vy> <vz>
...
```

The current visualizers infer the field extent from the supplied sample positions.

Sample: `sample-data/VectorField3D/radial.mml`.
