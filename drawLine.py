import pyglet
from pyglet.gl import *
from math import *
from random import randint

# function makeLine calculates the vertices of a line by stepping horizontally from midpoint xcenter, ycenter
def makeLine(distanceToCentre, xcenter, ycenter):
    numberOfVertices = 2                # specify the number of vertices we need for the shape
    vertices = []                       # initialize a list of vertices
    x = xcenter + distanceToCentre      # specify the first vertex of the line
    y = ycenter
    vertices.append(x)                  # append the x value to the vertex list
    vertices.append(y)                  # append the y value to the vertex list
    x = xcenter - distanceToCentre      # specify the second vertex of the line
    y = ycenter
    vertices.append(x)                  # append the x value to the vertex list
    vertices.append(y)                  # append the y value to the vertex list

    line = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))  # convert the vertex list to pyGlet vertex format
    return line

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()              # constructor for graphicsWindow class
        self.center1 = [self.width / 2, self.height / 2]    # initialize the centre of the line
        help(self.center1)

    def update(self, dt):
        print "Updating the center of the line"
        self.center1 = [window.width / 2 + randint(-200, 200), window.height / 2 + randint(-200, 200)]

    def on_draw(self):
        # calculate the list of vertices required to draw the line
        vertexList = makeLine(20, self.center1[0], self.center1[1])
        # use pyGlet commands to draw lines between the vertices
        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)  # clear the graphics buffer
        glColor3f(1, 1, 0)                      # specify colors
        vertexList.draw(GL_LINE_LOOP)           # draw

# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 2.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet
