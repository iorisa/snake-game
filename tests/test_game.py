## test_game.py

import unittest
from snake_game.game import SnakeGame, Point

class TestSnakeGame(unittest.TestCase):

    def test_snake_game_initialization(self):
        game = SnakeGame()
        self.assertEqual(game.score, 0)
        self.assertEqual(game.speed, 1)
        self.assertEqual(len(game.snake_body), 3)
        self.assertEqual(game.food_position.x, 300)
        self.assertEqual(game.food_position.y, 300)
        self.assertEqual(game.direction, "RIGHT")
        self.assertEqual(game.change_to, "RIGHT")

    def test_snake_game_update_direction(self):
        game = SnakeGame()
        game.update_direction("UP")
        self.assertEqual(game.change_to, "UP")
        game.update_direction("DOWN")
        self.assertEqual(game.change_to, "DOWN")
        game.update_direction("LEFT")
        self.assertEqual(game.change_to, "LEFT")
        game.update_direction("RIGHT")
        self.assertEqual(game.change_to, "RIGHT")

    def test_snake_game_update_game(self):
        game = SnakeGame()
        game.update_game()
        self.assertEqual(game.snake_body[0].x, 110)
        game.update_direction("UP")
        game.update_game()
        self.assertEqual(game.snake_body[0].y, 40)

    def test_snake_game_handle_collisions(self):
        game = SnakeGame()
        self.assertFalse(game.handle_collisions())
        game.snake_body[0].x = 800
        self.assertTrue(game.handle_collisions())

    def test_snake_game_generate_food(self):
        game = SnakeGame()
        game.generate_food()
        self.assertNotEqual(game.food_position.x, 300)
        self.assertNotEqual(game.food_position.y, 300)

    def test_snake_game_increase_snake_length(self):
        game = SnakeGame()
        game.increase_snake_length()
        self.assertEqual(len(game.snake_body), 4)

    def test_snake_game_play_game(self):
        game = SnakeGame()
        game.play_game()
        # This test is to check if the game runs without errors, not to assert specific outcomes.

if __name__ == '__main__':
    unittest.main()
