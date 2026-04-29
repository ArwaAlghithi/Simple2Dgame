import pygame
import random
from constants import *

class Shape:
    def __init__(self):
        self.type = random.randint(0, 2)
        self.size = 30
        self.x = random.randint(0, WIDTH - self.size)
        self.y = -self.size
        self.color = SHAPE_COLOR_4
        self.speed = SHAPE_SPEED

    def draw(self, screen):
        if self.type == 0: 
            pygame.draw.rect(screen, SHAPE_COLOR_1, (self.x, self.y, self.size, self.size))
        elif self.type == 1: 
            pygame.draw.circle(screen, SHAPE_COLOR_2, (self.x + self.size//2, self.y + self.size//2), self.size//2)
        elif self.type == 2: 
            points = [(self.x, self.y + self.size), 
                      (self.x + self.size // 2, self.y), 
                      (self.x + self.size, self.y + self.size)]
            pygame.draw.polygon(screen, SHAPE_COLOR_3, points)

    def fall(self):
        self.y += self.speed

