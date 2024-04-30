## game.py

import pygame
import random

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class SnakeGame:
    def __init__(self):
        self.score = 0
        self.speed = 1
        self.snake_body = [Point(100, 50), Point(90, 50), Point(80, 50)]
        self.food_position = Point(300, 300)
        self.direction = "RIGHT"
        self.change_to = self.direction

    def start_game(self):
        pygame.init()
        self.game_window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Snake Game')

    def update_direction(self, direction: str):
        if direction == "UP" and self.direction != "DOWN":
            self.change_to = "UP"
        if direction == "DOWN" and self.direction != "UP":
            self.change_to = "DOWN"
        if direction == "LEFT" and self.direction != "RIGHT":
            self.change_to = "LEFT"
        if direction == "RIGHT" and self.direction != "LEFT":
            self.change_to = "RIGHT"

    def update_game(self):
        if self.change_to == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if self.change_to == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        if self.change_to == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if self.change_to == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

        if self.direction == "UP":
            self.snake_body[0].y -= 10
        if self.direction == "DOWN":
            self.snake_body[0].y += 10
        if self.direction == "LEFT":
            self.snake_body[0].x -= 10
        if self.direction == "RIGHT":
            self.snake_body[0].x += 10

    def draw_game(self):
        self.game_window.fill((255, 255, 255))
        for position in self.snake_body:
            pygame.draw.rect(self.game_window, (0, 0, 0), pygame.Rect(position.x, position.y, 10, 10))
        pygame.draw.rect(self.game_window, (255, 0, 0), pygame.Rect(self.food_position.x, self.food_position.y, 10, 10))
        pygame.display.flip()

    def handle_collisions(self):
        if self.snake_body[0].x >= 800 or self.snake_body[0].x < 0 or self.snake_body[0].y >= 600 or self.snake_body[0].y < 0:
            return True
        for block in self.snake_body[1:]:
            if block.x == self.snake_body[0].x and block.y == self.snake_body[0].y:
                return True
        return False

    def generate_food(self):
        self.food_position = Point(random.randrange(1, 80) * 10, random.randrange(1, 60) * 10)
        for block in self.snake_body:
            if block.x == self.food_position.x and block.y == self.food_position.y:
                self.generate_food()

    def increase_snake_length(self):
        new_head = Point(self.snake_body[0].x, self.snake_body[0].y)
        self.snake_body.insert(0, new_head)

    def play_game(self):
        self.start_game()
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.update_direction("UP")
                    if event.key == pygame.K_DOWN:
                        self.update_direction("DOWN")
                    if event.key == pygame.K_LEFT:
                        self.update_direction("LEFT")
                    if event.key == pygame.K_RIGHT:
                        self.update_direction("RIGHT")

            self.update_game()
            if self.handle_collisions():
                game_over = True
                self.game_over()
            if self.snake_body[0].x == self.food_position.x and self.snake_body[0].y == self.food_position.y:
                self.increase_snake_length()
                self.score += 1
                self.generate_food()
            self.draw_game()
            pygame.time.Clock().tick(30)

        pygame.quit()

    def game_over(self):
        font = pygame.font.SysFont(None, 55)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        self.game_window.blit(game_over_text, (300, 250))
        pygame.display.flip()
        pygame.time.delay(2000)

if __name__ == "__main__":
    game = SnakeGame()
    game.play_game()
