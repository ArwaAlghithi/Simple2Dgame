import pygame
import sys
import random
from constants import *
from classes.player import *
from classes.shapes import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Catcher")
clock = pygame.time.Clock()

bg_image = pygame.image.load("assets/bg.jpg")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT)) 

player = Player()
shapes_list = []
score = 0
font = pygame.font.SysFont("monospace", 30, bold=True) 

score_text = font.render(f"SCORE: {score}", True, BLACK)
screen.blit(score_text, (20, 20))

def draw_grid(screen):
    for x in range(0, WIDTH, 40): 
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 40): 
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))
    GRID_COLOR = (220, 220, 220) 
    pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))


while True:
    screen.blit(bg_image, (0, 0))
    draw_grid(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player.move(keys) 

    if random.randint(1, 40) == 1: 
        shapes_list.append(Shape())

    for shape in shapes_list[:]:
        shape.fall()
        shape.draw(screen)

        player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
        shape_rect = pygame.Rect(shape.x, shape.y, shape.size, shape.size)

        if player_rect.colliderect(shape_rect):
            shapes_list.remove(shape)
            score += 1


        elif shape.y > HEIGHT:
            shapes_list.remove(shape)

    player.draw(screen)
    score_surface = font.render(f"SCORE: {score}", True, BLACK)
    screen.blit(score_surface, (20, 20))
    
    pygame.display.flip()
    clock.tick(FPS) 
