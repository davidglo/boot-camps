
# Good Programming Practice - Documenting Code

In the [last session](2_functions_and_modules.md) you learned how to package code into functions and to package functions into modules (also called libraries). Functions and modules let you easily design, write and package your code so that it is easy to understand and easily reusable. However, to share the code, and in order to help others (and even yourself, several months or years later) to really understand how it works, you need to add documentation. The general rule of thumb is that YOU CAN NEVER HAVE ENOUGH DOCUMENTATION.

You have already seen the documentation which available from within PyCharm's autocomplete function, and also using python's "help()" functionality. For example, lets use ipython to look at the documentation for the "string" module.

    $ ipython
    $ import string
    $ help(string)
    Help on module string:
    
    NAME
        string - A collection of string operations (most are no longer used).
    
    FILE
        /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/string.py
    
    MODULE DOCS
        http://docs.python.org/library/string
    
    DESCRIPTION
        Warning: most of the code you see here isn't normally used nowadays.
        Beginning with Python 1.6, many of these functions are implemented as
        methods on the standard string object. They used to be implemented by
        a built-in module called strop, but strop is now obsolete itself.

Lets compare this to the documentation for the "colors.py" script that we used in the last session. you can check the doc by navigating to the directory where 'colors.py' lives, opening up ipython, then doing

    $ import colors
    $ help(colors)
    
you get 

    Help on module colors:

    NAME
        colors

    FILE
        /Users/glowacki/Google Drive/hackathon/hackathon-2017/colors.py

    DATA
        color = {'blue': [0.0, 0.0, 1.0], 'green': [0.0, 1.0, 0.0], 'hotpink':...

Not great... It is very important when programming in any language that we provide full documentation for all of the functions and modules. In python, this is achieved by adding documentation strings to each part of the script. These are strings that are placed at the beginning of the function or module.

    $ def documentedFunction(a):
    $     """Here is the documentation string for this function"""
    $     return a
    $
    $ help(documentedFunction)
    
    Help on function documentedFunction in module __main__:
    
    documentedFunction(a)
        Here is the documentation string for this function

We can do the same thing for colors.py:

    """colors is a simple module for creating a color dictionary"""

    color = {}  # declare a color dictionary
    color['yellow'] = [1.0, 1.0, 0.0]  # fill each entry of the color dictionary with a list of three floats
    color['blue'] = [0.0, 0.0, 1.0]
    color['red'] = [1.0, 0.0, 0.0]
    color['green'] = [0.0, 1.0, 0.0]
    color['sienna'] = [0.627, 0.322, 0.176]
    color['hotpink'] = [1.0, 0.412, 0.706]

    def printAvailableColors():
        """This function prints all available colors within our dictionary"""
        print '\tyellow'
        print '\tblue'
        print '\tred'
        print '\tgreen'
        print '\tsienna'
        print '\thotpink'

    if __name__== "__main__":
        print 'executing colors.py as the main routine'
        print 'we have definitions of:'
        printAvailableColors()

We now get better documentation when using help()

    $ ipython
    $ import colors
    $ help(colors)
    NAME
        colors - colors is a simple module for creating a color dictionary

    FILE
        /Users/glowacki/Google Drive/hackathon/hackathon-2017/colors.py

    FUNCTIONS
        printAvailableColors()
            This function prints all available colors within our dictionary

    DATA
        color = {'blue': [0.0, 0.0, 1.0], 'green': [0.0, 1.0, 0.0], 'hotpink':...

### Exercise

Edit your two-triangle drawing code and the associated color module to add documentation strings as indicated above.


