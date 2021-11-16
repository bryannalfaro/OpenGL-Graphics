#version 450

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 ccolor;
uniform float flip;
uniform mat4 theMatrix;

out vec3 mycolor;

void main()
{
  gl_Position = theMatrix * vec4(position.x, position.y *flip, position.z, 1);
  mycolor = ccolor;
}