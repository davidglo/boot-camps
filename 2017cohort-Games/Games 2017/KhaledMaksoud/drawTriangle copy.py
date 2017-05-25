""""""

import pyglet
import pyglet.gl
import math
import random
from random import randint
import colours
from triangleClass_v1 import triangleClass
from ImageClass import ImageClass
from pyglet.window import key, mouse

# initialize a list of triangles
triangles = []


#populate the list of triangles
for tri in range(0, 1900):
    triangles.append(triangleClass('shape', 'random', randint(0, 1000), randint(0, 700), 20, randint(1, 12), randint(-5, 5), randint(10, 20)))

print len(triangles)


# essex = ImageClass('essex.png','image', 20, 0, 50, 50)


xpositions = []
ypositions = []
xvelocities = []
yvelocities = []

for i in range(0, len(triangles)):
    xpos = triangles[i].getX()
    ypos = triangles[i].getY()
    xv = triangles[i].getXVelocity()
    yv = triangles[i].getYVelocity()
    xpositions.append(xpos)
    ypositions.append(ypos)
    xvelocities.append(xv)
    yvelocities.append(yv)



logan = ImageClass('logan.png', 'image', 1000/2, 700/4, 1, 1, 20, 20)
manby = ImageClass('manby.png', 'image', 3*1000/4, 3*700/4, -10, 50, 600, 600)



class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class

        self.width = 1000
        self.height = 700

        print colours.printAvailableColors()
        self.total_time = 0

    def update(self, dt):
        timesteps = 30000

        if self.total_time <= timesteps:
            print "--- Step ", self.total_time ," of ", timesteps, " ---"




            for i in range(0, len(triangles)):
                triangles[i].updateCoordinates(self.width, self.height)
                # triangles[i].harmonicmodel(xpositions[i], ypositions[i], 40)
                triangles[i].restraint(xpositions[i], ypositions[i])



            logan.updateCoordinates(self.width, self.height)
            # logan.harmonicmodel(self.width/2, self.height/4, 50)
            # logan.restraint(self.width/2, self.height/4)
            # logan.increaseSize(20, 20, self.width, self.height)
            logan.increaseSize(5, 5, 50, 600)

            manby.updateCoordinates(self.width, self.height)
            # manby.harmonicmodel(3*self.width/4, 3*self.height/4, 40)
            # manby.increaseSize(20, 20, 200, 200)
            manby.decreaseSize(20, 20, 5, 50)

            # essex.updateCoordinates(self.width, self.height)
            self.total_time = self.total_time + 1
        else:
            print "Steps complete!"
            pyglet.app.exit()


    def on_draw(self):

        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT) # clear the graphics buffer


        for i in range(0, len(triangles)):
            vertexList = triangles[i].calculateTriangleVertices()

            pyglet.gl.glColor3f(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))  # openGL color specification
            pyglet.gl.glLineWidth(1)
            vertexList.draw(pyglet.gl.GL_POLYGON)  # draw polygon shapes

            vertexList2 = triangles[i].drawrestraintbox(xpositions[i], ypositions[i])

            pyglet.gl.glColor3f(random.uniform(0,1), random.uniform(0,1),random.uniform(0,1))  # openGL color specification
            vertexList2.draw(pyglet.gl.GL_LINE_LOOP)  # draw restraint boxes for each polygon


        pyglet.gl.glColor3f(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
        logan.ImageDraw()

        vertexList2 = logan.drawrestraintbox(self.width / 2, self.width / 4)
        pyglet.gl.glColor3f(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))  # openGL color specification
        pyglet.gl.glLineWidth(20)
        vertexList2.draw(pyglet.gl.GL_LINE_LOOP)  # draw

        lineColor = 'green'
        pyglet.gl.glColor3f(colours.color[lineColor][0], colours.color[lineColor][1],colours.color[lineColor][2])  # openGL
        manby.ImageDraw()






# this is the main game engine loop
if __name__ == "__main__":
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 2000.0)

    # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet



# for i in range(0, len(triangles) - 1):   Non-functioning collision code - will fix then implement
            #      for j in range(1, len(triangles)):
            #
            #
            #
            #
            #         if (xpositions[i] + triangles[i].getRadius() == xpositions[j] + triangles[j].getRadius()):
            #             triangles[i].setXVelocity(-1)
            #             # triangles[i].setXCoordinate(xpositions[i])
            #             triangles[j].setXVelocity(-1)
            #             # triangles[j].setXCoordinate(xpositions[j] - triangles[j].getRadius())
            #             triangles[i].updateCoordinates(self.width, self.height)
            #             triangles[j].updateCoordinates(self.width, self.height)
            #
            #
            #
            #
            #
            #
            #
            #
            #         if (ypositions[i] + triangles[i].getRadius() == ypositions[j] + triangles[j].getRadius()):
            #             triangles[i].setYVelocity(-1)
            #             # triangles[i].setYCoordinate(ypositions[i])
            #             triangles[j].setYVelocity(-1)
            #             # triangles[j].setYCoordinate(ypositions[j] - triangles[j].getRadius())
            #             triangles[i].updateCoordinates(self.width, self.height)
            #             triangles[j].updateCoordinates(self.width, self.height)