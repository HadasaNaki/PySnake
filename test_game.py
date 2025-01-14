import pytest
from game import SnakeGame

def test_snake_initialization():
    game = SnakeGame()
    assert len(game.snake) == 1
    assert game.score == 0
    assert not game.game_over

def test_food_placement():
    game = SnakeGame()
    food = game._place_food()
    assert isinstance(food, tuple)
    assert len(food) == 2
    assert 0 <= food[0] < game.width
    assert 0 <= food[1] < game.height

def test_collision_detection():
    game = SnakeGame()
    game.snake = [(100, 100), (120, 100)]
    game.direction = (-20, 0)
    game.update()
    assert game.game_over