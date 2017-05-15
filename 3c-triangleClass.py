import pyglet
import math


class triangleClass:
    def __init__(self, ID, color, xcenter, ycenter, rad):
        """ initialize a triangle """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
        self.xvelocity = 0
        self.yvelocity = 0

    def setCentreCoordinates(self, xcenter, ycenter):
        """ set the x,y coordinates of the triangle """
        self.x = xcenter
        self.y = ycenter

    def getColor(self):
        """ return the color of the triangle """
        return self.color

    def getRadius(self):
        """ return the radius of the triangle """
        return self.radius

    def getX(self):
        """ return the x coordinate of the triangle """
        return self.x

    def getY(self):
        """ return the y coordinate of the triangle """
        return self.y

    def calculateTriangleVertices(self):
        """ function which calculates the vertex list required to draw an equilateral triangle """
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

    def setVelocity(self,xvel,yvel):
        """set the x & y velocity components"""
        self.xvelocity = xvel
        self.yvelocity = yvel

    def updateCoordinates(self,windowWidth,windowHeight):

        if ((self.x + self.xvelocity > windowWidth) or (self.x + self.xvelocity < 0)):
            self.xvelocity = -1*self.xvelocity

        if ((self.y + self.yvelocity > windowHeight) or (self.y + self.yvelocity < 0)):
            self.yvelocity = -1*self.yvelocity

        self.x = self.x + self.xvelocity
        self.y = self.y + self.yvelocity
