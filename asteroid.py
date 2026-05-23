import pygame
import random
from logger import log_state, log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw (self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            astr1 = self.velocity.rotate(random_angle)
            astr2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            astroid1.velocity = astr1 * 1.2
            astroid2.velocity = astr2 * 1.2

