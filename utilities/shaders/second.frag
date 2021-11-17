#version 450
layout(location = 0) out vec4 fragColor;
//reference: https://learnopengl.com/Getting-started/Textures
in vec2 mytexture;
uniform sampler2D tex;
in float intensity_light;
void main()
{
  //vec4(mycolor, 1.0f)
  fragColor = intensity_light*texture(tex,mytexture) +vec4(0, 0, 1.0f,1.0f);
}
