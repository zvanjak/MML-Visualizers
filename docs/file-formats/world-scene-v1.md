# World Scene v1

Schema ID: `mml.world_scene.v1`
Launcher kind: `world`
Typical extension: `.mmlworld`
Archive families: WPF

World scene files describe a lightweight 3D scene for the WPF `MML_WorldVisualizer`. They are plain text and are intended for generated educational and diagnostic scenes such as coordinate frames, differential-form glyphs, and sampled field geometry.

## Header

```text
# MML_SCHEMA mml.world_scene.v1
MML_WORLD_SCENE 1
TITLE Example world scene
CAMERA 260 180 220
```

The `# MML_SCHEMA` comment is the public stable schema identifier used by `mmlviz open`. The first non-comment line remains the legacy visualizer header.

## Commands

All command names are case-insensitive. Numeric values use invariant-culture decimal text.

```text
TITLE <free text>
CAMERA <x> <y> <z>
POINT <x> <y> <z> <radius> <color>
VECTOR <x> <y> <z> <dx> <dy> <dz> <radius> <color>
VECTOR_AT_POINT <x> <y> <z> <dx> <dy> <dz> <radius> <color>
LINE <x0> <y0> <z0> <x1> <y1> <z1> <radius> <color>
PLANE <cx> <cy> <cz> <nx> <ny> <nz> <size> <color> <opacity>
PATCH <cx> <cy> <cz> <ux> <uy> <uz> <vx> <vy> <vz> <color> <opacity>
CIRCLE <cx> <cy> <cz> <radius> <nx> <ny> <nz> <line-radius> <color>
SPHERE_WIREFRAME <cx> <cy> <cz> <radius> <n-lat> <n-lon> <segments-lat> <segments-lon> <line-radius> <color>
```

Colors are `#RRGGBB` or `#AARRGGBB`. Opacity values are clamped by the visualizer to the range `[0, 1]`.

## Example

See [sample-data/WorldScene/basis-arrows.mmlworld](../../sample-data/WorldScene/basis-arrows.mmlworld).
