from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

def read_shader_file(file):
  with open(file) as f:
    return f.read()

def get_shader(shader):
  vertex_data = read_shader_file("utilities/shaders/vmain.vert")
  fragment_shader = read_shader_file(f"utilities/shaders/{shader}.frag")
  cvs = compileShader(vertex_data, GL_VERTEX_SHADER)
  cfs = compileShader(fragment_shader, GL_FRAGMENT_SHADER)

  shader = compileProgram(cvs, cfs)
  return shader

def getArrShader(position):
  shaders = ["main","first","second","third"]
  return shaders[position]