import pyglet
import math
from random import randint

class shape_class:
    """Class for a regular polygon."""
    def __init__(self,ID,color,xcenter,ycenter,rad,nvertices):
        """ construct a basic triangle """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
        self.nvertices = nvertices

    def setCentreCoordinates(self,xcenter,ycenter):
        """ set the center coordinates of the triangle """
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

    def ranShift(self):
        """Give a random x,y shift to the polygon position, and a random shift to the radius"""
        self.x = self.x + randint(-1, 1)
        self.y = self.y + randint(-1, 1)
        self.radius = self.radius + randint(-2, 2)
        # self.center[i] = [self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200)]

    def calculateShapeVertices(self): #numberOfVertices, radius, xcenter, ycenter):
        """Calculate the polygon with (self.nvertices) vertices, and return list of vertices."""
        vertices = []  # initialize a list of vertices
        for i in range(0, self.nvertices):
            angle = i * (2.0 / self.nvertices) * math.pi  # specify a vertex of the triangle (x,y values)
            x = self.radius * math.cos(angle) + self.x
            y = self.radius * math.sin(angle) + self.y
            vertices.append(x)  # append the x value to the vertex list
            vertices.append(y)  # append the y value to the vertex list
        # convert the vertices list to pyGlet vertices format for the first triangle & return this list
        vertexList = pyglet.graphics.vertex_list(self.nvertices, ('v2f', vertices))
        return vertexList


class logan_class:
    """Class for the head that bounces off walls. Associated with a constant velocity except for inversion
    upon hitting walls"""
    def __init__(self,xcenter,ycenter,velocity,dt):
        self.x = xcenter
        self.y = ycenter
        self.velocity = velocity
        self.dt = dt
        self.lim = 200

    def updatePosition(self):
        """Update position based on velocity, and invert a component of velocity if past boundary."""
        self.x = self.x + self.velocity[0]*self.dt
        self.y = self.y + self.velocity[1]*self.dt
        if (self.x > 600) or (self.x < 0):
            self.velocity[0] = - self.velocity[0]
        if (self.y > 400) or (self.y < 0):
            self.velocity[1] = - self.velocity[1]

    def getX(self):
        """return x coordinate of head"""
        return self.x

    def getY(self):
        """return y coordinate of head"""
        return self.y