#version 450
layout(location = 0) out vec4 fragColor;
//reference: https://learnopengl.com/Getting-started/Textures
//reference: https://glslsandbox.com/
in vec2 mytexture;
uniform sampler2D tex;
uniform int time;
in vec4 posi;
in float intensity_light;

void main()
{

	vec4 f_color = vec4( 0.5*sin((4.0*( posi.xy)).x ) + 0.5, 0.5*sin(time+(4.0*( posi.xy)).y) + 0.5, sin(time), 1.0 );
  fragColor = intensity_light*2*texture(tex,mytexture)*f_color;
}