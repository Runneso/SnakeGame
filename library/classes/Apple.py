from random import randint
from library.config import GAME_WIDTH, GAME_HEIGHT, GAME_SIZE


class Apple:
    def __init__(self, apple_x: int, apple_y: int, radius: int):
        self.x, self.y, self.radius = apple_x, apple_y, radius

    def respawn_apple(self):
        self.x, self.y = randint(15, GAME_SIZE * GAME_HEIGHT - 15), randint(15, GAME_SIZE * GAME_WIDTH - 15)

    def get_coordinates(self) -> tuple[int, int]:
        return self.x, self.y
