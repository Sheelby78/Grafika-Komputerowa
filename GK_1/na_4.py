#!/usr/bin/env python3
import sys
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render(time, x, y, a, c, d, r, g, b):
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(r, g, b)
    glBegin(GL_TRIANGLES)
    glVertex2f(x-d, y+d)
    glVertex2f(x+a, y)
    glVertex2f(x, y-c)
    glEnd()

    glColor3f(r, g, b)
    glBegin(GL_TRIANGLES)
    glVertex2f(x+a, y)
    glVertex2f(x+a+d, y-c-d)
    glVertex2f(x, y-c)
    glEnd()

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
    x=-25
    y=25
    a=50
    c=20
    d=50

    random.seed(a=None, version=2)

    r = random.random()
    g = random.random()
    b = random.random()


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
        render(glfwGetTime(), x, y, a, c, d, r, g, b)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
