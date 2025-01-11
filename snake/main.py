import pygame

from engine.scene_manager import SceneManager, Scene
from engine.components import SpriteRenderer
from engine.input_manager import InputManager

from snake.scenes import MainMenuScene, GameScene, GameOverScene
from snake.settings import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()

# Initialize InputManager
InputManager.bind_action("move_up", pygame.K_UP)
InputManager.bind_action("move_down", pygame.K_DOWN)
InputManager.bind_action("move_left", pygame.K_LEFT)
InputManager.bind_action("move_right", pygame.K_RIGHT)

# Init Scenes
mainMenu = MainMenuScene()
gameScene = GameScene()
gameOverScene = GameOverScene()

# Setup scenes
SceneManager.register_scene(mainMenu)
SceneManager.register_scene(gameScene)
SceneManager.register_scene(gameOverScene)
SceneManager.load_scene(mainMenu)

print(SceneManager.get_active_scene())

# Game loop
running = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        InputManager.handle_event(event)

    SceneManager.update_active_scene(clock.tick(60) / 1000.0)
    active_scene = SceneManager.get_active_scene()
    if active_scene:
        for game_object in active_scene.game_objects:
            sprite_renderer = game_object.get_component(SpriteRenderer)
            if sprite_renderer:
                sprite_renderer.render(screen)
    pygame.display.flip()

pygame.quit()
