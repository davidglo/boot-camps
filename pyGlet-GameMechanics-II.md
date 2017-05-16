# Simple Game Mechanics in Python

you've been working hard learning about python now. And along the way you've been building a nice little game engine which has actually gotten quite sophisticated. The point of this section is really just to have fun, hack around, and let your creativity go where it wants! You have the chance to use the stuff that you've learned so far to experiment with and develop the simple game framework that we've been referring to.

There is an excellent & very easy tuturial on basic pyGlet structure which is [available at this link](http://simeonfranklin.com/talk/pyglet/slides.html#slide-1), which you should work your way through. Don't worry about making the game suggested in the final slide of the tutorial. Do what you want. play around. make mistakes. do something crazy. try adding sprites for example. if you want to experiment with sprites for example, then these little *.pngs (which should be easy to use as sprites) might get your creative juices flowing.
* [manby](https://github.com/davidglo/boot-camps/blob/2017-TMCS-software/manby.png)
* [logan](https://github.com/davidglo/boot-camps/blob/2017-TMCS-software/logan.png)
* [essex](https://github.com/davidglo/boot-camps/blob/2017-TMCS-software/essex.png)

#Other things to try

There's lots of other things that you could try and do with this code. do what you want, but if you are stumped, then here are some suggestions:

* Figure out how to make classes for shapes other than triangles (e.g., pentagons, octagons, circles, ellipses, etc.)
* Experiment with different ways of making the circles move. For example, see if you can figure out how to write a function which will make the circles travel in different ways. For example, you could make them move:
    
    1. On circular trajectories
    
    2. Harmonically, based on how far the circle is displaced from the center of the graphics window
    
    3. On trajectories of the sort that you might expect for particles which have some kind of force interaction with the other particles in the system - e.g., harmonic interactions, Lennard-Jones interactions, or even gravitational fields. To incorporate forces, you will require an update scheme which incorporates forces - e.g., the so-called [velocity verlet scheme](https://en.wikipedia.org/wiki/Verlet_integration) is good way of doing this.
    
PyGlet has lots of options - for example it can implement sounds (you could make a bang when particles collide!), and also it can recognize keystrokes to control things in simple games. If you are really ambitious, you could even imagining trying to build a simple game of the old classic "pong"!

Be creative - this is a chance to experiment & have fun and see what you can do.
