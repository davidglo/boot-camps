
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

An "object" is a particular instantiation of a "class" definition. Sticking with our triangle example - we can potentially have many objects (i.e., triangles, each with their own position, size, color, and ID), but we will only have one class. If you know anything about Platonic philosophy, object oriented code resembles very much Plato's [theory of forms](https://en.wikipedia.org/wiki/Theory_of_Forms), where everything that we experience phenomenologically is in fact the imperfect manifestation of some idealized and "perfect" form. Plato famously applied his theory of forms to tables. Wikipedia explains the [Platonic theory of forms as follows](https://en.wikipedia.org/wiki/Theory_of_Forms): "For example, there are countless tables in the world but the Form of tableness is at the core; it is the essence of all of them". Substitute "triangles" for "tables" in the above example, and "class" for "Form" - and you are getting to the heart of object oriented programming. Countless triangle objects, but one triangle class, which is the essence of all of them.

Ok, enough philosophy for now. The idea of putting together member data and member functions which are important for certain classes of objects is called "Encapsulation". It's a key idea of object orientated programming, and refers to the practice of hiding the data in a Class, with the net result that only the functions which are defined as part of the Class can read or write (change) the data. Not only can this actually result in simpler to use and easier-to-read code which maps onto the problem we're actually trying to solve, but it also enforces practices that are much less likely to get abused by others (or ourselves in the future) when we're coding.

For example, take a look the code required to make a very basic "triangle" class:

    import pyglet
    import math

    class triangleClass:

        def __init__(self,ID,color,xcenter,ycenter,rad):
            """ construct a basic triangle """
            self.ID = ID
            self.color = color
            self.x = xcenter
            self.y = ycenter
            self.radius = rad

        def setCentreCoordinates(self,xcenter,ycenter):
            """ set the center coordinates of the triangle """
            self.x = xcenter
            self.y = ycenter

        def getColor(self):
            return self.color

        def calculateTriangleVertices(self):
            """ function to calculate the vertex list required to draw an equilateral triangle """
            numberOfVertices = 3  # specify the number of vertices we need for the shape
            vertices = []  # initialize a list of vertices

            for i in range(0, numberOfVertices):
                angle = i * (2.0 / 3.0) * math.pi  # specify a vertex of the triangle (x,y values)
                x = self.radius * math.cos(angle) + self.x
                y = self.radius * math.sin(angle) + self.y
                vertices.append(x)  # append the x value to the vertex list
                vertices.append(y)  # append the y value to the vertex list

            # convert the vertices list to pyGlet vertices format for the first triangle & return this list
            vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))
            return vertexList

This piece of Python contains lots of new ideas. Before we explore them, feel free to use ipython to check the help for this class definition.

    $ ipython
    $ from triangleClass import triangleClass
    $ help(triangleClass)

"triangleClass", is a example of a Class. Classes are used to package up functions with associated data. As you can see in the help(), we can only see the functions defined in the class. There are two functions, `__init__` (always enclosed on either side by two underscores), which is used to construct a new Object of type GuessGame, and "guess" which is used to guess the secret. As you can see, the first argument to each of these functions is "self". "self" is a special variable that is used by the Class to gain access to the data hidden within.

Lets look again at the source for GuessGame (in [guessgame.py](guessgame.py))

    """A simple guessing game"""
    
    class GuessGame:
        """A simple guess the secret game"""
        def __init__(self, secret):
            """Construct a game with the passed secret"""
            self.__secret = secret
            self.__nguesses = 0   # the number of guesses
    
        def guess(self, value):
            """See if the passed value is equal to the secret"""
    
            if self.__nguesses >= 3:
                print( "Sorry, you have run out of guesses." )
    
            elif value == self.__secret:
                print( "Well done - you have won the game!" )
                return True
            else:
                print( "Wrong answer. Try again!" )
                self.__nguesses += 1  # increase the number of wrong guesses
                return False

