import pygame
from constants import *

class Player:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = (WIDTH // 2) - (self.width // 2)
        self.y = HEIGHT - 50
        self.color = PLAYER_COLOR
        self.speed = PLAYER_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, keys):
      if keys[pygame.K_LEFT] and self.x > 0:
        self.x -= self.speed
      if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
        self.x += self.speed

