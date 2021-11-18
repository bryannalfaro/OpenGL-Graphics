#version 450
layout(location = 0) out vec4 fragColor;
//reference: https://learnopengl.com/Getting-started/Textures
in vec2 mytexture;
in vec4 posi;
uniform sampler2D tex;
uniform int time;
in float intensity_light;

void main()
{
  //vec4(mycolor, 1.0f)
  //fragColor = intensity_light*texture(tex,mytexture) +vec4(0, 0, 1.0f,1.0f);
  vec2 posi = posi.xy;

	float t1 = posi.x*150.0+time*1.0;
	float t2 = posi.y*30.0+time*2.0;

  vec4 f_color = vec4( 0.5*cos(t1)+1.5*cos(t2),0,0, 1.0 );
  vec4 p_color = vec4(0,0.5*cos(t1)+1.5*cos(t2*2.0),0.5*cos(t1)+1.5*cos(t2*2.0), 1.0 );

  if(mod(time/8,2)==0){
      fragColor = intensity_light*1.5*texture(tex,mytexture)*p_color;
  }else{
      fragColor = intensity_light*1.5*texture(tex,mytexture) * f_color;
  }

}
