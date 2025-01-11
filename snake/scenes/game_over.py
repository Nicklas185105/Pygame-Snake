import pygame
from engine import Scene, Canvas, Style, UIButton, SceneManager


class GameOverScene(Scene):
    def __init__(self):
        super().__init__("GameOverScene")
        self.canvas = Canvas(pygame.display.get_surface())
        self.style = Style(background_color=(50, 50, 50), border_color=(255, 255, 255), text_color=(255, 255, 255))

        restart_button = UIButton(200, 150, 200, 50, "Restart", lambda: SceneManager.load_scene("GameScene"), self.style)
        quit_button = UIButton(200, 250, 200, 50, "Quit", lambda: pygame.quit(), self.style)

        self.canvas.add_element(restart_button)
        self.canvas.add_element(quit_button)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.canvas.render()
