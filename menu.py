import pygame
from pathlib import Path

pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode((1000, 600))

LVL_FOLDER = Path('levels')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def get_lvl_rect_img(win_width, win_height):
    lvl_names = [f.stem for f in LVL_FOLDER.iterdir() if f.is_file()]

    cols = 3
    rows = len(lvl_names) // cols + (1 if len(lvl_names) % cols > 0 else 0)

    # Creating rects for pos of lvl_imgs
    col_size = win_width / cols
    row_size = win_height / rows
    lvl_img_width = col_size * 0.5
    lvl_img_height = row_size * 0.5

    lvl_rects = []
    for i in range(rows):
        for j in range(cols):
            x = round(j * col_size + lvl_img_width / 2)
            y = round(i * row_size + lvl_img_height / 2)
            rect = pygame.Rect((x, y), (lvl_img_width, lvl_img_height))
            lvl_rects.append(rect)

    # Creating font surfaces.
    font_size = round((lvl_img_width + lvl_img_height) / 8)
    font = pygame.font.SysFont('Courier', font_size)
    font_imgs = []
    for lvl_name in lvl_names:
        font_img = font.render(lvl_name, True, BLACK, WHITE)
        font_imgs.append(font_img)

    return lvl_rects, font_imgs

def create_menu_surface(win_width, win_height):
    lvl_rects, font_imgs = get_lvl_rect_img(win_width, win_height)

    for i in range(len(font_imgs)):
        pygame.draw.rect(WIN, WHITE, lvl_rects[i])

        font_rect = font_imgs[i].get_rect(center=lvl_rects[i].center)
        WIN.blit(font_imgs[i], font_rect)

create_menu_surface(1000, 600)

clock = pygame.time.Clock()
while True:
    pygame.display.flip()
    clock.tick(10)