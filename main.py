import pygame
from constants import *

pygame.init()


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        

if __name__ == "__main__":
    main()


    screen.fill((0,0,0))
    pygame.display.flip()





