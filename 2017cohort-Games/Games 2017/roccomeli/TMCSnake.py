"""
Rocco Meli
Software Development Training
TMCS-CDT
University of Oxford
"""
import pyglet
from pyglet.gl import *
from pyglet.window import key
from math import *
import random as rd
import sys
import numpy as np

def makeCircle(numPoints, radius, xcenter, ycenter):
    """
    Define circle as a list of vertexes
    """
    vertices = []
    for i in range(numPoints):
        angle = radians(float(i)/numPoints * 360.0)
        x = radius*cos(angle) + xcenter
        y = radius*sin(angle) + ycenter
        vertices += [x,y]
    circle = pyglet.graphics.vertex_list(numPoints, ('v2f', vertices))
    return circle

class Bullet:
    """
    Bullet (can be shot by the snake)
    """

    def __init__(self,pos,speed):
        """
        Create new bullet
        """

        # Position and speed
        self.pos = np.array(pos,dtype=float)
        self.speed = np.array(speed,dtype=float)

        # Keep track of bounces
        self.bounced = False

    def update(self):
        """
        Update bullet position
        """
        self.pos += self.speed

    def next(self):
        """
        Predict next bullet position
        """
        return self.pos + self.speed

    def bounce(self):
        """
        Make bullet bounce
        """
        # Revert bullet speed
        self.speed *= -1

        self.bounced = True

class Rock:

    def __init__(self,radius,width,height):
        """
        Create rock (obstacle)
        """
        # Rock size
        self.radius = radius

        # Get random coordinates
        # TODO: No overlap with snake
        x = rd.randint(0, width + 1)
        y = rd.randint(0, height + 1)

        self.pos = [x,y]

class Food:
    def __init__(self,width,height):
        """
        Create food at random position within the window
        """
        self.width = width # Window's width
        self.height = height # Window's height

        # Select random position in the window
        # TODO: No overlap with snake or rocks
        x = rd.randint(0,self.width+1)
        y = rd.randint(0,self.height+1)

        self.pos = [x,y]

    def get_pos(self):
        """
        Return food position
        """
        return self.pos

    def new_food(self):
        """
        Create new food at random position within the window
        """

        # New food at random position
        # TODO: No overlap with snake or rocks
        x = rd.randint(0, self.width + 1)
        y = rd.randint(0, self.height + 1)

        self.pos = [x,y]

class Snake:

    def __init__(self,pos,dir,speed):
        """
        Create new Snake
        """
        self.N = 1 # Snake length

        self.pos_list = [pos] # Positions (x,y)
        self.dir_list = [dir] # Directions (+-1,+-1)

        self.speed = speed # Speed (in pixels per refreshes)


    def next_pos(self):
        """
        Compute next position for Snake head 
        """
        next_x = self.pos_list[0][0] + self.dir_list[0][0] * self.speed
        next_y = self.pos_list[0][1] + self.dir_list[0][1] * self.speed

        return [next_x,next_y]

    def self_hit(self):
        """
        Detect self-hit (i.e. superposition of head and tail)
        """
        self_hit = False

        for i in range(1,self.N): # Loop over all particles
            # Check for self hit
            if(self.pos_list[0][0] == self.pos_list[i][0] and self.pos_list[0][1] == self.pos_list[i][1]):
                self_hit = True

        return self_hit

    def update(self,width,height):
        """
        Update snake positions and directions (with PBC)
        """

        for i in range(self.N):
            # Update position
            self.pos_list[i][0] = self.pos_list[i][0] + self.dir_list[i][0] * self.speed
            self.pos_list[i][1] = self.pos_list[i][1] + self.dir_list[i][1] * self.speed

            # Apply PBC
            if (self.pos_list[i][0] < 0):
                self.pos_list[i][0] += width
            elif (self.pos_list[i][0] > width):
                self.pos_list[i][0] -= width
            elif (self.pos_list[i][1] < 0):
                self.pos_list[i][1] += height
            elif (self.pos_list[i][1] > height):
                self.pos_list[i][1] -= height

        # Update directions
        self.dir_list[:] = [self.dir_list[0][:]] + self.dir_list[:-1][:]

        # Check for self hit
        return self.self_hit()

    def grow(self):
        """
        Adds a new particle (head) to the snake
        """

        # Predict new position
        next = self.next_pos()

        # Add one particle to counter
        self.N += 1

        # Add new particle (at predicted new position)
        self.pos_list[:] = [next[:]] + self.pos_list[:]
        self.dir_list[:] = [self.dir_list[0][:]] + self.dir_list[:]


