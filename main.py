import pygame

import level
from player import Player
from timer import Timer

pygame.init()

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Run Faster Game')

FPS = 60

player = Player()

layers = level.get_level('levels/l2.txt')
lvl_surface, platforms, (player.rect.x, player.rect.y), end_block = level.load_level(WIDTH, HEIGHT, layers)
timer = Timer(WIDTH, HEIGHT)

clock = pygame.time.Clock()
dt = 1 / FPS

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key in player.CONTROLS.values() and not timer.lvl_started:
                timer.start_timer()
                timer.lvl_started = True

    player.move(pygame.key.get_pressed(), dt, platforms)
    player.animate()
    timer.update_timer(player, end_block)

    WIN.blit(lvl_surface, (0, 0))
    WIN.blit(timer.box, timer.box_pos)
    # pygame.draw.rect(WIN, player.COLOR, player.rect)
    WIN.blit(player.surface, player.rect)

    pygame.display.flip()
    dt = clock.tick(FPS) 
    print(dt)

pygame.quit()