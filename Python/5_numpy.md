
# NumPy

In the last session you saw how to use classes and objects to write software and associated tests that can be used safely and easily by other developers. It is good practice to write software that can be used easily by other people. The best way to learn how to do this is to read and try to use other people's software. You will learn to improve your code by working out what they did right, and also by getting annoyed by the things that they did wrong.

NumPy is a complete, object-orientated module for fast maths (numerics) in Python. All of the code needed to manipulate matrices and vectors, calculate random numbers and perform polynomial fitting is obviously very complex. This complexity is hidden behind a set of classes / objects that are provided by NumPy to provide a simple, easy-to-use interface for users such as us.

you can have a quick look at what's available in numpy via ipython. Let's load the NumPy module.

    $ ipython
    $ import numpy

The first thing to do when looking at some new code is to try to read the documentation...

    $ help(numpy)
    Help on package numpy:
    
    NAME
        numpy
    
    FILE
        /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/__init__.py
    
    DESCRIPTION
        NumPy
        =====

The NumPy documentation is very complete and useful. You will also see that it points you towards a reference guide that is held at [http://scipy.org](http://scipy.org).

NumPy is built from a series of submodules, that can be seen listed near the end of the help. Modules include fft (fast fourier transform), linalg (linear algebra), polynomial (polynomial fitting etc.) and math (access to standard math functions such as cosine, sine etc.).

You can get the help on the fft submodule using

    $ help(numpy.fft)

All of numpy's modules are loaded when you type 

    $ import numpy

So, for example, the "cos" function in the math module can be used via

    $ numpy.math.cos(0)
    1.0

However, you can also import a single module, e.g. to import just the math module, type

    $ from numpy import math

Now, the cos function can be used via

    $ math.cos(0)
    1.0

You can also rename modules when you load them. This can be used to create a quick shorthand, e.g. renaming numpy as "np"

    $ import numpy as np
    $ np.math.cos(0)
    1

or

    $ from numpy import math as nmath
    $ nmath.cos(0)
    1

## Exercise

### Exercise 5a

NumPy is famous for fast matrix algebra - e.g., matrix-matrix multiplications, diagonalizations, singular value decompositions, inversions, etc. Look at the ipython help for the NumPy matrix class;

    # help(numpy.matrix)

First, use the help to work out how to create the 2D identity matrix (1,0 ; 0,1)?
Next, use the same technique to create a matrix corresponding to the vector (1,1).

The benefit of the NumPy matrix class, is that multiplication of matrix objects will follow the rules of matrix maths. Verify this by multiplying your vector by the identity matrix. The resulting vector should be the same.

Now, create a 2D matrix with values (2,0 ; 0,2). This should scale your vector by two times. Verify that multiplying your vector by this matrix returns the vector (2,2).

Next, while you can multiply a vector by a matrix, you cannot multiply a matrix by a vector. Verify that a python exception will be raised when you multiply the identity matrix by the vector.

### Excerise 5b

Let's look at how to use numpy to carry out a simple and oft-used linear algebra routine - matrix-matrix multiplications in order to rotate objects. The aim is to incorporate this into our triangle drawing code so that we can rotate our triangles. There's further detail [available at wikipedia](https://en.wikipedia.org/wiki/Rotation_matrix)

Say we have a list of triangle vertices (self.vertices) which are oriented around a center point self.x and self.y. If self.vertices is ordered in a list as follows [x1, y1, x2, y2, x3, y3, ...], then the following function rotateVertices() translates this set of vertices to the origin, uses numpy's linear algebra routines to rotate it by some angle self.theta (where self.theta is in degrees), and then translates it back to where it was before we carried out the rotation operation.

    def rotateVertices(self):
        """function to translate a set of coordinates to the (0,0) origin & then rotate them by some angle theta"""
        
        # translate vertices to the origin
        c = numpy.array([[self.vertices[0] - self.x,self.vertices[1] - self.y],
                         [self.vertices[2] - self.x,self.vertices[3] - self.y],
                         [self.vertices[4] - self.x,self.vertices[5] - self.y]])

        theta = (self.theta / 180.) * numpy.pi       # calculate theta in radians & the corresponding rotation matrix
        rotMatrix = numpy.array([[numpy.cos(theta), -numpy.sin(theta)],    
                                 [numpy.sin(theta), numpy.cos(theta)]])

        c = numpy.matmul(c,rotMatrix)                # matrix-matrix multiplication with numpy

        self.vertices = [c[0][0] + self.x,c[0][1] + self.y,    # translate the rotated vertices back to the center
                         c[1][0] + self.x,c[1][1] + self.y,
                         c[2][0] + self.x,c[2][1] + self.y]

At the end of this code snippet, self.vertices now contains the vertices, all rotated by angle theta.

For this excercise, see if you can take the numpy code snippet above and use it to rotate your vertices as they are moving around. Some hints on modifications that you might find useful to get this working:
* change self.vertices to a data structure that lives on triangleClass, using a declaration like self.vertices = [0.0] * 6
* add two new data members to triangleClass, self.theta (which stores the value of theta), and self.thetaIncrement (which stores how much theta should be incremented on update)
* change calculateTriangleVertices() to a function which is called updateVertices(), whose sole role is to update self.vertices
* add a new function on triangleClass called getVertices(), whose sole job is to return a vertex list in pyglet format using the line vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', self.vertices)) 
* By extending the code snippet I've give you above, add a new function on triangleClass called rotateVertices(), which rotates self.vertices using some value of self.theta

Some further hints:

With these new changes to triangleClass, your calls from `__init__()` might look something like:

        for i in range(0,len(triangles)):
            triangles[i].setCentreCoordinates(self.width / 2, self.height / 2)
            triangles[i].updateVertices()
            triangles[i].setVelocity(i+1,i+2)
            triangles[i].setThetaIncrement(5*i)

and update() should might look something like this:

        for i in range(0,len(triangles)):
            triangles[i].updateCoordinates(self.width, self.height )
            triangles[i].updateVertices()
            triangles[i].updateTheta()
            triangles[i].rotateVertices()
            
and draw() shouldn't change that much, but it might now look something like this:

        for i in range(0,len(triangles)):
            vertexList = triangles[i].getVertices()         # calculate the list of vertices required to draw the triangle
            #  use pyGlet commands to draw lines between the vertices for the triangle
            lineColor = triangles[i].getColor()             # openGL color specification
            pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw

if you are totally stuck, there are example scripts here:
* [5b/drawTriangle.py](5b/2d-drawTriangle.py)
* [5b/triangleClass.py](5b/2d-triangleClass.py)

### if you are hungry for more

Read and work through [this official NumPy tutorial](http://wiki.scipy.org/Tentative_NumPy_Tutorial).


