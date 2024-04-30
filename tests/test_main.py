## test_main.py

import unittest
from game import SnakeGame

class TestSnakeGame(unittest.TestCase):

    def test_game_initialization(self):
        game = SnakeGame()
        self.assertIsNotNone(game, "Game object should be initialized")

    def test_game_play(self):
        game = SnakeGame()
        self.assertTrue(callable(game.play_game), "play_game method should be callable")

if __name__ == '__main__':
    unittest.main()
