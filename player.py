import pygame
from constants import (
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    PLAYER_SPEED,
    JUMP_STRENGTH,
    GRAVITY,
    MAX_FALL_SPEED,
    BLUE,
)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = PLAYER_SPEED

    def jump(self):
        if self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y += GRAVITY
        if self.vel_y > MAX_FALL_SPEED:
            self.vel_y = MAX_FALL_SPEED

    def update(self, platforms):
        self.handle_input()
        self.apply_gravity()

        # Horizontal movement + collision
        self.rect.x += self.vel_x
        self._collide(platforms, dx=self.vel_x, dy=0)

        # Vertical movement + collision
        self.rect.y += self.vel_y
        self.on_ground = False
        self._collide(platforms, dx=0, dy=self.vel_y)

    def _collide(self, platforms, dx, dy):
        for platform in pygame.sprite.spritecollide(self, platforms, False):
            if dx > 0:
                self.rect.right = platform.rect.left
            if dx < 0:
                self.rect.left = platform.rect.right
            if dy > 0:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
                self.on_ground = True
            if dy < 0:
                self.rect.top = platform.rect.bottom
                self.vel_y = 0
