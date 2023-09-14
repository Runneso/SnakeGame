import pygame
import ctypes
from random import randint
from library.config import GAME_WIDTH, GAME_HEIGHT, GAME_SIZE
from library.classes.Color import Color
from library.classes.Apple import Apple
from library.classes.Snake import Snake


def distance_between_apple_snake(snake: Snake, apple: Apple) -> None:
    global LENGTH
    if abs(apple.x - snake.x) < GAME_SIZE and abs(apple.y - snake.y) < GAME_SIZE:
        apple.respawn_apple()
        sound_apple_eating.play()
        LENGTH += 1


def teleport_snake(snake: Snake) -> None:
    if snake.y >= GAME_HEIGHT * GAME_SIZE:
        snake.y = 0.5
    elif snake.y <= -0.5:
        snake.y = GAME_HEIGHT * GAME_SIZE - 0.5
    elif snake.x >= GAME_WIDTH * GAME_SIZE + 0.5:
        snake.x = 0.5
    elif snake.x <= -0.5:
        snake.x = GAME_WIDTH * GAME_SIZE - 0.5


if __name__ == "__main__":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')
    pygame.init()

    main_screen = pygame.display.set_mode((GAME_WIDTH * GAME_SIZE, GAME_HEIGHT * GAME_SIZE))
    sound_apple_eating = "sounds/apple_eating.mp3"
    sound_apple_eating = pygame.mixer.Sound(sound_apple_eating)
    game_name = "Snake Game"
    pygame.display.set_caption(game_name)
    game_logo = "images/logo.png"
    pygame.display.set_icon(pygame.image.load(game_logo))
    LENGTH = 2
    FPS = 60
    RED = Color(255, 0, 0)
    BLACK = Color(0, 0, 0)
    GREEN = Color(0, 0, 255)
    clock = pygame.time.Clock()

    snake = Snake((GAME_SIZE * GAME_WIDTH) // 2, (GAME_SIZE * GAME_HEIGHT) // 2, GAME_SIZE // 5)
    apple = Apple(randint(15, GAME_SIZE * GAME_WIDTH - 15), randint(15, GAME_SIZE * GAME_WIDTH - 15), 15)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.directions = [False, False, False, False]
                    snake.directions[0] = True
                if event.key == pygame.K_RIGHT:
                    snake.directions = [False, False, False, False]
                    snake.directions[1] = True
                if event.key == pygame.K_DOWN:
                    snake.directions = [False, False, False, False]
                    snake.directions[2] = True
                if event.key == pygame.K_UP:
                    snake.directions = [False, False, False, False]
                    snake.directions[3] = True

        main_screen.fill(BLACK())
        pygame.draw.circle(main_screen, RED(), (apple.get_coordinates()), 15)
        snake.check_directions()
        distance_between_apple_snake(snake, apple)
        teleport_snake(snake)
        for index in range(LENGTH):
            if snake.directions[0]:
                main_screen.blit(snake.snake[0 if index == 0 else 1],
                                 (snake.get_coordinates()[0] + 40 * index, snake.get_coordinates()[1]))
            if snake.directions[1]:
                main_screen.blit(snake.snake[0 if index == 0 else 1],
                                 (snake.get_coordinates()[0] - 40 * index, snake.get_coordinates()[1]))
            if snake.directions[2]:
                main_screen.blit(snake.snake[0 if index == 0 else 1],
                                 (snake.get_coordinates()[0], snake.get_coordinates()[1] - 40 * index))
            if snake.directions[3]:
                main_screen.blit(snake.snake[0 if index == 0 else 1],
                                 (snake.get_coordinates()[0], snake.get_coordinates()[1] + 40 * index))

        pygame.display.update()
        clock.tick(6)
