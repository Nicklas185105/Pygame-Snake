"""Snake entity module."""

import pygame

class Snake():
    """The Snake class represents the snake entity in the game."""
    def __init__(self, initial_position, cell_size, color):
        self.body = [pygame.Rect(initial_position[0], initial_position[1], cell_size, cell_size)]
        self.direction = pygame.Vector2(1, 0)  # Start moving to the right
        self.cell_size = cell_size
        self.color = color

    def move(self):
        """Move the snake by adding a new head in the direction of movement."""
        # Add a new head in the direction of movement
        new_head = self.body[0].copy()
        new_head.x += int(self.direction.x * self.cell_size)
        new_head.y += int(self.direction.y * self.cell_size)
        self.body.insert(0, new_head)
        # Remove the tail to maintain length
        self.body.pop()

    def grow(self):
        """Grow the snake by adding a new segment without removing the tail."""
        # Add a new segment without removing the tail
        new_head = self.body[0].copy()
        new_head.x += int(self.direction.x * self.cell_size)
        new_head.y += int(self.direction.y * self.cell_size)
        self.body.insert(0, new_head)

    def draw(self, screen):
        """Draw the snake on the screen."""
        for segment in self.body:
            pygame.draw.rect(screen, self.color, segment)

    def check_collision(self):
        """Check if the snake collides with the screen boundaries or itself."""
        # Check if the head collides with the body
        head = self.body[0]
        return any(head.colliderect(segment) for segment in self.body[1:])
