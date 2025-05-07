import pygame
from constants import *
from player import Player

updatable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()
Player.containers = (updatable_group, drawable_group)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable_group.update(dt)
        screen.fill("black")
        for i in drawable_group:
            i.draw(screen)
        pygame.display.flip()

    
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
