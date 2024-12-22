# Pygame Snake Game

## Overview

This project is a simple Snake game built using Pygame and a custom modular core designed to manage scenes, input, and game logic efficiently. The game demonstrates the use of modular design for game development, making it easier to extend and reuse components across different games.

## Features

- **Modular Design**: A reusable core for scene management, input handling, and utilities.
- **Classic Snake Gameplay**: Control the snake, eat food, and grow while avoiding collisions.
- **Dynamic Score Tracking**: A score counter displayed in the top-left corner of the screen.
- **Collision Detection**: Built-in checks for wall and self-collisions.
- **Extendable Settings**: Easily configurable screen dimensions, colors, and game behavior.

## Requirements

The following dependencies are required to run the project:

- Python 3.10 or later
- Pygame 2.5.2 or later

### Installing Dependencies

Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pygame-snake.git
   cd pygame-snake
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:

   ```bash
   python snake/main.py
   ```

## How to Play

- **Arrow Keys**: Control the snake's direction (Up, Down, Left, Right).
- **Objective**: Eat the food to grow the snake and increase your score.
- **Game Over**: The game ends if the snake collides with itself or the walls.

## Project Structure

```plaintext
pygame-snake/
│
├── core/                   # Reusable core module
│   ├── game.py             # Main game loop logic
│   ├── scene.py            # Scene base class
│   ├── input_manager.py    # Input handling logic
│   ├── utils.py            # Utility functions (e.g., collision detection)
│   └── __init__.py         # Module initialization
│
├── snake/                  # Game-specific implementation
│   ├── entities/           # Game entities
│   │   ├── snake.py        # Snake entity logic
│   │   ├── food.py         # Food entity logic
│   │   └── __init__.py     # Module initialization
│   ├── scenes/             # Game scenes
│   │   ├── main_menu.py    # Main menu scene
│   │   ├── gameplay.py     # Gameplay scene
│   │   └── __init__.py     # Module initialization
│   ├── settings.py         # Game-specific settings
│   └── main.py             # Game entry point
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Future Enhancements

- **Game Over Screen**: Add a scene to display the final score and options to restart or quit.
- **Levels/Difficulty**: Increase the snake’s speed as the score increases.
- **Custom Themes**: Allow players to choose colors or themes for the game.
- **Save High Scores**: Persist high scores to a file or database.

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Submit a pull request.
