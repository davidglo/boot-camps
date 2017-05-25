import pyglet
import pyglet.gl
import math
from random import randint
import random


class graphicsWindow1(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow1, self).__init__()  # constructor for graphicsWindow class
        self.sprite = pyglet.image.load("Mano.png").get_texture()
        #kitten = pyglet.image.load('kitten.png').get_texture()

        self.width = 225
        self.height = 225

    def update(self, dt):
        if pyglet.window.Window.has_exit == False:

            pyglet.window.Window.set_location(self, randint(0, 1000), randint(0, 500))

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        pyglet.gl.glColor3f(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        self.sprite.blit(self.width / 8 - 27, self.height / 8 - 27)

class graphicsWindow2(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow2, self).__init__()  # constructor for graphicsWindow class
        self.sprite = pyglet.image.load("logan.png").get_texture()
        # kitten = pyglet.image.load('kitten.png').get_texture()

        self.width = 225
        self.height = 225

    def update(self, dt):
        if pyglet.window.Window.has_exit == False:

            pyglet.window.Window.set_location(self, randint(0, 1000), randint(0, 500))

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        pyglet.gl.glColor3f(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))

        self.sprite.blit(self.width / 8 - 27, self.height / 8 - 27)

class graphicsWindow3(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow3, self).__init__()  # constructor for graphicsWindow class
        self.sprite = pyglet.image.load("Glowacki.png").get_texture()
        # kitten = pyglet.image.load('kitten.png').get_texture()

        self.width = 225
        self.height = 225

    def update(self, dt):
        if pyglet.window.Window.has_exit == False:
            pyglet.window.Window.set_location(self, randint(0, 1000), randint(0, 500))

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        pyglet.gl.glColor3f(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))

        self.sprite.blit(self.width / 8 - 27, self.height / 8 - 27)

class graphicsWindow4(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow4, self).__init__()  # constructor for graphicsWindow class
        self.sprite = pyglet.image.load("Tew.png").get_texture()
        # kitten = pyglet.image.load('kitten.png').get_texture()

        self.width = 225
        self.height = 225

    def update(self, dt):
        if pyglet.window.Window.has_exit == False:
            pyglet.window.Window.set_location(self, randint(0, 1000), randint(0, 500))

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        pyglet.gl.glColor3f(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))

        self.sprite.blit(self.width / 8 - 27, self.height / 8 - 27)



# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow1()  # initialize a window class
    if pyglet.window.Window.has_exit == False:
        #window = pyglet.window.Window(caption = 'Trivial')
        pyglet.clock.schedule_interval(window.update, 1 / 2.5)
        # tell pyglet the on_draw() & update() timestep

    window = graphicsWindow2()  # initialize a window class
    if pyglet.window.Window.has_exit == False:
        pyglet.clock.schedule_interval(window.update, 1 / 1.0)  # tell pyglet the on_draw() & update() timestep

    window = graphicsWindow3()  # initialize a window class
    if pyglet.window.Window.has_exit == False:
        pyglet.clock.schedule_interval(window.update, 1 / 0.5)  # tell pyglet the on_draw() & update() timestep

    window = graphicsWindow4()  # initialize a window class
    if pyglet.window.Window.has_exit == False:
        pyglet.clock.schedule_interval(window.update, 1 / 0.5)  # tell pyglet the on_draw() & update() timestep


    pyglet.app.run()  # run the infinite pyglet loop