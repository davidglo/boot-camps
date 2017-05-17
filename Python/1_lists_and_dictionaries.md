
# Containers - Lists and Dictionaries

Writing a program involves creating and manipulating data, which are held in variables. For example, we've used variables before

    $ meaningOfLife = 42.0
    $ mysticalSign = 19.0
    $ keyToTheMeaningOfLife = meaningOfLife/mysticalSign
    $ print keyToTheMeaningOfLife
    2.2105

Another example of using variables could also involve strings. For example:

    $ a = "hello "
    $ b = "world"
    $ print a + b
    hello world

Note here how we had to add an extra space after "hello". Typing and working with variables one-by-one like this is easy, but would be very time-consuming and prone to error if you have a program that uses thousands or millions of variables. Containers allow you to group variables together. The simplest container is a list.

## Lists

Lists, which are also called arrays or vectors, provide a simple list of variables. In python, we create lists using square brackets. For example

    $ testList = [14, 7, 28, 42]

would initialize a list with four elements. To access items in the list we use square brackets:

    $ print testList[0]
    14
and

    $ print testList[1]
    7

and

    $ print testList[2]
    28

and

    $ print testList[3]
    42

Note that element "0" of the list in fact denotes the first element of the list. In python, you can also work from the back of the list

    $ print testList[-1]
    42

printing the last item.

    $ print testList[-2]
    28

printing the second to last item, etc. If you access an item that doesn't exist, then you get an error.

    $ print testList[4]

gives an "index out of range" error.

To get the number of items in the list, we have to use "len"

    $ print len(testList)
    4

as we have four things in the list.

We can also change the value of an item by setting it equal to a new value

    $ testList[0] = 20
    $ print testList
    [20, 7, 28, 42]

The previous code we looked at (pyGlet-drawLine.py), uses some lists. For example
```
self.center1 = [self.width / 2, self.height / 2]    # initialize the centre of the line
```
initializes a list with two elements, self.width/2 and self.height/2, where self.width & self.height are variables that we specify in code.

### Functions of a List

A list comes with lots of useful abilities. You can see the list of abilities in PyCharm by declaring a list as follows
```
testList = []
```
and then typing
```
testList.
```
PyCharm should bring up an auto-complete menu, which includes all the functions that are available for lists. Alternatively, you could also type a line in your code which reads
```
help(testList) 
```
Put a breakpoint at the line, step over it, and then inspect the console output. Either way you use - auto-complete or help(), you will see that the available functions for a list are as follows:
```
    append    count    extend    index    insert    pop    remove    reverse   sort
```
The abilities are provided by functions, for example "append". There's a good dicussion of [how to use these functions at this link](https://www.digitalocean.com/community/tutorials/how-to-use-list-methods-in-python-3). One function which we will use extensively is "append", which is used to add items onto the end of the list. For example
```
testList=[]
```
declares a blank list. 
```
testList.append(27)
```
adds "27" to the list, i.e., 

    $ print testList
    [27]

We can append as many values as we want.

    $ testList.append(42)
    $ print testList
    [27,42]

We can also remove values from a list. For example

    $ testList.remove(42)

will remove the value 42 from testList.

### Looping over a list

You can iterate over all items in a list using a loop, for example

    $ testList = [14, 7, 28, 42]
    $ for i in range(0, len(testList)):
    $     print( testList[i] )
    
    14
    7
    28
    42

This can be useful, for example, for adding together two sets of numbers;

    $ x = [ 1, 2, 3, 4 ]
    $ y = [ 5, 6, 7, 8 ]
    $ z = []
    $ for i in range(0, len(x)):
    $     z.append( x[i] + y[i] )
    $
    $ z
    
    [6, 8, 10, 12]

### Nesting lists

Lists can contain a mixture of any type of data. For example, you can mix numbers and strings

    $ a = [ "cat", 15, 6.5 ]
    $ a
    ['cat', 15, 6.5]

Lists can also contain other lists, for example,

    $ matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]
    $ matrix
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

This is called "nesting" one list inside another. Accessing the sub-list, or items within it is easy.

    $ matrix[1]
    [5, 6, 7, 8]
    $ matrix[1][2]
    7

You can nest lists as deeply as you want, creating a multidimensional matrix.

    $ matrix = [ [ [ [ [ 5 ] ] ] ] ]
    $ matrix[0][0][0][0][0]
    5

## Dictionaries (A.K.A Associative Arrays)

