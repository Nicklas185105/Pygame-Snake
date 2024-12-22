"""Main module of the game. It initializes the game and runs the main loop."""

from core import Game, SceneManager
from snake.settings import SnakeSettings
from snake.scenes.main_menu import MainMenu

if __name__ == "__main__":
    import pygame
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member
    screen = pygame.display.set_mode((SnakeSettings.SCREEN_WIDTH, SnakeSettings.SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    manager = SceneManager(MainMenu(screen))
    game = Game(screen, 10)
    game.run(manager)
    # pylint: disable=no-member
    pygame.quit()
    # pylint: enable=no-member
