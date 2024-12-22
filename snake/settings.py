"""Settings for the Snake game."""

from core.settings import Settings

class SnakeSettings(Settings):
    """A class to store all settings for the Snake game."""

    # SCREEN_WIDTH = 800
    # SCREEN_HEIGHT = 600
    # FPS = 60
    # COLORS = {
    #     "background": (0, 0, 0),
    #     "player": (255, 255, 255),
    # }
    CELL_SIZE = 20
    COLORS = {
        "background": (0, 0, 0),
        "snake": (0, 255, 0),
        "food": (255, 0, 0),
        "score_text": (255, 255, 255),
    }
    SCORE = 0

    def __init__(self):
        self.game_over_size = 48

        self.snake_direction = 'right'
        self.snake_x = 0
        self.snake_y = 0

        self.food_x = 0
        self.food_y = 0

        self.score = 0

        self.game_over = False

        self.snake_body = []
        self.snake_body_length = 1

        self.snake_body_positions = []

        self.snake_body_positions.append((self.snake_x, self.snake_y))

        self.snake_body_positions = self.snake_body_positions[-self.snake_body_length:]

        self.snake_body.append((self.snake_x, self.snake_y))

        self.snake_body = self.snake_body[-self.snake_body_length:]

        self.snake_body_positions = self.snake_body_positions[-self.snake_body_length:]

        self.snake_body = self.snake_body[-self.snake_body_length:]

        self.snake_body_positions = self.snake_body_positions[-self.snake_body_length:]

        self.snake_body = self.snake_body[-self.snake_body_length:]

        self.snake_body_positions = self.snake_body_positions[-self.snake_body_length:]

        self.snake_body = self.snake_body[-self.snake_body_length:]

        self.snake_body_positions = self.snake_body_positions[-self.snake_body_length:]

        self.snake_body = self.snake_body[-self.snake_body_length:]

        self.snake_body_positions = self.snake_body_positions[-self.snake_body_length:]

        self.snake_body = self
