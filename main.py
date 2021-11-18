import numpy
from OpenGL.GL import *
import glm
from math import sin
from utilities.shaders import *
from utilities.obj import *

def prepare_data(shader,t_data,width, height):

  texture = glGenTextures(1)
  glBindTexture(GL_TEXTURE_2D, texture)
  glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, t_data)
  glGenerateMipmap(GL_TEXTURE_2D)

  model = Obj('utilities/model/wolf.obj')


  vertices = []
  texture = []
  norm = []
  for face in (model.faces):
            for v in range(len(face)):
                vertices.append((model.vertices[face[v][0]-1]))
                texture.append((model.tvertices[face[v][1]-1]))

                norm.append((model.nvertices[face[v][2]-1]))

  #Vertices
  vertex_data = numpy.hstack([
    numpy.array(vertices, dtype=numpy.float32),
    numpy.array(texture, dtype=numpy.float32),
    numpy.array(norm, dtype=numpy.float32)
  ])

  vertex_buffer_object = glGenBuffers(1)
  glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
  glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)


  vertex_array_object = glGenVertexArrays(1)
  glBindVertexArray(vertex_array_object)

  #Vertices
  glVertexAttribPointer(
    0, # location
    3, # size
    GL_FLOAT, # tipo
    GL_FALSE, # normalizados
    4 * 8, # stride
    ctypes.c_void_p(0)
  )
  glEnableVertexAttribArray(0) #Habilitar memoria

  #Color texture
  glVertexAttribPointer(
    1, # location
    2, # size
    GL_FLOAT, # tipo
    GL_FALSE, # normalizados
    4 * 8, # stride
    ctypes.c_void_p(4*3)
  )
  glEnableVertexAttribArray(1) #Habilitar

  #Normales
  glVertexAttribPointer(
    2, # location
    3, # size
    GL_FLOAT, # tipo
    GL_FALSE, # normalizados
    4 * 8, # stride
    ctypes.c_void_p(4*5)
  )
  glEnableVertexAttribArray(2) #Habilitar

  glUseProgram(shader) # usar shader

  #Pintar luego de uniforms
  glDrawArrays(GL_TRIANGLES,0,len(vertex_data))



#Matrices
def renderMatrix(a,a2,shader,pos_x,pos_y,pos_z):
  i = glm.mat4(1)
  light = glm.vec3(-150,300,0)
  #MODELO
  translate = glm.translate(i, glm.vec3(0,0,0))
  scale = glm.scale(i, glm.vec3(0.02,0.02,0.02))
  rotate = glm.rotate(i, 0,glm.vec3(glm.radians(pos_x),glm.radians(pos_y),glm.radians(pos_z))) #rotate model , glm.radians(a)
  #rotate = glm.rotate(i, sin(glm.radians(a*0.5)), glm.vec3(0,1,0)) #rotate model , glm.radians(a)

  model = translate * rotate * scale

  #Matriz de vista
  view = glm.lookAt(
    glm.vec3(pos_x,pos_y,pos_z), # donde esta, parametros para alejarla
    glm.vec3(0,0,0), #donde ve
    glm.vec3(0,1,0) #up
  )

  projection = glm.perspective(glm.radians(45), 1200/720, 0.1, 100.0) #apertura, aspect ratio, near, far

  theMatrix = projection * view * model

  #Viewport
  glViewport(0, 0, 1200, 720)
  #color = glm.vec4(0.2,0.2,0.2,1)
  #Send matrix to shader
  #location, size, boolean, pointer
  glUniformMatrix4fv(glGetUniformLocation(shader, "theMatrix"), 1, GL_FALSE, glm.value_ptr(theMatrix))
  glUniform3f(glGetUniformLocation(shader, "light"), light.x, light.y, light.z)
  glUniform1i(glGetUniformLocation(shader, "time"), a2)

