import pygame
import random
import sys
from typing import List, Tuple


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.grid_size = 20
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')

        self.snake: List[Tuple[int, int]] = [(self.width // 2, self.height // 2)]
        self.direction = (self.grid_size, 0)
        self.food = self._place_food()
        self.score = 0
        self.game_over = False

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        self.clock = pygame.time.Clock()

    def _place_food(self) -> Tuple[int, int]:
        while True:
            x = random.randrange(0, self.width, self.grid_size)
            y = random.randrange(0, self.height, self.grid_size)
            if (x, y) not in self.snake:
                return (x, y)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != (0, self.grid_size):
                    self.direction = (0, -self.grid_size)
                elif event.key == pygame.K_DOWN and self.direction != (0, -self.grid_size):
                    self.direction = (0, self.grid_size)
                elif event.key == pygame.K_LEFT and self.direction != (self.grid_size, 0):
                    self.direction = (-self.grid_size, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-self.grid_size, 0):
                    self.direction = (self.grid_size, 0)
        return True

    def update(self):
        if self.game_over:
            return

        new_head = (
            (self.snake[0][0] + self.direction[0]) % self.width,
            (self.snake[0][1] + self.direction[1]) % self.height
        )

        if new_head in self.snake[1:]:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self._place_food()
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill(self.BLACK)

        for segment in self.snake:
            pygame.draw.rect(self.screen, self.GREEN,
                             (segment[0], segment[1], self.grid_size - 2, self.grid_size - 2))

        pygame.draw.rect(self.screen, self.RED,
                         (self.food[0], self.food[1], self.grid_size - 2, self.grid_size - 2))

        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, self.WHITE)
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            game_over_text = font.render('Game Over!', True, self.WHITE)
            text_rect = game_over_text.get_rect(center=(self.width / 2, self.height / 2))
            self.screen.blit(game_over_text, text_rect)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(10)

        pygame.quit()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
