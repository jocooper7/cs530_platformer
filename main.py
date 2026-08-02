import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    TITLE,
    SKY_BLUE,
    UI_FONT_SIZE,
    UI_MARGIN,
    UI_TEXT_COLOR,
)
from player import Player
from levels import load_level_1


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, UI_FONT_SIZE)

    platforms = load_level_1()
    player = Player(100, 100)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(platforms)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP):
                    player.jump()

        player.update(platforms)

        screen.fill(SKY_BLUE)
        all_sprites.draw(screen)

        # Render remaining life in the top-left corner.
        life_surface = font.render(
            f"Remaining Life: {player.life}", True, UI_TEXT_COLOR
        )
        screen.blit(life_surface, (UI_MARGIN, UI_MARGIN))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
