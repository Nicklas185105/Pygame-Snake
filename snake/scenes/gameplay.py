"""Gameplay scene module."""

import pygame
# pylint: disable=no-name-in-module
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_s, K_a, K_d
# pylint: enable=no-name-in-module
from core.scene import Scene
from core.utils import check_collision
from snake.entities.snake import Snake
from snake.entities.food import Food
from snake.settings import SnakeSettings

class Gameplay(Scene):
    """The Gameplay scene class."""

    def __init__(self, screen):
        super().__init__(screen)
        self.snake = Snake(
            (SnakeSettings.CELL_SIZE * 5, SnakeSettings.CELL_SIZE * 5),
            SnakeSettings.CELL_SIZE,
            SnakeSettings.COLORS["snake"],
        )
        self.food = Food(
            SnakeSettings.SCREEN_WIDTH,
            SnakeSettings.SCREEN_HEIGHT,
            SnakeSettings.CELL_SIZE,
            SnakeSettings.COLORS["food"],
        )
        self.font = pygame.font.Font(None, 36)  # Font for rendering the score

    def update(self, input_manager):
        # Handle directional input
        if (input_manager.is_pressed(K_UP) or input_manager.is_pressed(K_w)) and self.snake.direction.y == 0:
            self.snake.direction = pygame.Vector2(0, -1)
        elif (input_manager.is_pressed(K_DOWN) or input_manager.is_pressed(K_s)) and self.snake.direction.y == 0:
            self.snake.direction = pygame.Vector2(0, 1)
        elif (input_manager.is_pressed(K_LEFT) or input_manager.is_pressed(K_a)) and self.snake.direction.x == 0:
            self.snake.direction = pygame.Vector2(-1, 0)
        elif (input_manager.is_pressed(K_RIGHT) or input_manager.is_pressed(K_d)) and self.snake.direction.x == 0:
            self.snake.direction = pygame.Vector2(1, 0)

        self.snake.move()

        # Check collisions
        if check_collision(self.snake.body[0], self.food.rect):
            self.snake.grow()
            self.food.respawn(SnakeSettings.SCREEN_WIDTH, SnakeSettings.SCREEN_HEIGHT)
            SnakeSettings.SCORE += 1  # Increase score on food collision

        self._check_wall_collision()
        self._check_self_collision()

    def _check_wall_collision(self):
        head = self.snake.body[0]
        if (
            head.x < 0
            or head.x >= SnakeSettings.SCREEN_WIDTH
            or head.y < 0
            or head.y >= SnakeSettings.SCREEN_HEIGHT
        ):
            print("Snake hit the wall! Game over.")
            self.running = False

    def _check_self_collision(self):
        head = self.snake.body[0]
        if any(check_collision(head, segment) for segment in self.snake.body[1:]):
            print("Snake collided with itself! Game over.")
            self.running = False

    def render(self):
        # Clear the screen with the background color
        self.screen.fill(SnakeSettings.COLORS["background"])
        # Draw the snake and the food
        self.snake.draw(self.screen)
        self.food.draw(self.screen)

        # Render the score
        score_text = self.font.render(f"Score: {SnakeSettings.SCORE}",
                                        True, SnakeSettings.COLORS["score_text"])
        self.screen.blit(score_text, (10, 10))  # Top-left corner
