import pyglet
import math

class triangleClass:

    def __init__(self,ID,color,xcenter,ycenter,rad):
        """ construct a basic triangle """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad

    def setCentreCoordinates(self,xcenter,ycenter):
        """ set the center coordinates of the triangle """
        self.x = xcenter
        self.y = ycenter

    def getColor(self):
        return self.color

    def calculateTriangleVertices(self):
        """ function to calculate the vertex list required to draw an equilateral triangle """
        numberOfVertices = 3  # specify the number of vertices we need for the shape
        vertices = []  # initialize a list of vertices

        for i in range(0, numberOfVertices):
            angle = i * (2.0 / 3.0) * math.pi  # specify a vertex of the triangle (x,y values)
            x = self.radius * math.cos(angle) + self.x
            y = self.radius * math.sin(angle) + self.y
            vertices.append(x)  # append the x value to the vertex list
            vertices.append(y)  # append the y value to the vertex list

        # convert the vertices list to pyGlet vertices format for the first triangle & return this list
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))
        return vertexList
