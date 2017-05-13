# Simple Game Mechanics in Python

In this section, you will explore some simple game mechanics available in Python using [pyGlet](https://bitbucket.org/pyglet/pyglet/wiki/Home), which should be available in Anaconda.

pyGlet is a very basic 2d game engine. At this stage, don't worry about all of the details of how it works. As we progress, you will have the opportunity to understand in depth what the various bits are doing. For the moment, we are going to focus on a simple bit of code (call it pyGlet-drawLine.py) which draws a horizontal line whose location is random. Note that the makeLine function works by building an ordered list of (x,y) vertices. pyGlet then "draws" by placing a connecting line between the vertices. 
 
pyGlet, like other game engines, runs as an infinite loop, until terminated by a user 
* On the first pass through the loop, pyGlet calls the \__init__(self) function and then the on_draw() function
* On every other pass through the loop, pyGlet calls the update() function and then on_draw() function
* The frequency at which pyglet loops is specified in pyglet.clock.schedule_interval()

pyGlet's key functions behave as follows:
* \__init__(self) is responsible for initializing the important data structures required during draws & updates
* update() is responsible for executing instructions required to update the positions of objects
* on_draw() is responsible for executing the drawing instructions
 
```
import pyglet
from pyglet.gl import *
from math import *
from random import randint

# function makeLine calculates the vertices of a line from some midpoint xcenter, ycenter
def makeLine(numberOfVertices, distanceToCentre, xcenter, ycenter):
    vertices = []                       # initialize a list of vertices
    x = xcenter + distanceToCentre      # specify the first vertex of the line
    y = ycenter
    vertices.append(x)                  # append the x value to the vertex list
    vertices.append(y)                  # append the y value to the vertex list
    x = xcenter - distanceToCentre      # specify the second vertex of the line
    y = ycenter
    vertices.append(x)                  # append the x value to the vertex list
    vertices.append(y)                  # append the y value to the vertex list

    line = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))  # convert the vertex list to pyGlet vertex format
    return line

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()              # constructor for graphicsWindow class
        self.center1 = [self.width / 2, self.height / 2]    # initialize the centre of the line

    def update(self, dt):
        print "Updating the center of the line"
        self.center1 = [window.width / 2 + randint(-200, 200), window.height / 2 + randint(-200, 200)]

    def on_draw(self):
        # calculate the list of vertices required to draw the line
        vertexList = makeLine(2, 20, self.center1[0], self.center1[1])
        # use pyGlet commands to draw lines between the vertices
        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)  # clear the graphics buffer
        glColor3f(1, 1, 0)                      # specify colors
        vertexList.draw(GL_LINE_LOOP)           # draw

# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 2.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet
```

Get this code running in PyCharm, and make sure it works. Then take some time to look at the code, set some breakpoints, and start to step through the code, in and out of functions, inspecting variables along the way. Use what we learned about debugging to carry out some detective work and get a feel for how the program execution works.  

See if you can start to make some guesses as to what the code is doing, in particular the code contained in: 
* \__init__(self) (for now, don't worry about the line super(graphicsWindow, self).\__init__())
* update() 
* on_draw()
* makeLine()

In what follows, we will use this simple line drawing code to learn about different aspects of python.