class GUI(pyglet.window.Window):

    def __init__(self,radius,TMCS=False,nobstacles=0,sounds=True):
        """
        Initialise GUI
        """
        self.TMCS = TMCS # Chemists can be fun too!
        self.radius = radius # Snake body radius
        self.sounds = sounds

        if(self.radius > 25):
            print("ERROR: Radius too big.")
            sys.exit(-1)

        # Create windows (proportional to radius)
        super(GUI, self).__init__(width=30*self.radius, height=30*self.radius)

        # Contact distance
        self.d2 = (2*self.radius)**2
        self.d2_bullet = (self.radius+self.radius/2)**2

        # Create snake and food
        self.snake = Snake([10,10],[1,0],2*self.radius)
        self.food = Food(self.width,self.height)

        self.bullets = []

        # Create obstacles
        self.rocks = []
        for i in range(nobstacles):
            self.rocks.append(Rock(self.radius,self.width,self.height))

        # Too bad!
        self.game_over = False

        # Load TMCS faces
        if(self.TMCS):
            self.logan_image = pyglet.image.load('logan.png')
            self.manby_image = pyglet.image.load('manby.png')
            self.essex_image = pyglet.image.load('essex.png')

        # Load sounds
        if(self.sounds):
            self.shot = pyglet.media.load('NFF-fireball-02.wav',streaming=False)

    def draw_snake(self):
        """
        Draw snake (withe balls)
        """

        for i in range(self.snake.N):
            glColor3f(1, 1, 1)
            circle = makeCircle(100,self.radius,self.snake.pos_list[i][0],self.snake.pos_list[i][1])
            circle.draw(GL_LINE_LOOP)
            glColor3f(0, 1, 0)
            circle = makeCircle(100, self.radius/2, self.snake.pos_list[i][0], self.snake.pos_list[i][1])
            circle.draw(GL_LINE_LOOP)

        if(self.TMCS):
            manby = pyglet.sprite.Sprite(self.manby_image,
                                         x=self.snake.pos_list[0][0],
                                         y=self.snake.pos_list[0][1])
            manby.scale = 1. / manby.height * self.radius * 2
            manby.set_position(manby.position[0] - manby.width / 2, manby.position[1] - manby.height / 2)
            manby.draw()

    def draw_food(self):
        """
        Draw food (red ball)
        """
        glColor3f(1, 0, 1)
        circle = makeCircle(100,self.radius,self.food.pos[0],self.food.pos[1])
        circle.draw(GL_LINE_LOOP)

        if(self.TMCS):
            logan = pyglet.sprite.Sprite(self.logan_image, x=self.food.pos[0], y=self.food.pos[1])
            logan.scale = 1. / logan.height * self.radius * 2
            logan.set_position(logan.position[0] - logan.width / 2, logan.position[1] - logan.height / 2)
            logan.draw()

    def draw_rocks(self):
        """
        Draw rocks (obstacles)
        """

        for r in self.rocks:
            glColor3f(1, 0, 0.5)
            circle = makeCircle(100,r.radius,r.pos[0],r.pos[1])
            circle.draw(GL_LINE_LOOP)
            circle = makeCircle(100, r.radius/2, r.pos[0], r.pos[1])
            circle.draw(GL_LINE_LOOP)

    def draw_bullets(self):
        """
        Draw bullets 
        """

        for b in self.bullets:
            glColor3f(0, 1, 1)
            circle = makeCircle(100, self.radius/2, b.pos[0], b.pos[1])
            circle.draw(GL_LINE_LOOP)

            if(self.TMCS):
                essex = pyglet.sprite.Sprite(self.essex_image,
                                             x=b.pos[0],
                                             y=b.pos[1])
                essex.scale = 1. / essex.height * self.radius
                essex.set_position(essex.position[0] - essex.width / 2, essex.position[1] - essex.height / 2)
                essex.draw()

    def draw_gameover(self):
        """
        Draw game over screen
        """

        if(not self.TMCS):

            label = pyglet.text.Label('GAME OVER!',
                                  x=self.width / 2, y=self.height / 2,
                                  anchor_x='center', anchor_y='center')
            label.draw()

        else:
            label = pyglet.text.Label('It\'s trivial!',
                                      x=self.width / 2, y=self.height / 2,
                                      anchor_x='center', anchor_y='center')
            label.draw()

        if(self.TMCS):
            logan = pyglet.sprite.Sprite(self.logan_image, x=self.width / 2, y=self.height / 4)
            logan.scale = 1. / logan.height * self.width / 4
            logan.set_position(logan.position[0] - logan.width / 2, logan.position[1] - logan.height / 2)
            logan.draw()

            logan = pyglet.sprite.Sprite(self.logan_image, x=self.width / 2, y=self.height * 3 / 4)
            logan.scale = 1. / logan.height * self.width / 4
            logan.set_position(logan.position[0] - logan.width / 2, logan.position[1] - logan.height / 2)
            logan.draw()

    def on_draw(self):
        """
        Draw snake and food in the GUI
        """

        # Clean window
        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        if not self.game_over: # Draw snake and food
            self.draw_snake()
            self.draw_food()
            self.draw_bullets()
            self.draw_rocks()
        else: # Draw game over screen
            self.draw_gameover()

    def update(self,dt):
        """
        Update game
        """

        # Update snake
        self_hit = self.snake.update(self.width,self.height)

        if(self_hit): # Check for self-hit
            self.game_over = True

        if self.rock_hit():
            self.game_over = True

        if self.bullet_snake_hit():
            self.game_over = True

        # Update bullets
        for b in self.bullets:
            b.update()

        br_hit, b_idx_list = self.bullet_rock_hit()
        if br_hit:
            for b_idx in b_idx_list:
                self.bullets[b_idx].bounce()

        if self.hit(): # Check for hit with food
            self.snake.grow()
            self.food.new_food()

        # Check bullets
        b_hit, idx = self.bullet_hit()
        if b_hit:
            del self.bullets[idx] # Remove bullet
            self.food.new_food() # New food

            # TODO: Uncomment this line if snake can grow with shoots
            #self.snake.grow() # Grow snake

        # Remove bullets that went out of screen
        self.remove_bullets()

    def hit(self):
        """
        Check if the snake hit the food
        """
        # Predict next position of snake's head
        next = self.snake.next_pos()

        # Compute distance between snake (head) and food
        d2 = (next[0]-self.food.pos[0])**2+(next[1]-self.food.pos[1])**2

        if(d2 < self.d2):
            return True
        else:
            return False

    def bullet_hit(self):
        """
        Check if any bullet gets the target
        """

        b_hit = False
        idx = -1

        for i,b in enumerate(self.bullets):
            dx = b.pos[0] - self.food.pos[0]
            dy = b.pos[1] - self.food.pos[1]

            # Food-bullet distance
            d2 = dx**2 + dy**2

            # Check collision between bullet and food
            if(d2 < self.d2_bullet):
                b_hit = True
                idx = i

        return b_hit, idx

    def rock_hit(self):
        """
        Check if the snake hit a rock
        """
        # Predict next position of snake's head
        next = self.snake.pos_list[0]

        for r in self.rocks:
            # Compute distance between snake (head) and food
            d2 = (next[0] - r.pos[0]) ** 2 + (next[1] - r.pos[1]) ** 2

            if (d2 < self.d2):
                return True

        return False

    def bullet_rock_hit(self):
        """
        Check collision between bullets and rocks
        """

        # Indices of bullet hitting rocks (allows multiple collisions)
        idx_list = []

        for idx,b in enumerate(self.bullets):
            for r in self.rocks:
                next = b.next()

                # Compute distance between bullet and rock
                d2 = (r.pos[0]-next[0])**2+(r.pos[1]-next[1])**2

                if(d2 < self.d2_bullet):
                    idx_list.append(idx)

        if len(idx_list)>0: # At leas one collision detected
            return True, idx_list
        else: # No collisions
            return False, -1

    def bullet_snake_hit(self):
        """
        Check collision between bullet and snake 
        """
        for b in self.bullets:

            for pos in self.snake.pos_list:
                # Snake-bullet distance
                d2 = (pos[0]-b.pos[0])**2+(pos[1]-b.pos[1])**2

                # Chek if the bullet bounced already
                # (Bullet just shooted can be close to the snake head!)
                if (d2 < self.d2_bullet and b.bounced):
                    return True

        return False


    def remove_bullets(self):
        """
        Remove bullets out of screen
        """

        bullets_on_screen = []

        # Check which bullet is still on screen
        for i,b in enumerate(self.bullets):
            if(not self.out_of_screen(b.pos)):
                bullets_on_screen.append(b)

        # Save only bullets on screen
        self.bullets = bullets_on_screen

    def out_of_screen(self,pos):
        """
        Determine if POS is out of screen
        """
        if (pos[0] < 0):
            return True
        elif(pos[0] > self.width):
            return True
        elif(pos[1] < 0):
            return True
        elif(pos[1] > self.height):
            return True

        return False

    def on_key_press(self,symbol,modifiers):
        """
        Control snake with arrow keys (no inversion allowed) and shoot
        """

        # Control snake
        if symbol == key.RIGHT:
            if(self.snake.dir_list[0][0] != -1):
                self.snake.dir_list[0][0] = 1
                self.snake.dir_list[0][1] = 0
        elif symbol == key.UP:
            if (self.snake.dir_list[0][1] != -1):
                self.snake.dir_list[0][0] = 0
                self.snake.dir_list[0][1] = 1
        elif symbol == key.DOWN:
            if (self.snake.dir_list[0][1] != 1):
                self.snake.dir_list[0][0] = 0
                self.snake.dir_list[0][1] = -1
        elif symbol == key.LEFT:
            if (self.snake.dir_list[0][0] != 1):
                self.snake.dir_list[0][0] = -1
                self.snake.dir_list[0][1] = 0

        # Shoot bullet
        if symbol == key.SPACE:
            self.bullets.append(Bullet(self.snake.pos_list[0][:],
                                           1.2*self.snake.speed*np.array(self.snake.dir_list[0][:])))

            if(self.sounds):
                self.shot.play()

if __name__ == '__main__':
    gui = GUI(25,TMCS=True,nobstacles=3)
    pyglet.clock.schedule_interval(gui.update, 1/10.)
    pyglet.app.run()