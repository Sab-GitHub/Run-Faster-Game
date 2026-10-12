import pygame

class Player:
    WIDTH = 30
    HEIGHT = 40
    COLOR = (200, 0, 200)

    SPEED = 0.5
    GRAVITY = 0.0001
    MAX_FALL_SPEED = 3
    JUMP_FORCE = 0.1

    CONTROLS = {
        'left': pygame.K_a,
        'right': pygame.K_d,
        'w_jump': pygame.K_w,
        'space_jump': pygame.K_SPACE
    }

    def __init__(self):
        self.rect = pygame.Rect((0, 0), (self.WIDTH, self.HEIGHT))
        self.vx = 0
        self.vy = 0
        self.fall_count = 0
        self.is_grounded = False
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT))

        self.img = pygame.image.load('assets/s_player_idle.gif')
        self.img = pygame.transform.scale(self.img, (self.WIDTH, self.HEIGHT))

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

    def move(self, move_inputs, dt, platforms):
        self.vx = 0

        if self.is_grounded:
            self.fall_count = 0
            self.vy = 0
        else:
            self.fall_count += 1
            self.vy = min(self.vy + self.fall_count * self.GRAVITY, self.MAX_FALL_SPEED)            

        if move_inputs[self.CONTROLS['left']]:
            self.vx += -self.SPEED

        if move_inputs[self.CONTROLS['right']]:
            self.vx += self.SPEED

        if move_inputs[self.CONTROLS['w_jump']] or move_inputs[self.CONTROLS['space_jump']]:
            if self.is_grounded:
                self.vy -= self.JUMP_FORCE

        self.rect.y += round(self.vy * dt)
        self.check_collision(platforms, 'y')

        self.rect.x += round(self.vx * dt)
        self.check_collision(platforms, 'x')

    def animate(self):
        self.img_boundry = self.img.get_rect()
        self.surface.blit(self.img, (self.img_boundry.x, self.img_boundry.y))