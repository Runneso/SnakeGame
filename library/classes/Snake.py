import pygame
from library.config import GAME_WIDTH, GAME_HEIGHT, GAME_SIZE
from library.classes.Color import Color

GREEN = Color(0, 0, 255)
YELLOW = Color(255, 0, 255)


class Snake:

    def __init__(self, snake_x: int, snake_y: int, snake_velocity: int):
        self.x, self.y, self.velocity = snake_x, snake_y, snake_velocity
        self.snake = [pygame.Surface((GAME_SIZE, GAME_SIZE)), pygame.Surface((GAME_SIZE, GAME_SIZE))]
        self.snake[0].fill(YELLOW())
        self.snake[1].fill(GREEN())
        self.directions = [False, False, False, False]

    def check_directions(self):
        if self.directions[0]:
            self.x -= self.velocity
        elif self.directions[1]:
            self.x += self.velocity
        elif self.directions[2]:
            self.y += self.velocity
        elif self.directions[3]:
            self.y -= self.velocity

    def get_coordinates(self) -> tuple[int, int]:
        return self.x, self.y
