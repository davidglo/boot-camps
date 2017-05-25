import random

"""Simple module for importing a color dictionary"""

color = {}                                  # declare a color dictionary
color['yellow']   = [1.0, 1.0, 0.0]         # fill each entry of the color dictionary with a list of three floats
color['blue']     = [0.0, 0.0, 1.0]
color['lightblue'] = [0.5, 0.5, 1.0]
color['red']      = [1.0, 0.0, 0.0]
color['green']    = [0.0, 1.0, 0.0]
color['sienna']   = [0.627, 0.322, 0.176]
color['hotpink'] =  [1.0, 0.412, 0.706]
color['white'] = [1.0, 1.0, 1.0]
color['random'] = [random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)]

keys = color.keys()

# def printAvailablecolors():
#     print "The available colours are as follows, alongside their OpenGL RGB code:-"
#     print "\n"
#     for i in range(0, len(keys)):
#         print keys[i], " == ", color[keys[i]]

def printAvailableColors():
    """Here is the documentation string for this function"""
    print '\tyellow'
    print '\tblue'
    print '\tred'
    print '\tgreen'
    print '\tsienna'
    print '\thotpink'
    print "\twhite"
    print '\trandom'

if __name__ == "__main__":
    print 'Executing colors.py as the main routine'
    print '--We have definitions of:'
    printAvailableColors()

