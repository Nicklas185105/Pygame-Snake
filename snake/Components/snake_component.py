from engine import Component, EventBus
from engine.components import Transform

from snake.settings import DIRECTION_RIGHT, SCREEN_WIDTH, GRID_SIZE, SCREEN_HEIGHT


class SnakeComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = DIRECTION_RIGHT
        self.food = None
        self.score = 0
        self.alive = True

    def update(self, delta_time: float):
        if not self.alive:
            return

        # Move the snake
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])

        # Check collisions
        if (new_head in self.body or
            new_head[0] < 0 or new_head[1] < 0 or
            new_head[0] >= SCREEN_WIDTH // GRID_SIZE or
            new_head[1] >= SCREEN_HEIGHT // GRID_SIZE):
            self.alive = False
            EventBus.publish("game_over")
            return

        # Add the new head
        self.body.insert(0, new_head)

        # Check if food is eaten
        if self.food and new_head == self.food.get_component(Transform).position:
            self.score += 1
            EventBus.publish("food_eaten")
        else:
            self.body.pop()

    def change_direction(self, direction):
        if (direction[0] != -self.direction[0] and direction[1] != -self.direction[1]):
            self.direction = direction
