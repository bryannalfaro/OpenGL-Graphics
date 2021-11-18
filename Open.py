import pygame
from OpenGL.GL import *
from math import sin
from main import *
from utilities.shaders.shader_manage import *

pygame.init()
screen = pygame.display.set_mode((1200, 720), pygame.OPENGL | pygame.DOUBLEBUF)
max_zoom = 3
min_zoom = -1

max_zoomz = 10
min_zoomz = 4


pygame.display.set_caption('3D Visualizer')


glClearColor(1, 1, 1, 1.0)
glEnable(GL_DEPTH_TEST) #habilitar zbuffer
glEnable(GL_TEXTURE_2D)
clock = pygame.time.Clock()
shaders = ["main","first","second","third"]

texture = pygame.image.load('utilities/texture/textureWolf.bmp')
t_data = pygame.image.tostring(texture, "RGB", 1)
width = texture.get_width()
height = texture.get_height()

angle2 = 0
running = True


shader = get_shader(shaders[0])
makeflip = 1
pos_x,pos_y,pos_z = 0,0,5
sound = pygame.mixer.Sound('utilities/sound/nature.mp3')
sound.play()
while running:
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  angle2 +=1

  prepare_data(shader,t_data,width,height)
  #Enviar informacion al shader
  glUniform1f(glGetUniformLocation(shader, "flip"),makeflip)
  renderMatrix(angle2,shader,pos_x,pos_y,pos_z)

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
          sound.stop()
          shader = get_shader(shaders[0])
          sound = pygame.mixer.Sound('utilities/sound/nature.mp3')
          sound.play()

      if event.key == pygame.K_k:
          shader = get_shader(shaders[1])
          sound.stop()
          sound = pygame.mixer.Sound('utilities/sound/chris.mp3')
          sound.play()
      if event.key == pygame.K_l:
          sound.stop()
          shader = get_shader(shaders[2])
          sound = pygame.mixer.Sound('utilities/sound/dance.mp3')
          sound.play()
      if event.key == pygame.K_p:
        sound.stop()
        shader = get_shader(shaders[3])
        sound = pygame.mixer.Sound('utilities/sound/electronic.mp3')
        sound.play()
      if event.key == pygame.K_w:
          if(pos_y+0.1<=max_zoom and pos_y+0.1 >=min_zoom):
              pos_y += 0.1

      if event.key == pygame.K_s:
          if(pos_y-0.1<=max_zoom and pos_y-0.1 >=min_zoom):
              pos_y -= 0.1
      if event.key == pygame.K_d:
          if(pos_x+0.1<=max_zoom and pos_x+0.1 >=min_zoom):
              pos_x += 0.1

      if event.key == pygame.K_a:
          if(pos_x-0.1<=max_zoom and pos_x-0.1 >=min_zoom):
              pos_x -= 0.1
      if event.key == pygame.K_e:
          if(pos_z+0.1<=max_zoomz and pos_z+0.1 >=min_zoomz):
              pos_z += 0.1
      if event.key == pygame.K_q:
          if(pos_z-0.1<=max_zoomz and pos_z-0.1 >=min_zoomz):
              pos_z -= 0.1