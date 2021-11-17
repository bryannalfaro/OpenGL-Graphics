#version 450

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 textureCoordinates;
uniform float flip;
uniform mat4 theMatrix;

out vec2 mytexture;

void main()
{
  gl_Position = theMatrix * vec4(position.x, position.y *flip, position.z, 1);
  mytexture = textureCoordinates;
}