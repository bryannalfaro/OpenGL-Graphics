#version 450
layout(location = 0) out vec4 fragColor;

in vec3 mycolor;

void main()
{
  fragColor = vec4(mycolor, 1.0f);
}
