
# Good Programming Practice - Functions and Modules

## Functions

In the [last session](1_lists_and_dictionaries.md), you wrote code to draw two triangles. The code hopefully works, but it's gotten considerably larger and harder to read. You can see that the complexity and readability of the code will suffer if we try to draw more shapes - we'll have to keep copying and pasting code every time we want to draw a new shape.

Functions provide a way of packaging code into reusable, easy-to-read, and easy-to-use components. Lets imagine I have some code to add together two arrays

    $ a = [1, 2, 3, 4]
    $ b = [5, 6, 7, 8]
    $ c = []
    $ for i in range(0,len(a)):
    $     c.append( a[i] + b[i] )
    $
    $ c
    [6, 8, 10, 12]

I can turn this into a function by using "def"

    $ def addArrays(x, y):
    $     z = []
    $     for i in range(0,len(x)):
    $         z.append(x[i] + y[i])
    $     return z

I can add the arrays by calling the function

    $ c = addArrays(a,b)
    $ c
    [6, 8, 10, 12]

In this case I have called the function "addArrays" and passed in the arguments "a" and "b". "a" is copied to "x", while "b" is copied to "y". The function addArrays then acts on "x" and "y", creating the summed array "z". It then returns the new array "z", which is copied back to "c".

Here is another example

    $ r = [ 0.1, 0.2, 0.3 ]
    $ s = [ 5, 12, 8 ]
    $ t = addArrays(r, s)
    $ t
    [5.1, 12.2, 8.3]

Note that we can pass the values to the function directly, e.g.

    $ r = addArrays( [ 1, 2, 3], [5, 6, 7] )
    $ r
    [6, 8, 10]

Note that you must pass in the right number of arguments to a function. addArrays expects two arguments, so if you pass more or less, then that is an error.

    $ r = addArrays()
    TypeError: addArrays() takes exactly 2 arguments (0 given)
    $ r = addArrays(a, b, c)
    TypeError: addArrays() takes exactly 2 arguments (3 given)

Note also that you can define your function to take as many arguments, and return as many values as you want, e.g.

    $ def lotsOfArgs(a, b, c, d, e):
    $     return (a+b, c+d, e)
    $
    $ (r, s, t) = lotsOfArgs(1, 2, 3, 4, 5)
    $ r
    3
    $ s
    7
    $ t
    5

### Exercise 2a

The file [1c/drawTwoTriangles.py](1c/drawTwoTriangles.py) can be made considerably more readable and compact by utilizing functions. Let's look specifically at the code invoked to draw the two triangles 

        # now we will calculate the list of vertices required to draw the FIRST triangle
        numberOfVertices = 3        # specify the number of vertices we need for the shape
        radius = 20                 # specify the radius of each point from the center
        xcenter = self.center1[0]   # specify xcenter
        ycenter = self.center1[1]   # specify ycenter
        vertices = []  # initialize a list of vertices

        for i in range(0,numberOfVertices):
            angle = i*(2.0/3.0)*math.pi  # specify a vertex of the triangle (x,y values)
            x = radius * math.cos(angle) + xcenter
            y = radius * math.sin(angle) + ycenter
            vertices.append(x)  # append the x value to the vertex list
            vertices.append(y)  # append the y value to the vertex list

        # convert the vertices list to pyGlet vertices format for the first triangle
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))

        # now use pyGlet commands to draw lines between the vertices for the first triangle
        lineColor = 'hotpink'                   # choose color
        pyglet.gl.glColor3f(color[lineColor][0], color[lineColor][1], color[lineColor][2])  # openGL color specification
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)           # draw

        # now we will calculate the list of vertices required to draw the SECOND triangle
        numberOfVertices = 3        # specify the number of vertices we need for the shape
        radius = 20                 # specify the radius of each point from the center
        xcenter = self.center2[0]   # specify xcenter
        ycenter = self.center2[1]   # specify ycenter
        vertices = []  # initialize a list of vertices

        for i in range(0,numberOfVertices):
            angle = i*(2.0/3.0)*math.pi  # specify a vertex of the triangle (x,y values)
            x = radius * math.cos(angle) + xcenter
            y = radius * math.sin(angle) + ycenter
            vertices.append(x)  # append the x value to the vertex list
            vertices.append(y)  # append the y value to the vertex list

        # convert the vertices list to pyGlet vertices format for the second triangle
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))

        # now use pyGlet commands to draw lines between the vertices for the second triangle
        lineColor = 'blue'                   # choose color
        pyglet.gl.glColor3f(color[lineColor][0], color[lineColor][1], color[lineColor][2])  # openGL color specification
        vertexList.draw(pyglet.gl.GL_LINE_LOOP) # draw

