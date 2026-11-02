# Builds the Audio-Reactive Pulse component and saves it as a .tox.
# Run inside TouchDesigner. See components/audio-reactive-pulse/README.md.

# Edit these two paths to match your clone of the repo.
SHADER_PATH = r"C:/path/to/FLy-High/shaders/audio_reactive_pulse.frag"
TOX_PATH = r"C:/path/to/FLy-High/components/audio-reactive-pulse/audio_reactive_pulse.tox"

with open(SHADER_PATH, encoding="utf-8") as f:
    shader_source = f.read()

comp = op("/project1").create(baseCOMP, "audio_reactive_pulse")

page = comp.appendCustomPage("Pulse")
page.appendFloat("Gain")
comp.par.Gain = 4.0

audio_in = comp.create(audiodeviceinCHOP, "audio_in")

analyze = comp.create(analyzeCHOP, "analyze")
analyze.par.function = "rmspower"
analyze.inputConnectors[0].connect(audio_in)

level = comp.create(lagCHOP, "level")
level.par.lag1 = 0.02
level.par.lag2 = 0.25
level.inputConnectors[0].connect(analyze)

pixel = comp.create(textDAT, "pixel_shader")
pixel.text = shader_source

glsl = comp.create(glslTOP, "glsl")
glsl.par.outputresolution = "custom"
glsl.par.resolutionw = 1280
glsl.par.resolutionh = 720
glsl.par.pixeldat = pixel.name

glsl.par.uniname0 = "uTime"
glsl.par.value0x.mode = ParMode.EXPRESSION
glsl.par.value0x.expr = "absTime.seconds"

glsl.par.uniname1 = "uLevel"
glsl.par.value1x.mode = ParMode.EXPRESSION
glsl.par.value1x.expr = "op('level')[0] * parent().par.Gain"

out = comp.create(outTOP, "out1")
out.inputConnectors[0].connect(glsl)

comp.save(TOX_PATH)
print("Saved", TOX_PATH)
