#version 450

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 textureCoordinates;
layout (location = 2) in vec3 normal;

uniform float flip;
uniform mat4 theMatrix;
uniform vec3 light;


out vec2 mytexture;
out float intensity_light;

void main()
{
  float intensity = dot(normal,normalize(light-position));
  gl_Position = theMatrix * vec4(position.x, position.y *flip, position.z, 1);
  intensity_light = intensity;
  mytexture = textureCoordinates;
}