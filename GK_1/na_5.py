#!/usr/bin/env python3
import sys
import math

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

def draw(x,y,a,h):

    if a<5:
        return
    
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    h/=2
    a/=2

    glVertex2f(x-(a/2), y+((h)*1/3))
    glVertex2f(x+(a/2), y+((h)*1/3))
    glVertex2f(x, y-(h*2/3))
    glEnd()
    h*=2
    a*=2

    draw(x,y+h*2/6,a/2,h/2)
    draw(x-a/4,y-(h*1/3)+h*1/6,a/2,h/2)
    draw(x+a/4,y-(h*1/3)+h*1/6,a/2,h/2)


def render(time, x, y, a):
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.42, 0.12, 0.12)
    glBegin(GL_TRIANGLES)
    h = (a*math.sqrt(3))/2
    glVertex2f(x, y+(h*2/3))
    glVertex2f(x+(a/2), y-(h*1/3))
    glVertex2f(x-(a/2), y-(h*1/3))
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x-(a/4), y+((h/2)*1/3))
    glVertex2f(x+(a/4), y+((h/2)*1/3))
    glVertex2f(x, y-(h/2*2/3))
    glEnd()


    draw(x,y+h*2/6,a/2,h/2)
    draw(x-a/4,y-(h*1/3)+h*1/6,a/2,h/2)
    draw(x+a/4,y-(h*1/3)+h*1/6,a/2,h/2)

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    a=170
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime(), 0, 0, a)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
