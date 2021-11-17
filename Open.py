import pygame
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from math import sin
from main import *
from utilities.shaders.shader_manage import *

pygame.init()
screen = pygame.display.set_mode((1200, 720), pygame.OPENGL | pygame.DOUBLEBUF)
glClearColor(0.1, 0.2, 0.5, 1.0)
glEnable(GL_DEPTH_TEST) #habilitar zbuffer
glEnable(GL_TEXTURE_2D)
clock = pygame.time.Clock()
shaders = ["1fr","fmain","rfrag"]

texture = pygame.image.load('utilities/texture/textureWolf.bmp')
t_data = pygame.image.tostring(texture, "RGB", 1)
width = texture.get_width()
height = texture.get_height()

angle = 0
angle2 = 0
running = True


shader = get_shader(shaders[0])
makeflip = 1
pos_x,pos_y,pos_z = 0,0,5
while running:
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  angle +=5
  angle2 +=1

  #len_d = prepare_data(shader)
  prepare_data(shader,t_data,width,height)
  #Enviar informacion al shader
  glUniform1f(glGetUniformLocation(shader, "flip"),makeflip)
  renderMatrix(angle,angle2,shader,pos_x,pos_y,pos_z)

  #Pintar luego de uniforms
  #glDrawElements(GL_TRIANGLES, len_d, GL_UNSIGNED_INT, None) #glDrawArrays(GL_TRIANGLES, 0, 3) ahora no son arrays, son elementos

  pygame.display.flip()
  clock.tick(30) # perder tiempo
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_g:
          glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
      if event.key == pygame.K_h:
          glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
      if event.key == pygame.K_j:
          shader = get_shader(shaders[0])
      if event.key == pygame.K_k:
          shader = get_shader(shaders[1])
      if event.key == pygame.K_l:
          shader = get_shader(shaders[2])
      if event.key == pygame.K_w:
          pos_y+=0.1
      if event.key == pygame.K_s:
          pos_y-=0.1
      if event.key == pygame.K_d:
          pos_x+=0.1
      if event.key == pygame.K_a:
          pos_x-=0.1
      if event.key == pygame.K_e:
          pos_z+=0.1
      if event.key == pygame.K_q:
          pos_z-=0.1