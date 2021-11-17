#version 450
layout(location = 0) out vec4 fragColor;
//reference: https://learnopengl.com/Getting-started/Textures
in vec2 mytexture;
in float intensity_light;
uniform sampler2D tex;
void main()
{
  //vec4(mycolor, 1.0f)
  fragColor = intensity_light*texture(tex,mytexture);
}
