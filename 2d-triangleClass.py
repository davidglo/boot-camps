import pyglet
import math
import numpy

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
        self.vertices = [0.0] * 6
        self.thetaIncrement = 0
        self.theta = 0

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

    def getVertices(self):
        """convert the vertices list to pyGlet vertices format for the first triangle & return this list"""
        numberOfVertices = 3
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', self.vertices))
        return vertexList

    def updateVertices(self):
        """ function which calculates the vertex list required to draw an equilateral triangle """
        numberOfVertices = 3  # specify the number of vertices we need for the shape
        vertices = []  # initialize a list of vertices

        for i in range(0, numberOfVertices):
            angle = i * (2.0 / 3.0) * math.pi  # specify a vertex of the triangle (x,y values)
            x = self.radius * math.cos(angle) + self.x
            y = self.radius * math.sin(angle) + self.y
            self.vertices[2*i]   = x    # append the x value to the vertex list
            self.vertices[2*i+1] = y  # append the y value to the vertex list

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

    def rotateVertices(self):
        """function that translates a set of coordinates to some origin & then rotates them"""

        # translate vertices to the origin
        for i in range(0,len(self.vertices)/2):
            xidx = i*2
            yidx = i*2 + 1
            self.vertices[xidx] = self.vertices[xidx] - self.x
            self.vertices[yidx] = self.vertices[yidx] - self.y

        c = numpy.array([[self.vertices[0],self.vertices[1]],
                         [self.vertices[2],self.vertices[3]],
                         [self.vertices[4],self.vertices[5]]])

        theta = (self.theta / 180.) * numpy.pi
        rotMatrix = numpy.array([[numpy.cos(theta), -numpy.sin(theta)],
                                 [numpy.sin(theta), numpy.cos(theta)]])

        c = numpy.matmul(c,rotMatrix)
        rotatedVertices = [c[0][0],c[0][1],c[1][0],c[1][1],c[2][0],c[2][1]]

        for i in range(0,len(rotatedVertices)/2):
            xidx = i*2
            yidx = i*2 + 1
            self.vertices[xidx] = rotatedVertices[xidx] + self.x
            self.vertices[yidx] = rotatedVertices[yidx] + self.y

    def setThetaIncrement(self,value):
        self.thetaIncrement = value

    def updateTheta(self):
        self.theta = self.theta + self.thetaIncrement
