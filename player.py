import pygame

class Player:
    WIDTH = 20
    HEIGHT = 30
    COLOR = (200, 50, 50)

    SPEED = 10
    GRAVITY = 1/5
    MAX_FALL_SPEED = 30

    def __init__(self):
        self.rect = pygame.Rect((0, 0), (self.WIDTH, self.HEIGHT))
        self.vx = 0
        self.vy = 0
        self.fall_count = 0

    def move(self, move_inputs):
        self.vx = 0
        if self.rect.y < 570:
            self.fall_count += 1
        else:
            self.fall_count = 0
        self.vy = min(self.vy + self.fall_count * self.GRAVITY, self.MAX_FALL_SPEED)

        if move_inputs[pygame.K_a]:
            self.vx += -self.SPEED

        if move_inputs[pygame.K_d]:
            self.vx += self.SPEED

        if move_inputs[pygame.K_w] or move_inputs[pygame.K_SPACE]:
            if self.rect.y == 570:
                self.vy -= self.SPEED

        self.rect.x += self.vx
        self.rect.y += self.vy
        self.rect.y = min(self.rect.y, 570)