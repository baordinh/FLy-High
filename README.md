# Fly High

Fly High is an open-source collection of TouchDesigner components (.tox), generative art pieces, and Python/GLSL scripts, released under the MIT License with documentation for each piece.

The gap: TouchDesigner has a strong visual-art community, but much of the best work is closed or shared as undocumented project files, which makes it hard for beginners to learn from or reuse. I want to publish well-documented, reusable building blocks (audio-reactive visuals, particle systems, real-time shaders) that other artists can drop into their own work. I work in motion graphics and 3D (Blender, After Effects, Unity), and the repo is public at my Github.

## Status

Early stage. No `.tox` has been published yet. The first piece, [Audio-Reactive Pulse](components/audio-reactive-pulse/README.md), currently ships as a shader and a build script, and has not been tested inside TouchDesigner yet.

## Repository layout

```
components/   One folder per component: docs, and the .tox and preview once available
shaders/      GLSL shaders
scripts/      Python scripts that run inside TouchDesigner
```

## License

[MIT](LICENSE)
