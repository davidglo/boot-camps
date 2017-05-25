import math
import pyglet
import pyglet.gl
import random
from random import randint

class ImageClass:

    def __init__(self,ID,name,xcenter,ycenter,xvel, yvel, imagewidth, imageheight):
        """ initialize a shape """
        self.ID = ID
        self.name = name
        self.x = xcenter
        self.y = ycenter
        self.xvelocity = xvel
        self.yvelocity = yvel

        self.name = pyglet.resource.image(self.ID)
        self.name.width = imagewidth
        self.name.height = imageheight






    def setCentreCoordinates(self,xcenter,ycenter):
        """ set the x,y coordinates of the shape """
        self.x = xcenter
        self.y = ycenter

    def getX(self):
        """ return the x coordinate of the shape """
        return self.x

    def getY(self):
        """ return the y coordinate of the shape """
        return self.y

    def increaseSize(self, xincrement, yincrement, xupperlimit, yupperlimit):
        """Incrementally increases and decreases the size of image"""



        if (self.name.width + xincrement > xupperlimit):
            self.name.width = self.name.width - xincrement

        if (self.name.height + yincrement > yupperlimit):
            self.name.height = self.name.height - yincrement


        self.name.width = self.name.width + xincrement
        self.name.height = self.name.height + yincrement

    def decreaseSize(self, xincrement, yincrement, xlowerlimit, ylowerlimit):
        """Incrementally increases and decreases the size of image"""

        if (self.name.width - xincrement < xlowerlimit):
            xincrement = -1*xincrement

        if (self.name.height - yincrement < ylowerlimit):
            yincrement = -1*yincrement


        self.name.width = self.name.width - xincrement
        self.name.height = self.name.height - yincrement




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
        if ((self.x + self.xvelocity > windowWidth + limit) or (self.x + self.xvelocity < windowWidth- limit)):
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

        x1 = 0.6*windowWidth + self.xvelocity*random.uniform(0,10)
        y1 = 0.6*windowHeight + self.yvelocity*random.uniform(0,10)
        x2 = 1.2*windowWidth + self.xvelocity*random.uniform(0,10)
        y2 = 0.6*windowHeight + self.yvelocity*random.uniform(0,10)
        x3 = 1.2*windowWidth + self.xvelocity*random.uniform(0,10)
        y3 = 1.2*windowHeight + self.yvelocity*random.uniform(0,10)
        x4 = 0.6*windowWidth + self.xvelocity*random.uniform(0,10)
        y4 = 1.2*windowHeight + self.yvelocity*random.uniform(0,10)

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



    def ImageDraw(self):
        """ Calculating and converting the verticies of the triangles to a vertex list for drawing in pyGlet """
        self.name.blit(self.x, self.y)