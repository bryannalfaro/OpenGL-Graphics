import pygame
import numpy
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import glm
from math import sin
from utilities.shaders import *


def prepare_data(shader):
  vertex_data = numpy.array([
    -0.5, -0.5, 0, 1.0,0,0,
    0.5, -0.5, 0, 0,1.0,0,
    0, 0.5,  0,0,0,1.0
  ], dtype=numpy.float32)

  #Faces
  index_data = numpy.array([
    0,1,2
  ], dtype=numpy.uint32)

  len_index = len(index_data)

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
    4 * 6, # stride
    ctypes.c_void_p(0)
  )
  glEnableVertexAttribArray(0) #Habilitar

  #Necesita estar despues del primer vertex arrays
  #Faces in index data load memory
  element_buffer_object = glGenBuffers(1)
  glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, element_buffer_object)
  glBufferData(GL_ELEMENT_ARRAY_BUFFER, index_data.nbytes, index_data, GL_STATIC_DRAW)

  #Color
  glVertexAttribPointer(
    1, # location
    3, # size
    GL_FLOAT, # tipo
    GL_FALSE, # normalizados
    4 * 6, # stride
    ctypes.c_void_p(4*3)
  )
  glEnableVertexAttribArray(1) #Habilitar

  glUseProgram(shader) # usar shader

  #Pintar luego de uniforms
  glDrawElements(GL_TRIANGLES, len(index_data), GL_UNSIGNED_INT, None)

  return len_index



#Matrices
def renderMatrix(a,a2,shader):
  i = glm.mat4(1)
  translate = glm.translate(i, glm.vec3(0,0,0))
  scale = glm.scale(i, glm.vec3(1,1,1))
  rotate = glm.rotate(i, sin(glm.radians(a)), glm.vec3(0,1,0)) #rotate model , glm.radians(a)

  model = translate * rotate * scale

  #Matriz de vista
  view = glm.lookAt(
    glm.vec3(0,0,5), # donde esta, parametros para alejarla
    glm.vec3(0,0,0), #donde ve
    glm.vec3(0,1,0) #up
  )

  projection = glm.perspective(glm.radians(45), 1200/720, 0.1, 100.0) #apertura, aspect ratio, near, far

  theMatrix = projection * view * model

  #Viewport
  glViewport(0, 0, 1200, 720)

  #Send matrix to shader
  #location, size, boolean, pointer
  glUniformMatrix4fv(glGetUniformLocation(shader, "theMatrix"), 1, GL_FALSE, glm.value_ptr(theMatrix))

