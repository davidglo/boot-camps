import math
import pyglet
import pyglet.gl
import random
from random import randint

class triangleClass:

    def __init__(self,ID,color,xcenter,ycenter,rad,corners, xvelocity, yvelocity):
        """ initialize a shape """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
        self.corners = corners
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity



    def setCentreCoordinates(self,xcenter,ycenter):
        """ set the x,y coordinates of the shape """
        self.x = xcenter
        self.y = ycenter

    def setXCoordinate(self,xcenter):
        """ set the x coordinate of the shape """
        self.x = xcenter

    def setYCoordinate(self,ycenter):
        """ set the y coordinate of the shape """
        self.y = ycenter


    def getColor(self):
        """ return the color of the shape """
        return self.color

    def getRadius(self):
        """ return the radius of the shape """
        return self.radius

    def increaseRadius(self, increment, limit):

        if (self.radius + increment > limit):
            self.radius = self.radius - increment

        self.radius = self.radius + increment


    def getX(self):
        """ return the x coordinate of the shape """
        return self.x

    def getY(self):
        """ return the y coordinate of the shape """
        return self.y

    def getcorners(self):
        """ return the number of verticies in the shape """
        return self.corners

    def setXVelocity(self, xvel):
        """ set the X velocity of the shape """
        self.xvelocity = xvel

    def setYVelocity(self, yvel):
        """ set the Y velocity of the shape """
        self.yvelocity = yvel


    def getXVelocity(self):
        """ return the x velocity of the shape """
        return self.xvelocity

    def getYVelocity(self):
        """ return the y velocity of the shape """
        return self.yvelocity

    def updateCoordinates(self, windowWidth, windowHeight):
        """ Updating the position of the shape based upon its velocity"""
        if ((self.x + self.xvelocity > windowWidth) or (self.x + self.xvelocity < 0)):
            self.xvelocity = -1*self.xvelocity  #On collision with window edges, the velocity changes sign


        if ((self.y + self.yvelocity > windowHeight) or (self.y + self.yvelocity < 0)):
            self.yvelocity = -1*self.yvelocity
            #self.y = -(windowHeight+10)

        self.x = self.x + self.xvelocity
        self.y = self.y + self.yvelocity


    def harmonicmodel(self, windowWidth, windowHeight, limit):
        """Model for simple harmonic motion of the shape in the 2d space"""
        if ((self.x + self.xvelocity > windowWidth + limit) or (self.x + self.xvelocity < windowWidth - limit)):
            self.xvelocity = -1*self.xvelocity  #On collision with window edges, the velocity changes sign


        if ((self.y + self.yvelocity > windowHeight + limit) or (self.y + self.yvelocity < windowHeight - limit)):
            self.yvelocity = -1*self.yvelocity
            #self.y = -(windowHeight+10)

        if ((self.x + self.xvelocity > windowWidth) or (self.x + self.xvelocity < 0)):
            self.xvelocity = -1*self.xvelocity  #On collision with window edges, the velocity changes sign


        if ((self.y + self.yvelocity > windowHeight) or (self.y + self.yvelocity < 0)):
            self.yvelocity = -1*self.yvelocity
            #self.y = -(windowHeight+10)

        self.x = self.x + self.xvelocity
        self.y = self.y + self.yvelocity

    def restraint(self, windowWidth, windowHeight):
        """Adding an artificial restraint upon the shape - can be toggled"""
        if ((self.x + self.xvelocity >= 1.2*windowWidth) or (self.x + self.xvelocity <= 0.6*windowWidth)):
            self.xvelocity = -1*self.xvelocity  #On collision with window edges, the velocity changes sign

        if ((self.y + self.yvelocity >= 1.2*windowHeight) or (self.y + self.yvelocity <= 0.6*windowWidth)):
            self.yvelocity = -1*self.yvelocity
            #self.y = -(windowHeight+10)

    def drawrestraintbox(self, windowWidth, windowHeight):
        numberOfVertices = 4
        vertices2 = []

        x1 = 0.6*windowWidth + self.radius + self.xvelocity*random.uniform(0, 1)
        y1 = 0.6*windowHeight + self.radius + self.yvelocity*random.uniform(0,1)
        x2 = 1.2*windowWidth + self.radius + self.xvelocity*random.uniform(0,1)
        y2 = 0.6*windowHeight + self.radius + self.yvelocity*random.uniform(0,1)
        x3 = 1.2*windowWidth + self.radius + self.xvelocity*random.uniform(0,1)
        y3 = 1.2*windowHeight + self.radius + self.yvelocity*random.uniform(0,1)
        x4 = 0.6*windowWidth + self.radius + self.xvelocity*random.uniform(0,1)
        y4 = 1.2*windowHeight + self.radius  + self.yvelocity*random.uniform(0,1)

        vertices2.append(x1)
        vertices2.append(y1)
        vertices2.append(x2)
        vertices2.append(y2)
        vertices2.append(x3)
        vertices2.append(y3)
        vertices2.append(x4)
        vertices2.append(y4)


        vertexList2 = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices2))
        return vertexList2


    def recogrestraint(self, windowWidth, windowHeight):
        """Adding an artificial restraint upon the shape - can be toggled"""
        if ((self.x + self.xvelocity >= 0.45*windowWidth/2) and (self.x + self.xvelocity <= 1.2*windowWidth/2)):
            self.xvelocity = -1*self.xvelocity  #On collision with window edges, the velocity changes sign

        if ((self.y + self.yvelocity >= 0.6*windowHeight/2) and (self.y + self.yvelocity <= 1.2*windowWidth/2)):
            self.yvelocity = -1*self.yvelocity
            #self.y = -(windowHeight+10)



    def calculateTriangleVertices(self):
        """ Calculating and converting the verticies of the triangles to a vertex list for drawing in pyGlet """
        numberOfVertices = self.corners
        vertices = []  # initialize a list of vertices

        for i in range(0, numberOfVertices):
            angle = i * (2.0 / numberOfVertices) * math.pi  # specify a vertex of the triangle (x,y values)
            x = self.radius * math.cos(angle) + self.x
            y = self.radius * math.sin(angle) + self.y
            vertices.append(x)  # append the x value to the vertex list
            vertices.append(y)  # append the y value to the vertex list

        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))
        return vertexList