import pygame

class Player:
    WIDTH = 20
    HEIGHT = 30
    COLOR = (200, 0, 200)

    SPEED = 5
    GRAVITY = 1/10
    MAX_FALL_SPEED = 30
    JUMP_FORCE = 10

    def __init__(self):
        self.rect = pygame.Rect((0, 0), (self.WIDTH, self.HEIGHT))
        self.vx = 0
        self.vy = 0
        self.fall_count = 0
        self.is_grounded = False

    def check_collision(self, platforms, axis):
        if axis == 'x':
            for platform in platforms:
                if self.rect.colliderect(platform):
                    if self.vx > 0: # Going right
                        self.rect.right = platform.left

                    elif self.vx < 0: # Going left
                        self.rect.left = platform.right

        elif axis == 'y':
            self.is_grounded = False
            for platform in platforms:
                if self.rect.colliderect(platform):
                    if self.vy > 0: # Going down
                        self.rect.bottom = platform.top
                        self.is_grounded = True

                    elif self.vy < 0: # Going up
                        self.rect.top = platform.bottom

    def move(self, move_inputs, platforms):
        self.vx = 0

        if self.is_grounded:
            self.fall_count = 0
            self.vy = 0
        else:
            self.fall_count += 1
            self.vy = min(self.vy + self.fall_count * self.GRAVITY, self.MAX_FALL_SPEED)            

        if move_inputs[pygame.K_a]:
            self.vx += -self.SPEED

        if move_inputs[pygame.K_d]:
            self.vx += self.SPEED

        if move_inputs[pygame.K_w] or move_inputs[pygame.K_SPACE]:
            if self.is_grounded:
                self.vy -= self.JUMP_FORCE

        self.rect.y += self.vy
        self.check_collision(platforms, 'y')

        self.rect.x += self.vx
        self.check_collision(platforms, 'x')