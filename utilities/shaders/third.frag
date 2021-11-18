#version 450
layout(location = 0) out vec4 fragColor;
//reference: https://learnopengl.com/Getting-started/Textures
in vec2 mytexture;
uniform sampler2D tex;
uniform int time;
in vec4 posi;
in float intensity_light;

void main()
{
  vec2 posi = 4.*( posi.xy);

	vec4 f_color = vec4( .5*sin(posi.x ) + .5, .5*sin(time+posi.y) + .5, sin(time), 1.0 );
  fragColor = intensity_light*2*texture(tex,mytexture)*f_color;
}