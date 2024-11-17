import pygame
from constants import *
from circleshape import *
class Shot(CircleShape):
    def __init__(self,x,y,radius,direction):
        super().__init__(x,y,radius)
        self.direction = direction
        self.velocity = pygame.Vector2(0,1).rotate(self.direction)*PLAYER_SHOOT_SPEED
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position += self.velocity * dt