Using what you've learned about functions, make a function calculateTriangleVertices() which will eliminate the redundant code in what's written above. calculateTriangleVertices() should take as input the radius, and the x,y coordinates of the center. It should return a vertexList in pyGlet format. 

If you are really stuck, there is an example completed script in [2a/drawTwoTriangles-refactor1.py](2a/drawTwoTriangles-refactor1.py)

## Modules

Functions are great for organising your software into self-contained, reusable blocks of code. However, as it stands, you'd have to copy and paste your function into every script or program in which it is used. Modules (also called libraries) provide a way of packaging up useful commmands and functions into a single, reusable package. In python, creating a module is very easy, and the ready availability of modules for just about anything you might want to do in fact account for why python is such a powerful coding framework. Indeed, the python scripts that you have been playing with already make extensive use of python modules. For example, let's have a look at how we have been carrying out mathematical operations - e.g., cosine, sine, and also getting the value of pi. Note that we have a line which reads

    import math

The "import" command loads a separate python script, which is located in a file called 'math.py', importing all functions, and then running any code that does not live inside a function call. You can see this easily using the power of PyCharm: highlight "math.pi" in your editor, right-click your mouse, and then click on "Go To" -> "Declaration".

This will take you to the file where "pi" is declared. Note that it lives in a file called "math.py", where we find a few lines, which read

    # Variables with simple values
    e = 2.718281828459045

    pi = 3.141592653589793

The ability to import modules that we can have access to consistent values of pi and e (or cosine, sine, etc.) at any point in any python code project that we are working on. Assuming that we've included within our code the "import math" line, then we can easily access the value of pi, or the value of e, simply by utilizing ".", the so-called "dot-operator" as follows:

    math.pi
    math.e

The availabilty of math.pi and math.e means that (if we wanted to) we could have our own local variables called "pi" or "e", and these  would not be confused with math.pi or math.e. Note that modules can include both data AND functions. Sine & Cosine are good examples of functions that are included within the math module. To access consistent definition of these functions is easy, so long as we have imported the math module

    math.cos(angle)
    math.sin(angle)
        
If you look at little bit more carefully at the code, you will see that we have utilized a few other modules - for example

    import pyglet
    import pyglet.gl

let us access functions (e.g., pyglet.gl.glClear) and data members (e.g., pyglet.gl.GL_LINE_LOOP) required to carry out simple drawings. The ability to access data and functions within these modules has saved us massive quantities of work. Note that pyglet's convention is that module data is always named using upper case letters (e.g., the GL_LINE_LOOP data member), while module functions are always named using lower case letters (e.g., the glClear() function).

So by encapsulating data and functions in modules, we can make code our more general, and more readable, and more sustainable.

## Exercise 2b

