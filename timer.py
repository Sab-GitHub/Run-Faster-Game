import pygame

pygame.font.init()

class Timer:
    def __init__(self, win_width, win_height):
        self.lvl_started = False
        self.lvl_not_ended = True

        self.box_width = win_width // 5
        self.box_height = win_height // 10
        self.box_pos = (win_width // 2 - self.box_width // 2, win_height - self.box_height)
        self.box = pygame.Surface((self.box_width, self.box_height))
        self.box_color = (0, 0, 255)

        self.text_font_size = (win_width + win_height) // 35
        self.font = pygame.font.SysFont('Courier', self.text_font_size)
        self.update_timer_text('0.00')

    def update_timer_text(self, timer_text):
        self.box.fill(self.box_color)
        self.timer_img = self.font.render(timer_text, True, (255, 255, 255))

        font_size_x, font_size_y = self.font.size(timer_text)
        timer_img_x = self.box_width // 2 - font_size_x // 2
        timer_img_y = self.box_height // 2 - font_size_y // 2

        self.box.blit(self.timer_img, (timer_img_x, timer_img_y))

    def start_timer(self):
        self.timer_start = pygame.time.get_ticks()

    def update_timer(self, player, end_block):
        if self.lvl_started and self.lvl_not_ended:
            if player.rect.colliderect(end_block):
                self.lvl_not_ended = False

            timer_curr = (pygame.time.get_ticks() - self.timer_start) / 1000 # Millseconds / 1000 = Seconds
            self.update_timer_text(f'{timer_curr:.2f}')