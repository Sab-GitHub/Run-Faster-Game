import pygame

def get_level(file_path):
    with open(file_path, 'r') as f:
        level = f.read()
    layers = level.splitlines()
    return layers

def render_level(width, height, layers):
    surface = pygame.Surface((width, height))
    surface.fill((0, 0, 0))

    row_height = height // len(layers)
    col_width = width // len(layers[0])
    for row in range(len(layers)):
        for col in range(len(layers[0])):
            if layers[row][col] == '-':
                x = col * col_width
                y = row * row_height
                pygame.draw.rect(surface, (255, 255, 255), (x, y, col_width, row_height))

    return surface
