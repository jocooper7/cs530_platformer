import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GROUND_HEIGHT,
    PLATFORM_COLOR,
)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=PLATFORM_COLOR):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))


def load_level_1():
    """
    Returns a sprite group of platforms for level 1.
    Positions are hardcoded for the proof-of-concept stage.
    """
    platforms = pygame.sprite.Group()

    # Ground
    ground = Platform(0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT)
    platforms.add(ground)

    # Floating platforms
    platforms.add(Platform(150, 450, 120, 20))
    platforms.add(Platform(350, 350, 120, 20))
    platforms.add(Platform(550, 250, 120, 20))

    return platforms
