import random
import pygame
from constants import *
from circleshape import *
from scoreboard import Scoreboard
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            Scoreboard.score += 1
            return
        else:
            randrotation = random.uniform(20,50)
            vector1 = self.velocity.rotate(randrotation)
            vector2 = self.velocity.rotate(-randrotation)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            firsthalf = Asteroid(self.position.x,self.position.y,newRadius)
            secondhalf = Asteroid(self.position.x,self.position.y,newRadius)
            firsthalf.velocity = vector1 * 1.2
            secondhalf.velocity = vector2 * 1.2
        