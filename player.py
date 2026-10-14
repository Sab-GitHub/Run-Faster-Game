import pygame

class Player:
    WIDTH = 30
    HEIGHT = 40
    COLOR = (200, 0, 200)

    SPEED = 0.5
    GRAVITY = 0.004
    MAX_RUN_SPEED = 0.7
    MAX_FALL_SPEED = 1.7
    JUMP_FORCE = 1.1

    CONTROLS = {
        'left': pygame.K_a,
        'right': pygame.K_d,
        'w_jump': pygame.K_w,
        'space_jump': pygame.K_SPACE
    }

    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y), (self.WIDTH, self.HEIGHT))
        self.true_x = float(x)
        self.true_y = float(y)
        self.vx = float(0)
        self.vy = float(0)
        self.is_grounded = False
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT))

        self.img = pygame.image.load('assets/s_player_idle.gif')
        self.img = pygame.transform.scale(self.img, (self.WIDTH, self.HEIGHT))

    def check_collision(self, platforms, axis):
        collision = False

        if axis == 'x':
            for platform in platforms:
                if self.rect.colliderect(platform):
                    collision = True

                    if self.vx > 0: # Going right
                        self.rect.right = platform.left

                    elif self.vx < 0: # Going left
                        self.rect.left = platform.right

        elif axis == 'y':
            self.is_grounded = False
            for platform in platforms:
                if self.rect.colliderect(platform):
                    collision = True

                    if self.vy > 0: # Going down
                        self.rect.bottom = platform.top
                        self.is_grounded = True

                    elif self.vy < 0: # Going up
                        self.rect.top = platform.bottom

        return collision

    def update_pos(self, dt, platforms):
        self.true_y += self.vy * dt
        self.rect.y = round(self.true_y)
        if self.check_collision(platforms, 'y'):
            self.true_y = float(self.rect.y)

        self.true_x += self.vx * dt
        self.rect.x = round(self.true_x)
        if self.check_collision(platforms, 'x'):
            self.true_x = float(self.rect.x)

    def move(self, move_inputs, dt, platforms, update):

        # If falling, continue adding to y vel.
        if self.is_grounded:
            self.vy = 0
        else:
            self.vy = min(self.vy +  self.GRAVITY * dt, self.MAX_FALL_SPEED)            

        # Add/subract from x vel if left or right being pressed, if not moving set vel to 0.
        if move_inputs[self.CONTROLS['left']] and not move_inputs[self.CONTROLS['right']]:
            self.vx -= self.SPEED

        elif move_inputs[self.CONTROLS['right']] and not move_inputs[self.CONTROLS['left']]:
            self.vx += self.SPEED

        else:
            self.vx = 0
        self.vx = max(min(self.vx, self.MAX_RUN_SPEED), -self.MAX_RUN_SPEED)

        jump_intent = move_inputs[self.CONTROLS['w_jump']] or move_inputs[self.CONTROLS['space_jump']]
        if jump_intent and self.is_grounded:
            self.vy -= self.JUMP_FORCE

        if update:
            self.update_pos(dt, platforms)

    def animate(self):
        self.img_boundry = self.img.get_rect()
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.img, (self.img_boundry.x, self.img_boundry.y))

    def reset(self, starting_x, starting_y):
        self.rect.x, self.rect.y = starting_x, starting_y
        self.true_x, self.true_y = float(starting_x), float(starting_y)
        self.vx = float(0)
        self.vy = float(0)
        self.is_grounded = False