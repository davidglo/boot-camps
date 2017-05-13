# Simple Game Mechanics in Python

In this section, you will explore some simple game mechanics available in Python using [pyGlet](https://bitbucket.org/pyglet/pyglet/wiki/Home), which should be available in Anaconda.

pyGlet is a very basic 2d game engine, so you shouldn't worry about all of the details at this stage. Later on, there will be an opportunity to understand in more depth what the various bits are doing. For the moment, we are going to focus on some code (call it pyGlet-drawTriangle.py) which draws an equilateral triangle whose location is random. Note that the makeTriangle function works by builds an ordered list of (x,y) vertices, which pyGlet then "draws" by sequentially connecting lines between the vertices. The functions in the graphicsWindow class behave as follows:

* \__init__(self) is responsible for initializing the important data structures required during draws & updates

* update() is responsible for executing instructions required to update the positions of objects

* on_draw() is responsible for executing the drawing instructions
 
* when pyglet runs, it calls update() and then on_draw() at the frequency specified in pyglet.clock.schedule_interval()
 
```
import pyglet
from pyglet.gl import *
from math import *
from random import randint

# function to calculate vertices of an equilateral triangle
def makeTriangle(radius, xcenter, ycenter):
    vertices = []
    
    # specify the first vertex of the triangle
    angle = 0.0
    x = radius * cos(angle) + xcenter
    vertices.append(x)
    y = radius * sin(angle) + ycenter
    vertices.append(y)

    # specify the second vertex of the triangle
    angle = (2.0/3.0)*pi
    x = radius * cos(angle) + xcenter
    vertices.append(x)
    y = radius * sin(angle) + ycenter
    vertices.append(y)

    # specify the third vertex of the triangle
    angle = (4.0/3.0)*pi
    x = radius * cos(angle) + xcenter
    vertices.append(x)
    y = radius * sin(angle) + ycenter
    vertices.append(y)

    triangle = pyglet.graphics.vertex_list(3, ('v2f', vertices))
    return triangle

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()
        
        # initialize the centre of the triangle
        self.center1 = [self.width / 2, self.height / 2]

    def update(self, dt):
        print "Updating the center of the triangle"
        self.center1 = [window.width / 2 + randint(-200, 200), window.height / 2 + randint(-200, 200)]

    def on_draw(self):
        # calculate the list of vertices required to draw the triangle
        vertexList = makeTriangle(20, self.center1[0], self.center1[1])  # populate the drawList

        # use pyGlet commands to draw lines between the vertices
        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)  # clear the graphics buffer
        glColor3f(1, 1, 0)  # specify colors & draw
        vertexList.draw(GL_LINE_LOOP)

# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update,1/2.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet
```


#Tasks

There's a few things that you should try and do with this code:

* Get it running in PyCharm

* Figure out how to extend the code to draw more than three circles
* 
    here's a hint - think about populating drawList, and then looping over drawList, something like:
```
    for element in drawList:
        glColor3f(1,1,0)
        element.draw(GL_LINE_LOOP)
```
* Rather than randomly generated circles, experiment with different ways of making the circles move. For example, see if you can figure out how to write a function which will make the circles travel in:

    1. Straight lines
    
    2. A circular trajectory
    
    3. Harmonically, based on how far the circle is displaced from the center of the graphics window
    
*  Split out the makeCircle() function so that it lives in a new file called 'simpleShapes.py', and figure out how to construct a module so that can run pyGlet-draw.py by simply including a line which reads "import simpleShapes" 

* Change simpleShapes.py so that rather than calling the makeCircle() function, you have a circle class, which should include data (radius, center positions, and vertex lists), as well as functions (to update position). Now you should be able to modify pyGlet-draw.py to instantiate various circle objects (e.g. circle1 = circle(...)). The position of a circle (e.g., circle1) can then be updated using a command like "circle1.updatePosition()"
 
* If you're really motivated, try and write a new class that draws a new shape (e.g., triangle, square, octagon, ellipse, rectangle, etc.)

