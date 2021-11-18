#version 450
layout(location = 0) out vec4 fragColor;

//reference: https://learnopengl.com/Getting-started/Textures
in vec2 mytexture;
uniform sampler2D tex;
uniform int time;
in float intensity_light;
in vec4 posi;

void main()
{
  vec2 pos = posi.xy;

	vec4 f_color = vec4( vec3( pos.y, (.5 - (pos.x ) / 2.), 1. - (pos.y) ), 1.0 );
  vec4 n_color = vec4( vec3( (.5 - (pos.x ) / 2.),pos.y , 1. - (pos.y)),1.0);
  vec4 p_color = vec4( vec3(1. - (pos.x), (.5 - (pos.y ) / 2.),pos.y ),1.0);


  if(mod(time/3,2)==0){
      fragColor = intensity_light*1.5*texture(tex,mytexture)*n_color;
  }
  if(mod(time/3,5)==0){
      fragColor = intensity_light*texture(tex,mytexture)*p_color;
  }
  if(mod(time/3,3)==0){
      fragColor = intensity_light*texture(tex,mytexture)*p_color;
  }
  else{
    fragColor = intensity_light*texture(tex,mytexture)*f_color.yxzw;
  }

}
