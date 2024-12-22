"""Settings for the Snake game."""

from core.settings import Settings

# pylint: disable=too-few-public-methods
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
