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

    glColor3f(0.2, 0.4, 0.8)
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(0, (N-1)):
        for j in range(0, (N-1)):

            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])

            #glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])

            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])

            #glVertex3f(tab[i+1][j+1][0], tab[i+1][j+1][1], tab[i+1][j+1][2])
    glEnd()

    g =-3.9

    glColor3f(0.9, 0.2, 0.9)
    for z in range(0, 3):
        glBegin(GL_TRIANGLE_STRIP)
        for i in range(0, (N-1)):
            for j in range(0, (N-1)):

                glVertex3f(tab[i][j][0]+g, tab[i][j][1], tab[i][j][2])

                #glVertex3f(tab[i][j+1][0]+g, tab[i][j+1][1], tab[i][j+1][2])

                glVertex3f(tab[i+1][j][0]+g, tab[i+1][j][1], tab[i+1][j][2])

                #glVertex3f(tab[i+1][j+1][0]+g, tab[i+1][j+1][1], tab[i+1][j+1][2])
        glEnd()
        g+=3.9

    g=-3.9

    glColor3f(0.2, 0.1, 0.9)
    for z in range(0, 2):
        glBegin(GL_TRIANGLE_STRIP)
        for i in range(0, (N-1)):
            for j in range(0, (N-1)):

                glVertex3f(tab[i][j][0]+g, tab[i][j][1]+g, tab[i][j][2])

                #glVertex3f(tab[i][j+1][0]+g, tab[i][j+1][1]+g, tab[i][j+1][2])

                glVertex3f(tab[i+1][j][0]+g, tab[i+1][j][1]+g, tab[i+1][j][2])

                #glVertex3f(tab[i+1][j+1][0]+g, tab[i+1][j+1][1]+g, tab[i+1][j+1][2])
        glEnd()
        g+=7.8

    g =-3.9
    glColor3f(0.9, 0.9, 0.1)
    for z in range(0, 2):
        glBegin(GL_TRIANGLE_STRIP)
        for i in range(0, (N-1)):
            for j in range(0, (N-1)):

                glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2]+g)

                #glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2]+g)

                glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2]+g)

                #glVertex3f(tab[i+1][j+1][0], tab[i+1][j+1][1], tab[i+1][j+1][2]+g)
        glEnd()
        g+=7.8


    glFlush()

def countMatrix():
    random.seed(a=None, version=2)
    u=-6.28;
    f = 6.28/(N-1)
    g = 12.56/(N-1)
    for i in range(0, N):
        v=-12.56;
        for j in range(0, N):
            tab[i][j][0]=2*math.cos(u)*math.cos(v)
            tab[i][j][1]=2*math.cos(u)*math.sin(v)
            tab[i][j][2]=2*math.sin(u)
            v +=g
        u+=f

    

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