Associative Arrays (which are called 'dictionaries in python) are one of the really nice features of many object oriented languages. For certain tasks, they make your life a lot easier. Whereas lists let you store lots of variables, accessing them requires you to know their location in the list. However, there are lots of times when you want to store lots of variables, but access them using more complex relationships. Associative arrays let you store variables and access them using a key. 

Dictionaries in python are represented using curly brakets

    $ a = { "cat" : "meeow", "dog" : "woof", "horse" : "neigh" }

Here I am storing four key-value pairs. I am storing the value "meeow", and saying that this is accessed using the key "cat". 

    $ print a["cat"]
    'meeow'

Similarly, I have stored the value "woof", and have said that this is accessed using the key "dog"

    $ print a["dog"]
    'woof'

Like lists, dictionaries also come with a lot of useful functions, which we can show using the autocomplete functionality in PyCharm 

    $ a.

or else via the help function.

    $ help(a)

Either way we can inspect the functions available for processing data in lists:

    clear       get         iteritems   keys        setdefault  viewitems   
    copy        has_key     iterkeys    pop         update      viewkeys    
    fromkeys    items       itervalues  popitem     values      viewvalues  

There's a nice overview of [dictionary methods at this link] (https://docs.python.org/2/library/stdtypes.html#mapping-types-dict). One particularly useful method is the keys() function, which returns a list of all of the keys

    $ print a.keys()
    ['horse', 'dog', 'cat']

while the values() function returns the list of all of the values

    $ print a.values()
    ['neigh', 'woof', 'mieow']

We can change items in the dictionary by setting them equal to a new value

    $ a["dog"] = "bark"
    $ print a
    {'cat': 'mieow', 'dog': 'bark', 'horse': 'neigh'}

We can also use this to add new items to the dictionary

    $ a["fish"] = "bubble"
    $ print a
    {'cat': 'mieow', 'dog': 'bark', 'fish': 'bubble', 'horse': 'neigh'}

### Looping over a dictionary

As the keys() function returns the list of all keys in a dictionary, the best way to loop over all items in a dictionary is to loop over the list of keys

    $ keys = a.keys()
    $ for i in range(0,len(keys)):
    $     print keys[i], " == ", a[keys[i]]
    
    horse == neigh
    dog == bark
    fish == bubble
    cat == mieow

You could print them out in alphabetical order by using the sort() function of a list to sort the keys before looping. Have a look at the methods available for manipulating the keys by again using either PyCharm's autocomplete

    $ keys.
    
or else via the help function

    $ help(keys)
 
Either way, we see the following methods
    
    append   extend   insert   remove   sort     
    count    index    pop      reverse  

    $ keys.sort()
    $ print keys
    ['cat', 'dog', 'fish', 'horse']

    $ for i in range(0,len(keys)):
    $     print("%s == %s" % (keys[i], a[keys[i]]))

    cat == meeow
    dog == bark
    fish == bubble
    horse == neigh

### Nesting dictionaries

Like lists, dictionaries can contain any type of data, and you can also nest dictionaries and lists inside each other.

    $ a = { "cat" : 5, "dog" : ["walk", "feed", "sleep"], "fish" : {"type" : "goldfish"} }
    $ print a["cat"]
    5
    $ print a["dog"]
    ['walk', 'feed', 'sleep']
    $ print a["dog"][1]
    'feed'
    $ print a["fish"]["type"]
    'goldfish'

You can also create the above dictionary item-by-item

    $ a = {}
    $ a["cat"] = 5
    $ a["dog"] = [ "walk", "feed", "sleep" ]
    $ a["fish"] = { "type" : "goldfish" }
    $ print a
    {'cat': 5, 'dog': ['walk', 'feed', 'sleep'], 'fish': {'type': 'goldfish'}}


## Strings as lists

Finally, we will finish this session by noting that strings are actually lists. A string is a list container of letters.

    $ a = "hello world"
    $ print len(a)
    11
    $ print a[0]
    'h'
    $ print a[-1]
    'd'

We can loop over all letters in a string using

    $ for i in range(0,len(a)):
    $     print(a[i])
    h 
    e
    l
    l
    o
     
    w
    o
    r
    l
    d

Python provides a nice shorthand for looping over every item in a list

    $ for letter in a:
    $    print letter

will print the same output.

You can also create a string from a list of letters. For this, you need to import and use the "string" module from python

    $ import string
    $ a = ['h', 'e', 'l', 'l', 'o']
    $ print a
    ['h', 'e', 'l', 'l', 'o']

    $ s = string.join(a)
    $ print s
    'h e l l o'

Note that string.join has added a space between each letter. Using help() we can see how to remove this space

    $ help(string.join)
    Help on function join in module string:
    
    join(words, sep=' ')
        join(list [,sep]) -> string
    
        Return a string composed of the words in list, with
        intervening occurrences of sep.  The default separator is a
        single space.
    
        (joinfields and join are synonymous)

    $ s = string.join(a, "")
    $ s
    'hello'

Let's return to the simple line drawing program we looked at earlier. The script is available as [drawTriangle.py](https://github.com/davidglo/boot-camps/blob/2017-TMCS-software/drawTriangle.py). 

        # now we will calculate the list of vertices required to draw the triangle
        numberOfVertices = 3        # specify the number of vertices we need for the shape
        radius = 20                 # specify the radius of each point from the center
        xcenter = self.center1[0]   # specify xcenter
        ycenter = self.center1[1]   # specify ycenter
        vertices = []  # initialize a list of vertices

        angle = 0.0               # specify the first vertex of the triangle (x,y values)
        x = radius * cos(angle) + xcenter
        y = radius * sin(angle) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

        angle = (2.0 / 3.0) * pi  # specify the second vertex of the triangle (x,y values)
        x = radius * cos(angle) + xcenter
        y = radius * sin(angle) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

        angle = (4.0 / 3.0) * pi  # specify the third vertex of the triangle (x,y values)
        x = radius * cos(angle) + xcenter
        y = radius * sin(angle) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

        # convert the vertices list to pyGlet vertices format
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))

