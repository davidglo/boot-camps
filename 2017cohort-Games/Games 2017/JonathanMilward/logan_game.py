import pyglet
from pyglet.gl import *
from pyglet.window import key
from math import *
from random import randint
import random
import math
import colors
from my_classes import shape_class, logan_class

people = ['logan.png','manby.png','essex.png']

class graphicsWindow(pyglet.window.Window):
    """Class of the game in a graphics window. Initialization of the game, using the my_classes.py
    classes (shape_class and logan_class) is done here, along with checking for user input and
    setting the output."""
    def __init__(self):
        super(graphicsWindow, self).__init__()              # constructor for graphicsWindow class
        # Initialize empty array for shape_class objects to be added
        self.nshapes = 0
        self.myshapes = []
        # Create a logan object with initial coordinates, velocity time-step
        self.mylogan = logan_class(100,100,[1,4],3)
        # Set initial image as logan face
        self.logan_image = pyglet.image.load(people[0])
        # Integer that tracks who the current face is set to zero for logan (logan,manby,essex)
        self.current_person = 0
        # Initial sprite, scale
        self.logan_sprite = pyglet.sprite.Sprite(self.logan_image, x=self.mylogan.getX(), y=self.mylogan.getY())
        # Various initial values, with logical variables that allow switching between different modes
        # on hitting buttons.
        self.logan_scale = 3.0
        self.logan_scale_bool = True
        self.logan_rotation = 0.0
        self.logan_rotation_bool = True
        self.rotate_bool = False
        self.rotspeed = 2.0
        self.nvertices = 3
        self.label = pyglet.text.Label('Numbers (3..9).  Space.  Enter.  "q" to clear.',
                                  font_name='Arial',
                                  font_size=12,
                                  x=157, y=470,
                                  anchor_x='center', anchor_y='center')

    def update(self, dt):
        # Give shapes a random shift
        for i in range(self.nshapes):
            self.myshapes[i].ranShift()
        # Update position of logan
        self.mylogan.updatePosition()
        # Set up logan sprite for output at appropriate position
        self.logan_sprite = pyglet.sprite.Sprite(self.logan_image, x=self.mylogan.getX(), y=self.mylogan.getY())
        # Set up point to rotate around, rotate, and scale
        self.logan_sprite.image.anchor_x = self.logan_sprite.image.width / 2
        self.logan_sprite.image.anchor_y = self.logan_sprite.image.height / 2
        self.logan_sprite.scale = self.logan_scale
        self.logan_sprite.rotation = self.logan_rotation

        # If become over some scale limit, start going smaller
        if self.logan_scale > 3.0:
            self.logan_scale_bool = True
        # If under some scale limit, start getting bigger, and create a shape at the point with some random properties
        if self.logan_scale < 0.0001:
            self.logan_scale_bool = False
            self.myshapes.append(shape_class(1,random.choice(colors.color.keys()),self.mylogan.getX(),self.mylogan.getY(),randint(10,30),self.nvertices))
            self.nshapes = self.nshapes + 1
        if self.logan_scale_bool:
            self.logan_scale = self.logan_scale - 0.1
        else:
            self.logan_scale = self.logan_scale + 0.1

        # Do equivalent for rotations, over or under some rotation limit
        # Here account for possibility of enter having been pressed,
        # in which case the rotation is not limited
        if self.rotate_bool == False:
            if self.logan_rotation > 30:
                self.logan_rotation_bool = False
            if self.logan_rotation < -30:
                self.logan_rotation_bool = True
        if self.logan_rotation_bool:
            self.logan_rotation = self.logan_rotation + self.rotspeed
        else:
            self.logan_rotation = self.logan_rotation - self.rotspeed

    def on_draw(self):

        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)  # clear the graphics buffer
        # now we will calculate the list of vertices required to draw the triangle

        for j in range(self.nshapes):
            # convert the vertices list to pyGlet vertices format
            vertexList = self.myshapes[j].calculateShapeVertices()
            glColor3f(colors.color[self.myshapes[j].getColor()][0], colors.color[self.myshapes[j].getColor()][1], colors.color[self.myshapes[j].getColor()][2])  # specify colors
            vertexList.draw(GL_TRIANGLE_FAN)#GL_LINE_LOOP)           # draw

        self.logan_sprite.draw()
        self.label.draw()

    def on_key_press(self,symbol,modifiers):
        # Upon pressing space, change the face image
        if (symbol == key.SPACE):
            self.current_person += 1
            if self.current_person > 2:
                self.current_person = 0
            self.logan_image = pyglet.image.load(people[self.current_person])
        # Upon pressing enter, go into fast rotation
        if (symbol == key.ENTER):
            if self.rotate_bool == False:
                self.rotspeed = 18.0
            else:
                self.rotspeed = 2.0
            self.rotate_bool = not self.rotate_bool
            self.logan_rotation = self.logan_rotation%360
        # If user enters a number from 3 to 9, the polygon produced will have that number of vertices
        if (symbol == key.Q):
            self.nshapes = 0
            self.myshapes = []
        if (symbol == key._3):
            self.nvertices = 3
        if (symbol == key._4):
            self.nvertices = 4
        if (symbol == key._5):
            self.nvertices = 5
        if (symbol == key._6):
            self.nvertices = 6
        if (symbol == key._7):
            self.nvertices = 7
        if (symbol == key._8):
            self.nvertices = 8
        if (symbol == key._9):
            self.nvertices = 9

# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()   # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1/100.)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run() # run the infinite pyglet loop