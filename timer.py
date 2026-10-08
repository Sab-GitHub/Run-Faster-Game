import pygame
import time

pygame.font.init()

class Timer:
    def __init__(self, win_width, win_height):
        self.timer_start = time.time()
        self.lvl_not_ended = True

        self.box_width = win_width // 5
        self.box_height = win_height // 10
        self.box_pos = (win_width // 2 - self.box_width // 2, win_height - self.box_height)
        self.box = pygame.Surface((self.box_width, self.box_height))
        self.box_color = (0, 0, 255)

        self.text_font_size = (win_width + win_height) // 35
        self.font = pygame.font.SysFont('Courier', self.text_font_size)

    def update_timer_text(self):
        curr_time = time.time()
        timer_curr = curr_time - self.timer_start
        timer_img = self.font.render(f'{timer_curr:.2f}', True, (255, 255, 255))

        self.box.fill(self.box_color)
        x = self.box.get_width() // 2 - timer_img.get_width() // 2
        y = self.box.get_height() // 2 - timer_img.get_height() // 2
        self.box.blit(timer_img, (x, y))

    def update_timer(self, player, end_block):
        if self.lvl_not_ended:
            if player.rect.colliderect(end_block):
                timer_end = time.time()
                self.lvl_not_ended = False
                return

            else:
                self.update_timer_text()