import pygame

pygame.font.init()

class Pause_btn:
    def __init__(self, win_width, ui_height):
        self.center = (round(win_width * 0.03) , ui_height // 2)
        self.radius = round(ui_height * 0.3)

    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), self.center, self.radius)

class Records:
    def __init__(self, win_width, ui_height, at = '-', pb = '-'):
        if at == '': at = '-'
        self.at = f'Author Time: {at}'
        if pb == '': pb = '-'
        self.pb = f'Personal Best: {pb}'

        self.display_width = round(win_width * 0.3)
        self.at_display = pygame.Surface((self.display_width, ui_height // 2))
        self.pb_display = pygame.Surface((self.display_width, ui_height // 2))

        self.text_font_size = (self.display_width + ui_height // 2) // 16
        self.font = pygame.font.SysFont('Courier', self.text_font_size)

    def draw(self, win, win_width, ui_height):
        for text, display in [(self.at, self.at_display), (self.pb, self.pb_display)]:
            display.fill((255, 255, 0))
            text_img = self.font.render(text, True, (0, 0, 0))

            font_size_x, font_size_y = self.font.size(text)
            text_img_x = self.display_width // 2 - font_size_x // 2
            text_img_y = ui_height // 2 - font_size_y

            display.blit(text_img, (text_img_x, text_img_y))

        win.blit(self.at_display, (win_width - self.display_width, 0))
        win.blit(self.pb_display, (win_width - self.display_width, ui_height // 2))