The code that we wrote to make colors in [drawTwoTriangles-refactor1.py](https://github.com/davidglo/boot-camps/blob/2017-TMCS-software/drawTwoTriangles-refactor1.py), something like

    color = {}  # declare a color dictionary
    color['yellow'] = [1.0, 1.0, 0.0]  # fill each entry of the color dictionary with a list of three floats
    color['blue'] = [0.0, 0.0, 1.0]
    color['red'] = [1.0, 0.0, 0.0]
    color['green'] = [0.0, 1.0, 0.0]
    color['sienna'] = [0.627, 0.322, 0.176]
    color['hotpink'] = [1.0, 0.412, 0.706]

was pretty useful, but it could quite quickly become massive if we wanted to add lots of colors to the dictionary. In addition, it's easy to imagine that the color dictionary could be useful to other bits of code that we (or others) might write in the future. So we're going to focus on turning this bit of color code into a python module.

To do this we are going to execute the following steps:
* create a new file within your PyCharm proeject called "colors.py"
* move the code for generating a color dictionary into colors.py
* change your code to utilize the colors.py module (hint: you will have to add an "import" and then use the dot operator to access data on colors.py
* let's also add an additional function to colors.py, which is called printAvailableColors(), and which prints out all of the colors which we have defined
* add a call within \__init()__ to printAvailableColors(), so that we get a list of available colors at initialization time

If you are really stuck, then the completed scripts are available as 
* [2b/drawTwoTriangles-refactor2.py](2b/drawTwoTriangles-refactor2.py) 
* [2b/colors.py](2b/colors.py)

One final point: it's often the case that the code within a module definition is something which can function on its own as standalone python program; however, it might also include lots of useful stuff that we might want to reuse elsewhere. For example, consider a slightly modified version of our color.py module:

    color = {}  # declare a color dictionary
    color['yellow'] = [1.0, 1.0, 0.0]  # fill each entry of the color dictionary with a list of three floats
    color['blue'] = [0.0, 0.0, 1.0]
    color['red'] = [1.0, 0.0, 0.0]
    color['green'] = [0.0, 1.0, 0.0]
    color['sienna'] = [0.627, 0.322, 0.176]
    color['hotpink'] = [1.0, 0.412, 0.706]

    def printAvailableColors():
        print '\tyellow'
        print '\tblue'
        print '\tred'
        print '\tgreen'
        print '\tsienna'
        print '\thotpink'

    print 'executing colors.py as the main routine'
    print 'we have definitions of:'
    printAvailableColors()

Say that (for some reason - maybe we are teaching a software course), we want the code in color.py to run as a standalone package. When the code runs, we want to print the information indicated in the final three lines. It's easy enough to run this as a standalone application in PyCharm. Right-click "colors.py" in the PyCharm explorer, and then click 'Run colors'. You should see console output which reads

    executing colors.py as the main routine
    we have definitions of:
        yellow
        blue
        red
        green
        sienna
        hotpink

This might be useful in some contexts, but it also might be annoying to have it run every time colors.py is imported. For example, when we run our triangle drawing code, we will get this print-out every time, which we may not want. To avoid this, we can use a python "hidden variable". Hidden variables begin with one or two underscores. We're not going to go into detail on hidden variables here; for the moment, suffice it to say that there is a hidden variable called name called "__name__". If the function that we are in is a top level function, then its "__name__" is "__main__". To specify that certain code within our colors.py module should only run when we are running colors.py as the top level code (i.e., not importing it into something else), then we simply need to enclose the relevant bits of colors.py as follows:
    
    if __name__ == "__main__":
        # only run this code if colors.py is run as the top-level function
        # ignore if colors.py is imported as a module 
        print 'executing colors.py as the main routine'
        print 'we have definitions of:'
        printAvailableColors()

Now if I run "colors.py" in PyCharm, I get the information printed.

If instead I run my triangle drawing code in PyCharm, which imports colors.py as a module, the information is not printed. Have a go at including this code in your project, and verify for yourself that this is indeed the case.

It is extremely good programming practice to write all of your scripts as if they were modules (and indeed to write all of your code as if they were part of a reusable library). This makes it really easy for you to pick up and reuse all of your code, preventing you from having to continually rewrite the same functionality over and over again.



# [Previous](1_lists_and_dictionaries.md) [Next](3_documenting_code.md) 
