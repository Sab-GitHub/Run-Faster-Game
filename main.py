import pygame

import level
from player import Player

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Run Faster Game')

FPS = 30

player = Player()

layers = level.get_level('levels/l1.txt')
surface = level.render_level(WIDTH, HEIGHT, layers)

clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.move(pygame.key.get_pressed())

    WIN.blit(surface, (0, 0))
    pygame.draw.rect(WIN, player.COLOR, player.rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()