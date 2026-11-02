# Audio-Reactive Pulse

Rings that expand and shift color with the level of an audio input.

**Status: untested.** The shader and build script have not been run inside TouchDesigner yet, so operator parameter names may need fixing. There is no `.tox` or preview until they have been.

## Build the .tox

1. Open `scripts/build_audio_reactive_pulse.py` and set `SHADER_PATH` and `TOX_PATH`.
2. In TouchDesigner, paste the script into a Text DAT.
3. Right-click the DAT and choose Run Script.

The script creates `/project1/audio_reactive_pulse` and saves the `.tox`.

## Parameters

| Parameter | Default | Effect |
| --- | --- | --- |
| Gain | 4.0 | Multiplies the audio level before it reaches the shader |

## Output

`out1`: a 1280×720 TOP.

## Source

- Shader: [`shaders/audio_reactive_pulse.frag`](../../shaders/audio_reactive_pulse.frag)
- Build script: [`scripts/build_audio_reactive_pulse.py`](../../scripts/build_audio_reactive_pulse.py)
