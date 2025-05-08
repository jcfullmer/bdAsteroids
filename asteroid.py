import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20,50)
            as_velocity1 = self.velocity.rotate(new_angle)
            as_velocity2 = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            as1 = Asteroid(self.position.x, self.position.y, new_radius)
            as2 = Asteroid(self.position.x, self.position.y, new_radius)
            as1.velocity = as_velocity1 * 1.2
            as2.velocity = as_velocity2 * 1.2


