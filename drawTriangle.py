import pyglet
from pyglet.gl import *
import math
from random import randint


class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()              # constructor for graphicsWindow class
        self.center1 = [self.width / 2, self.height / 2]    # initialize the centre of the triangle

    def update(self, dt):
        print "Updating the center of the triangle"
        self.center1 = [window.width / 2 + randint(-200, 200), window.height / 2 + randint(-200, 200)]

    def on_draw(self):
        # clear the graphics buffer
        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT) 
        
        # now we will calculate the list of vertices required to draw the triangle
        numberOfVertices = 3        # specify the number of vertices we need for the shape
        radius = 20                 # specify the radius of each point from the center
        xcenter = self.center1[0]   # specify xcenter
        ycenter = self.center1[1]   # specify ycenter
        vertices = []  # initialize a list of vertices

        angle = 0.0               # specify the first vertex of the triangle (x,y values)
        x = radius * math.cos(angle) + xcenter
        y = radius * math.sin(angle) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

        angle = (2.0 / 3.0) * math.pi  # specify the second vertex of the triangle (x,y values)
        x = radius * math.cos(angle) + xcenter
        y = radius * math.sin(angle) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

        angle = (4.0 / 3.0) * math.pi  # specify the third vertex of the triangle (x,y values)
        x = radius * math.cos(angle) + xcenter
        y = radius * math.sin(angle) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

        # convert the vertices list to pyGlet vertices format
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))

        # now use pyGlet commands to draw lines between the vertices
        glColor3f(1, 1, 0)                      # specify colors
        vertexList.draw(GL_LINE_LOOP)           # draw


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()   # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 2.0)  # tell pyglet the on_draw() & update() timestep
pyglet.app.run() # run pyglet
