#version 450
layout(location = 0) out vec4 fragColor;
//reference: https://learnopengl.com/Getting-started/Textures
//reference: https://glslsandbox.com/
in vec2 mytexture;
in vec4 posi;
uniform sampler2D tex;
uniform int time;
in float intensity_light;

void main()
{
  vec2 posi = posi.xy;

	float angle1 = posi.x+time;
	float angle2 = posi.y-time;

  vec4 f_color = vec4( 0.5*sin(angle1*150.0)+1.5*cos(angle2*30.0),0,0, 1.0 );
  vec4 p_color = vec4(0,0.5*sin(angle1*150.0)+1.5*cos(angle2*2.0),0.5*sin(angle1*150.0)+1.5*cos(angle2*2.0), 1.0 );

  if(mod(time/8,2)==0){
      fragColor = intensity_light*1.5*texture(tex,mytexture)*p_color;
  }else{
      fragColor = intensity_light*1.5*texture(tex,mytexture) * f_color;
  }

}
