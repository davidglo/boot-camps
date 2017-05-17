# Simple Game Mechanics in Python

In this section, you will explore some simple game mechanics available in Python using [pyGlet](https://bitbucket.org/pyglet/pyglet/wiki/Home), which should be available in Anaconda.

pyGlet is a very basic 2d game engine. At this stage, don't worry about all of the details of how it works. As we progress, you will have the opportunity to understand in depth what the various bits are doing. For the moment, we are going to focus on a simple bit of code (call it drawTriangle.py) which draws an equilaterial triangle whose center point is random. Note that the makeTriangle function works by building an ordered list of (x,y) vertices. pyGlet then "draws" by placing connecting lines between the vertices. 
 
pyGlet, like other game engines, runs as an infinite loop, until terminated by a user 
* On the first pass through the loop, pyGlet calls the \__init__(self) function followed by the on_draw() function
* On every other pass through the loop, pyGlet calls the update() function followed by the on_draw() function
* The frequency at which pyglet loops is specified in pyglet.clock.schedule_interval()

pyGlet's key functions behave as follows:
* \__init__(self) is responsible for initializing the important data structures required during subsequent draws & updates
* update() is responsible for executing instructions required to update the states of objects
* on_draw() is responsible for executing drawing instructions
 
```
import pyglet
import pyglet.gl
import math
from random import randint

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()              # constructor for graphicsWindow class
        self.center1 = [self.width / 2, self.height / 2]    # initialize the centre of the triangle

    def update(self, dt):
        print "Updating the center of the triangle"
        self.center1 = [self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200)]

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT) 
        
        # now we will calculate the list of vertices required to draw the triangle
        numberOfVertices = 3        # specify the number of vertices we need for the shape
        radius = 20                 # specify the radius of each point from the center
        xcenter = self.center1[0]   # specify xcenter
        ycenter = self.center1[1]   # specify ycenter
        vertices = []  # initialize a list of vertices

        angle = 0.0               # specify the first vertex of the triangle (x,y values)
        x = radius * math.cos(angle) + xcenter
        y = radius * math.sin(angle) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

        angle = (2.0 / 3.0) * math.pi  # specify the second vertex of the triangle (x,y values)
        x = radius * math.cos(angle) + xcenter
        y = radius * math.sin(angle) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

        angle = (4.0 / 3.0) * math.pi  # specify the third vertex of the triangle (x,y values)
        x = radius * math.cos(angle) + xcenter
        y = radius * math.sin(angle) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

        # convert the vertices list to pyGlet vertices format
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))

        # now use pyGlet commands to draw lines between the vertices
        pyglet.gl.glColor3f(1, 1, 0)                      # specify colors
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)           # draw

# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()   # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 2.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run() # run pyglet
```

Get this code running in PyCharm, and make sure it works. Then take some time to look at the code, set some breakpoints, and start to step through the code, in and out of functions, inspecting variables along the way. Use what we learned about debugging to carry out some detective work and get a feel for how the program execution works.  

See if you can start to make some guesses as to what the code is doing, in particular the code contained in: 
* \__init__(self) - for now, don't worry about the line super(graphicsWindow, self).\__init__()
* update() 
* on_draw()

In what follows, we will use this simple triangle drawing code to learn about different aspects of python.

