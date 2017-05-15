import pyglet
import pyglet.gl
import math
from random import randint
import colors
from triangleClass import triangleClass

# initialize the triangles that we will be drawing
triangle1 = triangleClass('triangle1', 'blue',    0, 0, 20)
triangle2 = triangleClass('triangle2', 'hotpink', 0, 0, 20)

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        triangle1.setCentreCoordinates(self.width / 2, self.height / 2)
        triangle2.setCentreCoordinates(self.width / 2, self.height / 2)
        colors.printAvailableColors()

    def update(self, dt):
        # print "Updating the center of the triangle"
        triangle1.setCentreCoordinates(self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200))
        triangle2.setCentreCoordinates(self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200))

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # now we will calculate the list of vertices required to draw the FIRST triangle
        vertexList = triangle1.calculateTriangleVertices()

        # now use pyGlet commands to draw lines between the vertices for the first triangle
        lineColor = triangle1.getColor()
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  # openGL color specification
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw

        # now we will calculate the list of vertices required to draw the SECOND triangle
        vertexList = triangle2.calculateTriangleVertices()

        # now use pyGlet commands to draw lines between the vertices for the second triangle
        lineColor = triangle2.getColor()
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  # openGL color specification
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 2.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run the infinite pyglet loop
    
