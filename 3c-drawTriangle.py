import pyglet
import pyglet.gl
import math
from random import randint
import colors
from triangleClass import triangleClass

# initialize a list of triangles
triangles = []

# populate the list of triangles
triangles.append(triangleClass('triangle1', 'blue',    0, 0, 20))
triangles.append(triangleClass('triangle2', 'hotpink', 0, 0, 20))
triangles.append(triangleClass('triangle3', 'yellow',  0, 0, 20))
triangles.append(triangleClass('triangle4', 'red',     0, 0, 20))
triangles.append(triangleClass('triangle5', 'green',   0, 0, 20))

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class

        for i in range(0,len(triangles)):
            triangles[i].setCentreCoordinates(self.width / 2, self.height / 2)

        for i in range(0,len(triangles)):
            triangles[i].setVelocity(5+i,10+i)

    def update(self, dt):
        # print "Updating the center of the triangle"
        for i in range(0,len(triangles)):
            triangles[i].updateCoordinates(self.width, self.height )

    def on_draw(self):
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)    # clear the graphics buffer

        for i in range(0,len(triangles)):
            # calculate the list of vertices required to draw the triangle
            vertexList = triangles[i].calculateTriangleVertices()
            #  use pyGlet commands to draw lines between the vertices for the triangle
            lineColor = triangles[i].getColor()             # openGL color specification
            pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw

# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 30.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run the infinite pyglet loop
