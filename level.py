import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SKIP_CHARS = {'|', ' '}
LVL_CHARS = {
    'start': '(',
    'end': ')',
    'grass_block': '-'
}
lvl_img_paths = {
    # type: (file_path, (x, y), (width, height))
    'grass_block': ('assets/s_dirt_tileset.png', [(97, 95), (14, 15)])
}

def get_ui_height(win_height):
    ui_height = win_height // 10
    return ui_height

def get_level(file_path):
    with open(file_path, 'r') as f:
        level = f.read().replace('|', '')
    layers = level.splitlines()

    at = layers[0] # Author time
    pb = layers[1] # Personal best time
    return layers[2:], at, pb

def load_img(obj, width, height):
    img = pygame.image.load(lvl_img_paths[obj][0])
    img = img.subsurface(lvl_img_paths[obj][1])
    img = pygame.transform.scale(img, (width, height))
    return img

def load_level(width, height, layers):
    lvl_surface = pygame.Surface((width, height))
    lvl_surface.fill((0, 0, 0))

    row_height = height / len(layers)
    col_width = width / len(layers[0])

    platform_surface = pygame.Surface((col_width, row_height))
    platform_img = pygame.image.load('assets/s_dirt_tileset.png')
    platform_surface.blit(platform_img, (0, 0))

    platforms = []
    for row in range(len(layers)):
        for col in range(len(layers[0])):
            if layers[row][col] not in SKIP_CHARS:
                # x = int(col * col_width)
                # y = int(row * row_height)
                x = col * int(col_width)
                y = row * int(row_height)

                if layers[row][col] == LVL_CHARS['grass_block']:
                    platform = pygame.rect.Rect((x, y), (col_width, row_height))
                    platforms.append(platform)

                    img = load_img('grass_block', col_width, row_height) # Same width and height as for platform to scale size.
                    lvl_surface.blit(img, platform)

                elif layers[row][col] == LVL_CHARS['start']:
                    start = (x + col_width // 2, y + row_height // 2)
                    pygame.draw.rect(lvl_surface, GREEN, (x, y, col_width, row_height))

                elif layers[row][col] == LVL_CHARS['end']:
                    end_block = pygame.rect.Rect((x, y), (col_width, row_height))
                    pygame.draw.rect(lvl_surface, RED, end_block)

    return lvl_surface, platforms, start, end_block