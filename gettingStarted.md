# Getting Started with Python

## Setup
1. Make sure you have python installed. I suggest you use [Anaconda for python 2.7](https://www.continuum.io/downloads)
2. you should then [pip install pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Download) 
3. Install the community edition of [PyCharm](https://www.jetbrains.com/pycharm/)
4. be sure to point your PyCharm interpreter to the Anaconda installation of Python. Instructions for doing that [can be found here](https://docs.continuum.io/anaconda/ide_integration#pycharm). If you want to learn more about the Anaconda environment and package management, have a look at the [Anaconda documentation](http://conda.pydata.org/docs/using/index.html).

## Hello World

Let's get going with a very simple "hello world" program in python. There's a number of ways to write this very simple python program, and you should be familiar with them. We'll cover three ways here. 

The first way utilizes interactive python, or "ipython".

    $ ipython

Within the ipython shell, type

    $ print 'hello world'
    $ print 'hello again'
    $ meaningOfLife = 42.0
    $ mysticalSign = 19.0
    $ keyToTheMeaningOfLife = meaningOfLife/mysticalSign
    
    $ print '\n'
    $ print 'keyToTheMeaningOfLife = ', keyToTheMeaningOfLife
    $ print 'keyToTheMeaningOfLife * ', mysticalSign,' = ', keyToTheMeaningOfLife * mysticalSign
    $ print '\n'

when you hit 'enter' at the end of each line, ipython will print out the specified text. You can exit ipython using ctrl + d.

The second way way to get python to print out 'hello world' uses standard command line python. Using a text editor, make a file called "hello.py". The file contents should be as follows:

```
print 'hello world'
print 'hello again'

meaningOfLife = 42.0
mysticalSign = 19.0
keyToTheMeaningOfLife = meaningOfLife/mysticalSign

print '\n'
print 'keyToTheMeaningOfLife = ', keyToTheMeaningOfLife
print 'keyToTheMeaningOfLife * ', mysticalSign,' = ', keyToTheMeaningOfLife * mysticalSign
print '\n'
```

From within the same directory, type 

    $ python hello.py

when you hit 'enter', python should execute & print out the specified text.

A third way to get python to print out 'hello world' utilizes an integrated development environment (IDE). 

IDEs offer software developers a customizable and integrated set of tools for managing software projects, writing code, debugging, and unit testing. IDEs allow developers to efficiently manage large and complex software projects, which they would struggle with if they were to do it the 'old-fashioned' way - e.g., using text editors and print statements for debugging.

Major software development firms have shown (over and over again) that developer efficiency increases dramatically using IDEs. When it comes to scientific software development, where you often find yourself working on legacy code which is the product of several developers over the years (e.g., generations of PhDs and post-docs), the visual debugger provided by an IDE (combined with powerful integrated search tools) can save massive amounts of time understanding how previous contributors have organized the code and the order in which various bits of the program are executed.

Different languages and platforms have their own IDE tools. For example, OSX developers writing in C++, C, iOS, or Objective C tend to use XCode, which is Apple's IDE. Microsoft developers writting in C++, C, or C# for Windows platforms often use Microsoft's Visual Studio IDE.

It's a little more complicated to set up a hello world program using PyCharm, but it's worth it for lots of reasons. One of the most popular IDEs for Python is called PyCharm - this is going to be our preferred way of writing python during this course. It's a little more complicated to get hello World going in PyCharm, but it's worth it. Follow the steps below to get going:

1) make a directory called /helloTest
2) open PyCharm
3) On the Welcome screen, click Create New Project
4) specify that the project should live in /helloTest
5) be sure to choose the anaconda python interpreter
6) Click Create
7) in the project explorer, right click the 'helloTest directory', and add a new file called 'hello.py'
8) use the PyCharm text editor to fill 'hello.py' with the following:
```
# hello world
print 'hello world'
print 'hello again'

meaningOfLife = 42.0
mysticalSign = 19.0
keyToTheMeaningOfLife = meaningOfLife/mysticalSign

print '\n'
print 'keyToTheMeaningOfLife = ', keyToTheMeaningOfLife
print 'keyToTheMeaningOfLife * ', mysticalSign,' = ', keyToTheMeaningOfLife * mysticalSign
print '\n'
```
Now we will run the code from within PyCharm. To do this, right click on 'hello.py' from within the project explorer, and click 'Run hello.py' (You can also click 'Debug hello.py'). you should see that PyCharm opens a console and prints out the text.

In the simple code we wrote above, the keyToTheMeaningOfLife is clearly very useful, but not very easy to use or reusable. For example, say we started up a business with a code-base that required us to calculate keyToTheMeaningOfLife for billions of customers worldwide based on some value of mysticalSign given to us by each customer. And say that calculating keyToTheMeaningOfLife was a little bit more complicated than simple division. Calculating keyToTheMeaningOfLife would rapidly become unsustainable: we would have to carry out all sorts of edits, copying and pasting our code every time we need to calculate meaningOfLife within our code-base, potentially based on some different mysticalSign or even meaningOfLife values. You can see how this would get really tedious, and ultimately hurt out profit margins.

Functions provide a way of packaging code into reusable and easy-to-use components. We can turn our keyToTheMeaningOfLife by defining a function - let's call it meaningOfLifeCalculator. To define such a function, we write
```
def meaningOfLifeCalculator(meaning, sign):
    key = meaning/sign
    print 'keyToTheMeaningOfLife = ', key
    print 'keyToTheMeaningOfLife * ', sign, ' = ', key * sign
    return key
```
Now we can quickly calculate the meaning of life for any mysticalSign or any meaningOfLife, simply by calling meaningOfLifeCalculator as follows
```
functionOutput = meaningOfLifeCalculator(meaningOfLife,mysticalSign)
```

In this case I have called the function "meaningOfLifeCalculator" and passed in the arguments "meaningOfLife" and "mysticalSign". "meaningOfLife" is copied to "meaning", while "mysticalSign" is copied to "sign". The function meaningOfLifeCalculator then acts on "meaning" and "sign", creating "key". It then returns "key", which is copied back to "functionOutput".

Let's get this working in PyCharm by pasting the following code into our editor.
```
def meaningOfLifeCalculator(meaning, sign):
    key = meaning/sign
    print 'keyToTheMeaningOfLife = ', key
    print 'keyToTheMeaningOfLife * ', sign, ' = ', key * sign
    return key

print 'hello world'
print 'hello again'

meaningOfLife = 42.0
mysticalSign = 19.0
keyToTheMeaningOfLife = meaningOfLife/mysticalSign

print '\n'
print 'keyToTheMeaningOfLife = ', keyToTheMeaningOfLife
print 'keyToTheMeaningOfLife * ', mysticalSign,' = ', keyToTheMeaningOfLife * mysticalSign
print '\n'

print 'executing meaningOfLifeCalculator...'
functionOutput = meaningOfLifeCalculator(meaningOfLife,mysticalSign)
print 'keyToTheMeaningOfLife = ', functionOutput
print '\n'

print 'thats all folks'
```

Next we'll learn how to use PyCharm's debugging features to go examine execution flow of this simple example code.

