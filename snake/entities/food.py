"""Food class for the snake game."""

import random
import pygame

class Food:
    """The Food class represents the food entity in the game."""
    def __init__(self, screen_width, screen_height, cell_size, color):
        self.cell_size = cell_size
        self.color = color
        self.rect = pygame.Rect(0, 0, cell_size, cell_size)
        self.respawn(screen_width, screen_height)

    def respawn(self, screen_width, screen_height):
        """Respawn the food at a random location on the screen."""
        self.rect.x = random.randint(0, (screen_width // self.cell_size) - 1) * self.cell_size
        self.rect.y = random.randint(0, (screen_height // self.cell_size) - 1) * self.cell_size

    def draw(self, screen):
        """Draw the food on the screen."""
        pygame.draw.rect(screen, self.color, self.rect)
