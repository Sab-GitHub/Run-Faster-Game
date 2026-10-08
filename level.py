import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SKIP_CHARS = {'|', ' '}
LVL_CHARS = {
    'start': '(',
    'end': ')',
    'platform': '-'
}

def get_level(file_path):
    with open(file_path, 'r') as f:
        level = f.read()
    layers = level.splitlines()
    return layers

def load_level(width, height, layers):
    surface = pygame.Surface((width, height))
    surface.fill((0, 0, 0))

    row_height = height // len(layers)
    col_width = width // len(layers[0])

    platforms = []
    for row in range(len(layers)):
        for col in range(len(layers[0])):
            if layers[row][col] not in SKIP_CHARS:
                x = col * col_width
                y = row * row_height

                if layers[row][col] == LVL_CHARS['platform']:
                    platform = pygame.rect.Rect((x, y), (col_width, row_height))
                    platforms.append(platform)
                    pygame.draw.rect(surface, WHITE, platform)

                elif layers[row][col] == LVL_CHARS['start']:
                    start = (x + col_width // 2, y + row_height // 2)
                    pygame.draw.rect(surface, GREEN, (x, y, col_width, row_height))

                elif layers[row][col] == LVL_CHARS['end']:
                    end_block = pygame.rect.Rect((x, y), (col_width, row_height))
                    pygame.draw.rect(surface, RED, end_block)

    return surface, platforms, start, end_block
