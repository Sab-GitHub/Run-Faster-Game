import pygame

import ui
import level
from player import Player
from timer import Timer

pygame.init()

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Run Faster Game')

FPS = 120

BLACK = (0, 0, 0)

# Level content
layers, at, pb = level.get_level('levels/l3.txt')
ui_height = level.get_ui_height(HEIGHT)
lvl_surface, platforms, (player_x, player_y), end_block = level.load_level(WIDTH, HEIGHT - ui_height, layers )

# UI
pause_btn = ui.Pause_btn(WIDTH, ui_height)
records = ui.Records(WIDTH, ui_height, at, pb)

timer = Timer(WIDTH, ui_height)
player = Player(player_x, player_y)

clock = pygame.time.Clock()
prev_time = pygame.time.get_ticks()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key in player.CONTROLS.values():
                timer.timer_started = True

            elif event.key == pygame.K_r:
                player.reset(player_x, player_y)
                timer.reset()

    if timer.timer_started and not timer.timer_started_once:
        timer.timer_start = pygame.time.get_ticks()
        timer.timer_started_once = True

    # Delta time calculation
    now_time = pygame.time.get_ticks()
    dt = now_time - prev_time
    prev_time = now_time

    # Calculating player pos this way gives the most accurate movement with different FPS/lag.
    player.move(pygame.key.get_pressed(), dt/2, platforms, True) # Updating first half of dt.
    player.move(pygame.key.get_pressed(), dt/2, platforms, False) # Updating second half of dt without updating position.
    player.animate()

    timer.update_timer(now_time, player, end_block)

    WIN.fill(BLACK)
    WIN.blit(lvl_surface, (0, ui_height))
    WIN.blit(player.surface, (player.rect.x, player.rect.y+ ui_height))
    WIN.blit(timer.box, timer.box_pos)
    pause_btn.draw(WIN)
    records.draw(WIN, WIDTH, ui_height)

    pygame.display.flip()
    clock.tick(FPS) 

pygame.quit()