import pyglet
import pyglet.gl
from pyglet.window import key
# import math
from random import randint
# import colors


# graphics window class derived from pyglet one
class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        # loads the images ad sounds
        self.image = pyglet.resource.image('logan.png')
        self.image.width = self.image.width / 1
        self.image.height = self.image.height / 1
        self.imgveg = pyglet.resource.image('manby.png')
        self.imgveg.width = self.imgveg.width / 2
        self.imgveg.height = self.imgveg.height / 2
        self.xvg = self.width / 4
        self.yvg = self.height / 4
        # self.imageveg =
        self.x = self.width / 2
        self.y = self.height / 2
        self.velx = 1
        self.vely = 0
        self.radius = self.image.width / 2
        self.nom = pyglet.resource.media('nom1.wav',streaming=False)


    # updates positions, image moves with a velocity, if imgveg is encountered image grows
    def update(self, dt):
        self.x = (self.x + self.velx) % self.width
        self.y = (self.y + self.vely) % self.height
        if ((self.x-self.xvg)^2+(self.y-self.yvg)^2)<self.radius^2:
            self.image.width += 2
            self.image.height += 2
            self.xvg = randint(0,self.width)
            self.yvg = randint(0, self.height)
            self.nom.play()
            self.radius += 2

    # detects key strokes to change velocity
    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            # self.velx = 2
            # self.vely = 0
            self.velx+=1
        elif symbol == key.UP:
            # self.velx = 0
            # self.vely = 2
            self.vely += 1
        elif symbol == key.DOWN:
            # self.velx = 0
            # self.vely = -2
            self.vely -= 1
        elif symbol == key.LEFT:
            # self.velx = -2
            # self.vely = 0
            self.velx -= 1

    # draws images in given positions
    def on_draw(self):
        window.clear()
        self.image.blit(self.x, self.y)
        self.imgveg.blit(self.xvg, self.yvg)


if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 40.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run the infinite pyglet loop