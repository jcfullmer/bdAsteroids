import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shots import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids= pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = updatable
Shot.containers = (shots, updatable, drawable)
asteroid_field = AsteroidField()

def main():
    pygame.init()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if player.collision(asteroid):
                    print("Game Over!")
                    sys.exit()
                elif shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()

    
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
