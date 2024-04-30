import unittest
from snake_game import Snake, Food, GameBoard

class TestSnakeGame(unittest.TestCase):

    def test_snake_initial_length(self):
        snake = Snake()
        self.assertEqual(len(snake.body), 1)

    def test_food_position(self):
        food = Food()
        self.assertIsInstance(food.position, tuple)
        self.assertEqual(len(food.position), 2)

    def test_game_board_size(self):
        game_board = GameBoard(10, 10)
        self.assertEqual(game_board.width, 10)
        self.assertEqual(game_board.height, 10)

    def test_game_board_update(self):
        game_board = GameBoard(10, 10)
        snake = Snake()
        game_board.update(snake, Food())
        self.assertEqual(len(game_board.board), 10)
        self.assertEqual(len(game_board.board[0]), 10)

if __name__ == '__main__':
    unittest.main()