Here you can see that the keyword "class" is used to define a new class (in this case, called GuessGame). Within the class you can see defined the two functions, `__init__` and "guess". The `__init__` function is special, and is called the "constructor". It must be present in all classes, and constructors are used in all object orientated programming languages. The job of the constructor is to define how to create an object of the class, i.e. how to initialise the data contained within the class. This data initialization is often called the 'instantiation' of the class: this is what programmers mean when they refer to "objects" - i.e., objects are the instantiations of a particular class definition. In this case, you can see that the constructor specifies two data members: "__secret", which will hold the secret to be guessed, and "__nguesses", which holds the number of wrong guesses made to date. Note that these data memember variables start with two underscores. This is the way you tell Python that the variables are private to the class, and cannot be modified unless modifications occur through member functions on the class. While not strictly necessary, it is good programming practice to ensure that all class variable names in python are private, and start with two underscores.

Note that the variables are defined as attached to "self", via the full stop, e.g. "self.__secret". "self" is a special variable that is only available within the functions of the class, and provides access to the hidden data of the class. You can see that "self" is used by the "guess" function to check the passed guess against "self.__secret", and to increase the value of "self.__nguesses" if the guess is wrong.

An instantiation of a particular class is called an object. We can construct as many instances (objects) of a class as we want, and each will have its own "self" and its own set of hidden variables. For example, in what follows we have three different GuessGame objects, named game1, game2, and game3. Key to the practice of object-oriented programming is the notion of "Abstraction". One of the best definitions of abstraction I’ve ever read states: “An abstraction denotes the essential characteristics of an object that distinguish it from all other kinds of object and thus provide crisply defined conceptual boundaries, relative to the perspective of the viewer.” (G. Booch, in "Object-Oriented Design With Applications", Benjamin/Cummings, Menlo Park, California, 1991). In this case, objects are defined by their secret, the number of guesses, and functions that help keep track of whether we have won or lost the game;

    $ ipython
    $ from guessgame import GuessGame
    $ game1 = GuessGame("orange")
    $ game2 = GuessGame("carrot")
    $ game3 = GuessGame("apricot")
    $ game1.guess("apricot")
    Wrong answer. Try again!
    Out[4]: False
    $ game3.guess("apricot")
    Well done - you have won the game!
    Out[6]: True

(Note that we have used the "from X import Y" syntax in Python to import only GuessGame from [guessgame.py](guessgame.py). This allows us to write "game1 = GuessGame("orange")" instead of "game1 = guessgame.GuessGame("orange")".)

Note that we don't need to pass "self" ourselves to the class functions. "self" is passed implicitly by Python when we construct an object of the class, or when we call a function of the object.

## Exercise

### Exercise 4

Edit your [morse.py](3/example/morse.py) script create a class "MorseTranslator" by packaging together the functions "encodeToMorse" and "decodeFromMorse" with the variables "letter_to_morse" and "morse_to_letter".

Make sure that you document your class, e.g. by documenting the `__init__` function you will have to write, and also by documenting the class, as in the above GuessGame class in [guessgame.py](guessgame.py).

When you have finished, test that the Morse code produced by your class is correctly translated back to English, e.g.

    $ ipython
    $ from morse import MorseTranslator
    $ translator = MorseTranslator()
    $ message = "hello world"
    $ translator.decode( translator.encode(message) ) == message
    True

If you get really stuck, you can take a look at the completed example in [4/example/morse.py](4/example/morse.py).

### Extension

The act of encoding and decoding a message to and from Morse code is very similar to encrypting and decrypting a message. Try to write a new class, "Encryptor", that can encrypt a message using an "encrypt" function, and decrypt the message using a "decrypt" function. 

When you have finished, test that your Encryptor can decrypt its own encrypted messages, e.g.

    $ ipython
    $ from encryptor import Encryptor
    $ encryptor = Encryptor()
    $ message = "hello world"
    $ encryptor.decrypt( encryptor.encrypt(message) ) == message
    True

If you get really stuck, then you can take a look at the completed example in [4/example/encryptor.py](4/example/encryptor.py)

Make sure that you commit your edited script to your Git repository.

    $ git commit -am "...commit message..."
    $ git push

