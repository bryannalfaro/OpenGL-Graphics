import pygame
import numpy
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import glm
from math import sin
from main import *
from utilities.shaders.shader_manage import *

pygame.init()
screen = pygame.display.set_mode((1200, 720), pygame.OPENGL | pygame.DOUBLEBUF)
glClearColor(0.1, 0.2, 0.5, 1.0)
glEnable(GL_DEPTH_TEST) #habilitar zbuffer
clock = pygame.time.Clock()
shaders = ["fmain","rfrag"]

angle = 0
angle2 = 0
running = True


shader = get_shader(shaders[0])
makeflip = 1
while running:
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  angle +=5
  angle2 +=1

  len_d = prepare_data(shader)
  #Enviar
  glUniform1f(glGetUniformLocation(shader, "flip"),makeflip)
  renderMatrix(angle,angle2,shader)

  #Pintar luego de uniforms
  glDrawElements(GL_TRIANGLES, len_d, GL_UNSIGNED_INT, None) #glDrawArrays(GL_TRIANGLES, 0, 3) ahora no son arrays, son elementos

  pygame.display.flip()
  clock.tick(30) # perder tiempo
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
          #makeflip*=-1
          shader = get_shader(shaders[1])
          glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
      if event.key == pygame.K_b:
          shader = get_shader(shaders[0])
          glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)