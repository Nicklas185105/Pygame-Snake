"""Main menu scene."""

import pygame
from engine import Scene, Canvas, Style, UIButton, SceneManager

from snake.scenes.game_scene import GameScene


class MainMenuScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__("MainMenuScene", screen)
        print(pygame.display.get_surface())
        self.style = Style(background_color=(50, 50, 50), border_color=(255, 255, 255), text_color=(255, 255, 255))

        start_button = UIButton(200, 150, 200, 50, "Start Game", lambda: SceneManager.load_scene(GameScene(screen)), self.style)
        quit_button = UIButton(200, 250, 200, 50, "Quit", lambda: pygame.quit(), self.style)

        self.canvas.add_element(start_button)
        self.canvas.add_element(quit_button)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.canvas.render()
