import pyglet
from pyglet.gl import *
from math import *
from random import randint


# function to calculate vertices of an equilateral triangle
def makeTriangle(radius, xcenter, ycenter):
    numberOfVertices = 3                        # specify the number of vertices we need for the shape
    vertices = []                               # initialize a list of vertices

    for i in range(0,3):
        angle = i*(2.0/3.0)*pi
        x = radius * cos(angle) + xcenter
        y = radius * sin(angle) + ycenter
        vertices.append(x)                          # append the x value to the vertex list
        vertices.append(y)                          # append the y value to the vertex list

    triangle = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))
    return triangle


class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()              # constructor for graphicsWindow class
        self.center1 = [self.width / 2, self.height / 2]    # initialize the centre of the triangle

    def update(self, dt):
        print "Updating the center of the triangle"
        self.center1 = [window.width / 2 + randint(-200, 200), window.height / 2 + randint(-200, 200)]

    def on_draw(self):
        # calculate the list of vertices required to draw the triangle
        vertexList = makeTriangle(20, self.center1[0], self.center1[1])

        # use pyGlet commands to draw lines between the vertices
        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)  # clear the graphics buffer
        glColor3f(1, 1, 0)                      # specify colors
        vertexList.draw(GL_LINE_LOOP)           # draw


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()   # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 2.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()            # run pyglet
