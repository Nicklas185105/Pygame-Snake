import random

from engine import ScriptableObject

from snake.settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE


class FoodScriptableObject(ScriptableObject):
    """
    A scriptable object for managing food logic.
    """
    def __init__(self, name, snake):
        """
        Args:
            snake (SnakeComponent): The SnakeComponent instance to check collisions.
        """
        super().__init__(name)
        self.snake = snake
        self.position = (0, 0)  # Food's position on the grid
        self.relocate()

    def relocate(self):
        """
        Move the food to a random position not occupied by the snake.
        """
        while True:
            new_position = (random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1),
                            random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1))
            if new_position not in self.snake.body:
                self.position = new_position
                break
