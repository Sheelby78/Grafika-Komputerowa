#!/usr/bin/env python3
import sys
import numpy
import math
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


N = 30
tab = numpy.zeros((N, N, 6))

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


def render(time):

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 180 / 3.1415)
    axes()

    glBegin(GL_TRIANGLES)
    for i in range(0, (N-1)):
        for j in range(0, (N-1)):
            glColor3f(tab[i][j+1][3], tab[i][j+1][4], tab[i][j+1][5])
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])

            glColor3f(tab[i][j][3], tab[i][j][4], tab[i][j][5])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])

            glColor3f(tab[i+1][j][3], tab[i+1][j][4], tab[i+1][j][5])
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])

            glColor3f(tab[i][j+1][3], tab[i][j+1][4], tab[i][j+1][5])
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])

            glColor3f(tab[i+1][j+1][3], tab[i+1][j+1][4], tab[i+1][j+1][5])
            glVertex3f(tab[i+1][j+1][0], tab[i+1][j+1][1], tab[i+1][j+1][2])

            glColor3f(tab[i+1][j][3], tab[i+1][j][4], tab[i+1][j][5])
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
    glEnd()

    glFlush()

def countMatrix():
    random.seed(a=None, version=2)
    for i in range(0, N):
        u = i/(N-1)
        for j in range(0, N):
            v = j/(N-1)
            tab[i][j][0]=(-90 * math.pow(u, 5) + 225 * math.pow(u, 4) - 270 * math.pow(u, 3) + 180 * math.pow(u, 2) - 45 * u) * math.cos(math.pi * v)
            tab[i][j][1]=160*math.pow(u,4)-320*math.pow(u,3)+160*math.pow(u,2)-5
            tab[i][j][2]=(-90 * math.pow(u, 5) + 225 * math.pow(u, 4) - 270 * math.pow(u, 3) + 180 * math.pow(u, 2) - 45 * u) * math.sin(math.pi * v)
            tab[i][j][3]=random.random()
            tab[i][j][4]=random.random()
            tab[i][j][5]=random.random()


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
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    countMatrix()
 
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
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
