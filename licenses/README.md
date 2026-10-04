# Licenses And Notices

Released archives include first-party and runtime license/notice files under their extracted
`licenses/` directory.

This public companion repository carries release documentation, schemas, and sample data. The
visualizer application source remains private. Binary releases must include notices for redistributed
runtime components, including Qt when Qt runtime libraries or plugins are bundled.

The MML Visualizers applications are free for personal, educational, and non-commercial academic use.
Commercial use requires a separate paid commercial license; see
[MML-Visualizers-LICENSE.md](MML-Visualizers-LICENSE.md).

Expected archive files:

```text
licenses/
  MML-Visualizers-LICENSE.md
  third-party-notices.md
  Qt-LICENSE.md
  FLTK-LICENSE.md
  DotNet-WPF-NOTICES.md
  OpenGL-NOTICES.md
  Compiler-Runtime-NOTICES.md
  ICU-LICENSE.md
```

Release validation fails if this baseline notice set is absent. Before publishing an artifact,
inspect the exact redistributed binaries for that platform and extend these files with any
additional notice text required by the dependencies actually shipped.
