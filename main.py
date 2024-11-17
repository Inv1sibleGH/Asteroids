import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scoreboard import Scoreboard
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    delta = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (updatable,drawable,bullets)
    AsteroidField.containers = (updatable)
    pl = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill("black")
        for upd in updatable:
            upd.update(dt)
        for dra in drawable:
            dra.draw(screen) 
        for ast in asteroids:
            if ast.collision(pl):
                print("Game over !")
                print(f"Score: {Scoreboard.score}")
                sys.exit()
            for bullet in bullets:
                if ast.collision(bullet):
                    ast.split()
                    bullet.kill()

        
        pygame.display.flip()
        dt = delta.tick(60)/1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()