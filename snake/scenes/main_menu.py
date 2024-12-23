"""Main menu scene."""

import pygame
# pylint: disable=no-name-in-module
from pygame.constants import K_RETURN
# pylint: enable=no-name-in-module
from core import Scene
from snake.scenes.gameplay import Gameplay

class MainMenu(Scene):
    """The Main Menu scene class."""

    def update(self, input_manager):
        if input_manager.is_pressed(K_RETURN):  # Check if Enter is pressed
            print("Enter pressed. Transitioning to Gameplay.")
            return Gameplay(self.screen)

        # Handle quitting via input
        # for event in pygame.event.get():
        #     if event.type == QUIT:
        #         self.running = False

    def render(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("Press Enter to Start", True, (255, 255, 255))
        self.screen.blit(text, (100, 250))
