import pygame
from engine import Scene, GameObject, EventBus, SceneManager
from engine.components import Transform

from snake.Components.snake_component import SnakeComponent
from snake.ScriptableObjects.food_scriptable_object import FoodScriptableObject
from snake.settings import COLOR_BACKGROUND, COLOR_SNAKE, GRID_SIZE, COLOR_FOOD


class GameScene(Scene):
    def __init__(self):
        super().__init__("GameScene")

        # Snake GameObject
        self.snake = GameObject("Snake")
        self.snake_component = self.snake.add_component(SnakeComponent)

        # Food ScriptableObject
        self.food_script = FoodScriptableObject("apple", self.snake_component)

        # Food GameObject
        self.food = GameObject("Food")
        self.food_transform = self.food.add_component(Transform)

        # Initialize food position
        self.food_transform.position = self.food_script.position

        self.add_game_object(self.snake)
        self.add_game_object(self.food)

        # Event subscriptions
        EventBus.subscribe("food_eaten", self.on_food_eaten)
        EventBus.subscribe("game_over", self.on_game_over)

    def on_food_eaten(self):
        """
        Relocate food when eaten.
        """
        self.food_script.relocate()
        self.food_transform.position = self.food_script.position

    def on_game_over(self):
        SceneManager.load_scene("GameOverScene")

    def update(self, delta_time):
        super().update(delta_time)
        if self.snake_component.alive:
            self.snake_component.update()

    def render(self, screen):
        screen.fill(COLOR_BACKGROUND)

        # Render snake
        for segment in self.snake_component.body:
            pygame.draw.rect(screen, COLOR_SNAKE,
                             (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Render food
        food_position = self.food_transform.position
        pygame.draw.rect(screen, COLOR_FOOD,
                         (food_position[0] * GRID_SIZE, food_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