### Exercise 1a

For the purposes of this exercise, we will focus on the code snippet above. There's lots of redundant code in this function, which we can tighten up using what we've learned about lists. Your job is to use PyCharm and its debugging facilities to step through this code, figure out what it's doing, and then refactor it utilizing what you've learned about lists and loops. You should be able to make significant improvements, cleaning up the rendundancy and making much more compact code which is more elegant and less error-prone. This is the sort of task that one often finds oneself having to carry out in the course of a software dev project: explicit code can often be cleaned up and made more transparent through the canny use of lists and dictionaries.

If you are really stuck, then there is an example completed script available to read in [1a/drawTriangle-refactor1.py](1a/drawTriangle-refactor1.py).

### Exercise 1b

Now we are going to play around a little bit with dictionaries and nesting. The particular bit of code which we are going to focus on is the one that specifies the color of the object that is drawn

    glColor3f(1, 1, 0)  # specify colors

This code specifies in OpenGL RGB format what color OpenGL should use for the lines it's about to draw. Each entry is a float ('3f' means 'three floats') specifies the amount of R, the amount of G, and the amount of B, where the possible value of each entry can range from 0 to 1. You can [construct lots of different colors using this simple format](http://prideout.net/archive/colors.php#Floats).

What we're going to do now is use a dictionary to make the arguments to glColor3f() more human readable. For example, it would enable us to choose our aesthetic a lot quicker if we could specify a color by entering code that looked something like

    lineColor = 'hotpink'
    glColor3f(color[lineColor][0], color[lineColor][1], color[lineColor][2]) # specify colors

As you can see, when we want to change colors, we only have to change the value of a single variable. So for example if we want blue (or red or green or yellow or sienna or whatever), we simply have to make a small modification along the lines of:

    lineColor = 'blue'

Your job now is to formulate a nested structure of dictionaries/lists, which allow us to specify colors as I've written above, so that we can change color by simply changing a single word. To do this, you will have to declare the relevant data structures in a location that enables it to be seen "globally" - i.e., acknowledged by everything in our code. We'll learn more about this as we go on, but for the moment I'm going to help you: the location when working with PyGlet should be as follows:

    from random import randint

    ...YOUR CODE HERE...

    class graphicsWindow(pyglet.window.Window):

Once you've figured out how to do this, play around with a few different colors for your triangle. It should be as easy as simply editing the string which indicates color. Feel free to get creative. [The link at this page gives lots of different examples of various colors in '3f' format](http://prideout.net/archive/colors.php#Floats). If you are really stuck, then there is an example completed script available to read in [1b/drawTriangle-refactor2.py](1b/drawTriangle-refactor2.py).

### Exercise 1c

See if you can extend your code to draw more than one triangle, each with a different color and with its own center. So you'll need to modify \__init()__ and update() to include a new data structure self.center2, and then you'll probably need to copy & paste some code in on_draw() in order to tell pyGlet to draw a second list of vertices

If you are hopelessly stuck, then there is an example script available in [1c/drawTwoTriangles.py](1c/drawTwoTriangles.py)

# [Next](https://github.com/davidglo/boot-camps/blob/2017-TMCS-software/Python/2_functions_and_modules.md)
