import pyglet
import pyglet.gl
import math
from random import randint

color = {}                                  # declare a color dictionary
color['yellow']   = [1.0, 1.0, 0.0]         # fill each entry of the color dictionary with a list of three floats
color['blue']     = [0.0, 0.0, 1.0]
color['red']      = [1.0, 0.0, 0.0]
color['green']    = [0.0, 1.0, 0.0]
color['sienna']   = [0.627, 0.322, 0.176]
color['hotpink'] =  [1.0, 0.412, 0.706]

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()              # constructor for graphicsWindow class
        self.center1 = [self.width / 2, self.height / 2]    # initialize the centre of the triangle

    def update(self, dt):
        print "Updating the center of the triangle"
        self.center1 = [self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200)]

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT) 
        
        # now we will calculate the list of vertices required to draw the triangle
        numberOfVertices = 3        # specify the number of vertices we need for the shape
        radius = 20                 # specify the radius of each point from the center
        xcenter = self.center1[0]   # specify xcenter
        ycenter = self.center1[1]   # specify ycenter
        vertices = []  # initialize a list of vertices

        for i in range(0,numberOfVertices):
            angle = i*(2.0/3.0)*math.pi  # specify a vertex of the triangle (x,y values)
            x = radius * math.cos(angle) + xcenter
            y = radius * math.sin(angle) + ycenter
            vertices.append(x)  # append the x value to the vertex list
            vertices.append(y)  # append the y value to the vertex list

        # convert the vertices list to pyGlet vertices format
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))

        # now use pyGlet commands to draw lines between the vertices
        lineColor = 'hotpink'                   # choose color
        pyglet.gl.glColor3f(color[lineColor][0], color[lineColor][1], color[lineColor][2])  # openGL color specification
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)           # draw


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()   # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 2.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run() # run the inifinite pyglet loop
