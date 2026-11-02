// Audio-Reactive Pulse: rings that expand and brighten with audio level.
// For a TouchDesigner GLSL TOP (pixel shader).

uniform float uTime;   // seconds
uniform float uLevel;  // audio level, roughly 0 to 1

out vec4 fragColor;

void main()
{
    vec2 uv = vUV.st * 2.0 - 1.0;
    uv.x *= uTDOutputInfo.res.z / uTDOutputInfo.res.w;

    float level = clamp(uLevel, 0.0, 1.0);
    float dist = length(uv);

    float rings = sin(dist * (10.0 + level * 20.0) - uTime * 2.0);
    float glow = smoothstep(0.0, 1.0, rings) * exp(-dist * (2.5 - level * 1.5));

    vec3 color = mix(vec3(0.05, 0.15, 0.6), vec3(1.0, 0.35, 0.2), level) * glow;
    fragColor = TDOutputSwizzle(vec4(color, 1.0));
}
