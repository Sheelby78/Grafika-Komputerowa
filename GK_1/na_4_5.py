#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def draw(x, y, a, b):
    if a<10:
        return
    
    x2=x/3
    y2=y/3
    a2=a/3
    b2=b/3

    glColor3f(1.0, 0.5, 0.5)
    glBegin(GL_LINES)
    glVertex2f(x,y-(b/3))
    glVertex2f(x+a,y-(b/3))
    glVertex2f(x,(y-(b/3))-(b/3))
    glVertex2f(x+a,(y-(b/3))-(b/3))
    glVertex2f(x+(a/3),y)
    glVertex2f(x+(a/3),y-b)
    glVertex2f((x+(a/3))+(a/3),y)
    glVertex2f((x+(a/3))+(a/3),y-b)
    glEnd()
    

    x+=a2
    y-=b2

    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x+a2, y)
    glVertex2f(x, y-b2)
    glEnd()

    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x+a2, y)
    glVertex2f(x+a2, y-b2)
    glVertex2f(x, y-b2)
    glEnd()

    x-=a2
    y+=b2

    draw(x,y,a2,b2)
    draw(x+a2,y,a2,b2)
    draw(x+(a2*2),y,a2,b2)
    draw(x+(a2*2),y-b2,a2,b2)
    draw(x,y-b2,a2,b2)
    draw(x,y-(2*b2),a2,b2)
    draw(x+a2,y-(2*b2),a2,b2)
    draw(x+(2*a2),y-(2*b2),a2,b2)


def render(time, x, y, a, b):
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x+a, y)
    glVertex2f(x, y-b)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x+a, y)
    glVertex2f(x+a, y-b)
    glVertex2f(x, y-b)
    glEnd()

    glColor3f(1.0, 0.5, 0.5)
    glBegin(GL_LINES)
    glVertex2f(x,y/3)
    glVertex2f(x+a,y/3)
    glVertex2f(x,(y/3)-(b/3))
    glVertex2f(x+a,(y/3)-(b/3))
    glVertex2f(x/3,y)
    glVertex2f(x/3,y-b)
    glVertex2f((x/3)+(a/3),y)
    glVertex2f((x/3)+(a/3),y-b)
    glEnd()

    x2=x/3
    y2=y/3
    a2=a/3
    b2=b/3

    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x2, y2)
    glVertex2f(x2+a2, y2)
    glVertex2f(x2, y2-b2)
    glEnd()

    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x2+a2, y2)
    glVertex2f(x2+a2, y2-b2)
    glVertex2f(x2, y2-b2)
    glEnd()


    draw(x,y,a2,b2)
    draw(x+a2,y,a2,b2)
    draw(x+(a2*2),y,a2,b2)
    draw(x+(a2*2),y-b2,a2,b2)
    draw(x,y-b2,a2,b2)
    draw(x,y-(2*b2),a2,b2)
    draw(x+a2,y-(2*b2),a2,b2)
    draw(x+(2*a2),y-(2*b2),a2,b2)

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
    x=-150
    y=100
    a=300
    b=200
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
        render(glfwGetTime(), x, y, a, b)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
