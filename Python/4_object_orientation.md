
# Object Orientation

You have now learned how to package up your code into re-usable, documented functions, and how to then package up those functions into re-usable, documented modules (libraries). It is great to package up your code so that it is easy for other people to understand and re-use. However, there often cases where we want to go beyond the modularity provided even by module structures. there's lots of reasons for this. 

One reason is that modules don't protect their data very well -i.e., other people (like yourself several months after you've written a module) have a habit of re-using your code in the wrong, or in unexpected ways...

As an example, lets imagine someone using code in the [colors.py](https://github.com/davidglo/boot-camps/blob/2017-TMCS-software/colors.py) module. It would be really easy for somebody to write something like the following from somewhere in the pyglet routines:

    colors.color['blue']=[0.5,0.5,0.5]

This will turn into grey an entry which we had intended to be 'blue'. Or they could do something like 

    colors.color['blue']=[1.0, 0.0, 0.0]

where now they've assigned the tag 'blue' to a color that is actually red! The problem in both of these examples is that the "colors" dictionary is visible, and anybody can change its value whenever they want. This might seem like a good thing, but in complex code projects, this is the sort of thing that can lead to hard-to-find and extremely subtle bugs that can drive you mad.
 
Another problem with modules and functions is that they sometimes don't reflect the structure of our code very well. For example, in our [drawTwoTriangles-refactor2.py](https://github.com/davidglo/boot-camps/blob/2017-TMCS-software/drawTwoTriangles-refactor2.py) code, there's a sense in which the triangles don't really "exist" as enduring data structures. At each pyglet update, we simply call the function to generate some random coordinates, and then formulate a vertex list which is then drawn. In fact, each of our trianges are characterized by some properties. For example, any given object which has the properties of an equilateral triangle should be minimally characterized by:
* a color
* an id (e.g., the 'first' or 'second' triangle; we could give them more exotic names if we wanted - maybe "hydrogenAtom" & "heliumAtom")
* an x & y position
* a radius (i.e., the distance from each corner to the center)
* in the future, you could imagine a scenario whereby we want each triangle to also have an x,y velocity

What we've just done is specify the data that should define any object which belongs to class "triangle". In addition to data, there's at least one function that we would want our triangle class to include: 
* a function which (on demand) can turn x,y position and radius data into a list of vertices

## Object oriented programming

Object orientated programming solves both of the problems specified above by packaging functions and their associated data together into a Class. A Class defines two things:
* data
* functions to manipulate that data 

An "object" is a particular instantiation of a "class" definition. Sticking with our triangle example - we can potentially have many objects (i.e., triangles, each with their own position, size, color, and ID), but we will only have one class. If you know anything about Platonic philosophy, object oriented code resembles very much Plato's [theory of forms](https://en.wikipedia.org/wiki/Theory_of_Forms), where everything that we experience phenomenologically is in fact the imperfect manifestation of some idealized "perfect" form. Plato famously applied his theory of forms to tables. Wikipedia explains the [Platonic theory of forms as follows](https://en.wikipedia.org/wiki/Theory_of_Forms): "For example, there are countless tables in the world but the Form of tableness is at the core; it is the essence of all of them". Substitute "triangles" for "tables" in the above example, and "class" for "Form" - and you are getting to the heart of object oriented programming: Countless triangle objects, but one triangle class, which is the essence of all of them.

Ok, enough philosophy for now. The idea of putting together member data and member functions which are important for certain classes of objects is called "Encapsulation". It's a key idea of object orientated programming, and refers to the practice of hiding the data in a Class, with the net result that only the functions which are defined as part of the Class can read or write (change) the data. Not only can this actually result in simpler to use and easier-to-read code which maps onto the problem we're actually trying to solve, but it also enforces practices that are much less likely to get abused by others (or ourselves in the future) when we're coding.

For example, take a look the code [triangleClass-v1.py](https://github.com/davidglo/boot-camps/blob/2017-TMCS-software/triangleClass-v1.py) required to make a very basic "triangle" class:

    class triangleClass:

        def __init__(self,ID,color,xcenter,ycenter,rad):
            """ initialize a triangle """
            self.ID = ID
            self.color = color
            self.x = xcenter
            self.y = ycenter
            self.radius = rad
            # self.xvelocity = 0
            # self.yvelocity = 0

        def setCentreCoordinates(self,xcenter,ycenter):
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

This piece of Python contains lots of new ideas. Before we explore them, feel free to use ipython to check the help for this class definition.

    $ ipython
    $ from triangleClass import triangleClass
    $ help(triangleClass)

"triangleClass", is a example of a Class. Classes are used to package up functions with associated data. As you can see in the help(), we can only see the functions defined in the class. It has several functions, `__init__` (always enclosed on either side by two underscores), which is used to construct a new Object of type triangleClass, and several "set" and "get" functions, each of which is used to either retreive or set triangleClass data members. As you can see, the first argument to each of these functions is "self". "self" is a special variable that is used by the Class to gain access to the data hidden within. 

Lets look again at the source for [triangleClass-v1.py](https://github.com/davidglo/boot-camps/blob/2017-TMCS-software/triangleClass-v1.py)

    class triangleClass:

        def __init__(self,ID,color,xcenter,ycenter,rad):
            """ initialize a triangle """
            self.ID = ID
            self.color = color
            self.x = xcenter
            self.y = ycenter
            self.radius = rad
            # self.xvelocity = 0
            # self.yvelocity = 0

        def setCentreCoordinates(self,xcenter,ycenter):
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

Here you can see that the keyword "class" is used to define a new class (in this case, called triangleClass). Within the class you can see defined a number of functions. The first is `__init__` followed by several others which we used to set & retreive data that lives on teh class. The `__init__` function is special, and is called the "constructor". It must be present in all classes, and constructors are used in all object orientated programming languages. The job of the constructor is to define how to create an object of the class, i.e. how to initialise the data contained within the class. In general, data is either passed in explicitly, or else set to sensible defaults. This data initialization is often called the 'instantiation' of the class: this is what programmers mean when they refer to "objects" - i.e., objects are the "instantiations" of a particular class definition (think of Plato!). 

In this case, you can see that the constructor takes as input six data members: "self", which is always required for any member function in a class definition, "ID", which is a string that will hold the triangle's ID, "color", which holds a string for the color we want our triangle to be, "xcenter" & "ycenter", which give the center of the triangle, and "rad", which gives the distance of each triangle vertex to the center point. Sometimes when you look at class definitions in python you will see that data member variables start with two underscores (e.g., self.`__color`). This is the way you tell Python that the variables are private to the class, and cannot be modified unless modifications occur through member functions on the class. If you look at other class definitions, you will see that class data members often start with two underscores. This is not strictly necessary, but is good programming practice to ensure that all class variable names in python are private. We will avoid using the underscores here, simply to make the code easier to read, but I definitely recommend it as good practice.

The constructor takes as input the data which we pass in, and then defines variables which are attached to "self", via the full stop, e.g. "self.ID", "self.color", "self.x", etc. "self" is a special variable that is only available within the functions of the class, and provides access to the hidden data of the class. You can see that "self" is also used by the other functions in the class - setCentreCoordinates(), getColor(), getRadius(), getX(), and getY().

An instantiation of a particular class is called an object. We can construct as many instances (objects) of a class as we want, and each will have its own "self" and its own set of hidden variables. 

So, how do we use the triangleClass in practice - e.g., in our [drawTwoTriangles-refactor2.py](https://github.com/davidglo/boot-camps/blob/2017-TMCS-software/drawTwoTriangles-refactor2.py) code? Let's have a look

First we must make drawTwoTriangles-refactor2.py aware of our class definition:

    from triangleClass import triangleClass
    
Immediately afterward, we add the following to initialize two triangle objects:

    # initialize the triangles that we will be drawing
    triangle1 = triangleClass('triangle1', 'blue',    0, 0, 20)
    triangle2 = triangleClass('triangle2', 'hotpink', 0, 0, 20)
    
This is key - it's where we "instantiate" an object from a class defintion. We're saying: 
*"initialize an object triangle1 from class triangleClass, using 'triangle1', 'blue',    0, 0, 20 as arguments to the triangleClass constructor"
*"initialize an object triangle2 from class triangleClass, using 'triangle2', 'hotpink', 0, 0, 20 as arguments to the triangleClass constructor"

It's worth putting breakpoints at these lines, and the hovering over 'triangle1' and 'triangle2' after we've instantiated them as objects. this will give you a great feel for how PyCharm thinks about objects - i.e., as a collection of data.

So how do we use these objects? through the "dot operator" as follows:

In `__init__()` we can swap out 

    self.center1 = [self.width / 2, self.height / 2]  # initialize the centre of the triangle
    self.center2 = [self.width / 2, self.height / 2]  # initialize the centre of the triangle
 
by using the member function setCentreCoordinates to which each triangle object has access:
 
    triangle1.setCentreCoordinates(self.width / 2, self.height / 2)
    triangle2.setCentreCoordinates(self.width / 2, self.height / 2)

You should use a breakpoint with PyCharm's 'step into' function in order to see how the above code works. We can do a similar thing in update(), replacing 

    self.center1 = [window.width / 2 + randint(-200, 200), window.height / 2 + randint(-200, 200)]
    self.center2 = [window.width / 2 + randint(-200, 200), window.height / 2 + randint(-200, 200)]

with the appropriate triangleClass member functions. You should do this now.

In on_draw(), we can swap 

    vertexList = calculateTriangleVertices(radius,self.center1[0],self.center1[1])

by using member functions on triangleClass to query the values of radius, X, and Y on triangle1:

    vertexList = calculateTriangleVertices(triangle1.getRadius(),triangle1.getX(),triangle1.getY())

In the example above, we have constructed two different triangleClass objects, named triangle1 and triangle2. Key to the practice of object-oriented programming is the notion of "Abstraction". One of the best definitions of abstraction I’ve ever read states: “An abstraction denotes the essential characteristics of an object that distinguish it from all other kinds of object and thus provide crisply defined conceptual boundaries, relative to the perspective of the viewer.” (G. Booch, in "Object-Oriented Design With Applications", Benjamin/Cummings, Menlo Park, California, 1991). In this case, objects are defined by their data: color, id, x & y position, and radius.

Note that we don't need to pass "self" ourselves to the member class functions. "self" is passed implicitly by Python when we construct an object of the class, or when we call a function of the object.

## Exercise 4a

Add the calculateTriangleVertices() to the triangleClass definition, and rework your code to utilize it. Hint: you should not need to pass anything into the function when it is called, because all the relevant data should now be included in the triangleClass definition. This should start to make your code a lot more streamlined.

If you are really stuck, the example scripts are here:
* [4a/drawTriangle.py](4a/1c-drawTriangle.py)
* [4a/triangleClass.py](4a/triangleClass.py)

## Exercise 4b

Instead of triangles which are randomly placed each frame, let's allow the triangles to make simple linear transits across the screen, updating their positions from their last position. The member data in objects is "persistent" - i.e., it exists in the state we left it until we change it, or until we call the object's "destructor" function. Ojbect persistence means that we can increment position based on the last position. For this simple linear transit code, the triangles should be initialized with a certain velocity. If they hit the wall, let them reflect off the wall by reversing the sign of the appropriate velocity component. 

Hints: 
* to do this, we will need to add a velocity data member to the triangleClass definition 
* we will also probably need a function which sets the initial velocity, called from `__init__`
* we will also need a function that updates the coordinates based on the velocity values, and reverses the appropriate velocity components if the triangle reaches a wall
* to really get the sense of motion, you will need to change the screen refresh rate. At present, it's set to 1/2 seconds; however, the human eye does not typically see motion as continuous until we have refresh rate close to 1/30 seconds.

If you are really stuck, the example scripts are here:
* [4b/drawTriangle.py](4b/2c-drawTriangle.py)
* [4b/triangleClass.py](4b/2c-triangleClass.py)

## Exercise 4c

One of the really powerful things about working with objects is that lists can hold objects. So for example, our previous triangle instantiations, which we wrote as

    # initialize the triangles that we will be drawing
    triangle1 = triangleClass('triangle1', 'blue',    0, 0, 20)
    triangle2 = triangleClass('triangle2', 'hotpink', 0, 0, 20)
    
could have also been formulated as

    # initialize a list of triangles 
    triangles = []
    
    # populate the list of triangles
    triangles.append(triangleClass('triangle1', 'blue',    0, 0, 20))
    triangles.append(triangleClass('triangle2', 'hotpink', 0, 0, 20))
    
We could then do something like

    for i in range(0,len(triangles)):
        triangles[i].setCentreCoordinates(self.width / 2, self.height / 2)

For code with lots of objects, you can see how useful this sort of thing would be. Your job in this exercise is to implement the triangles list described above, and refactor your code to make use of loops over this list. Then you should be able to easily extend your code so that it can draw and propagate the motion of five triangles, each a different color, and a different initial velocity.

If you are really stuck, the example scripts are here:
* [4c/drawTriangle.py](4c/3c-drawTriangle.py)
* [4c/triangleClass.py](4c/3c-triangleClass.py)



