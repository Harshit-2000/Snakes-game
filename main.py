import pygame
import random
import math, sys, time

pygame.init()

screen = pygame.display.set_mode((450, 450))

snake_width = 10
red = (255, 0, 0)
snake_speed = 15
pos = []
clock = pygame.time.Clock()


def inc_length():
    for x in pos:
        snake_head = pygame.Rect(x[0], x[1], snake_width, snake_width)
        pygame.draw.rect(screen, red, snake_head)


def draw_food(x, y):
    food = pygame.Rect(x, y, snake_width, snake_width)
    pygame.draw.rect(screen, (0, 255, 255), food)


def collision(snakeX, snakeY, foodX, foodY):
    d = math.sqrt((snakeX - foodX) ** 2 + (snakeY - foodY) ** 2)
    if d < 15:
        return True
    else:
        return False


def print_message(msg, x, y, size):
    font = pygame.font.SysFont("comicsansms", size)
    text = font.render(msg, True, (0, 0, 0))
    screen.blit(text, (x, y))


def game():
    snakeX = 100
    snakeY = 100
    snakeX_speed = 10
    snakeY_speed = 0
    foodX = random.randint(20, 420)
    foodY = random.randint(20, 420)
    lenth_of_snake = 1
    direction = "right"
    game_over = False

    # main loop
    running = True
    while running:

        screen.fill((255, 255, 255))

        snakeX += snakeX_speed
        snakeY += snakeY_speed

        snake_head = pygame.Rect(snakeX, snakeY, snake_width, snake_width)
        pygame.draw.rect(screen, red, snake_head)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "down":
                    snakeY_speed = -snake_width
                    snakeX_speed = 0
                    direction = "up"
                if event.key == pygame.K_DOWN and direction != "up":
                    snakeY_speed = snake_width
                    snakeX_speed = 0
                    direction = "down"
                if event.key == pygame.K_LEFT and direction != "right":
                    snakeX_speed = -snake_width
                    snakeY_speed = 0
                    direction = "left"
                if event.key == pygame.K_RIGHT and direction != "left":
                    snakeX_speed = snake_width
                    snakeY_speed = 0
                    direction = "right"

        # snake does not go outside the screen
        if snakeX < 0:
            snakeX = 450
        if snakeX > 450:
            snakeX = 0
        if snakeY < 0:
            snakeY = 450
        if snakeY > 450:
            snakeY = 0

        # eating food
        if collision(snakeX, snakeY, foodX, foodY):
            lenth_of_snake += 1
            foodX = random.randint(5, 420)
            foodY = random.randint(5, 420)

        # increasing snakes length
        snake_head = []
        snake_head.append(snakeX)
        snake_head.append(snakeY)
        pos.append(snake_head)
        if len(pos) > lenth_of_snake:
            del pos[0]

        # game over
        for x in pos[:-1]:
            if x == snake_head:
                game_over = True
                time.sleep(1)
                pos.clear()
        while game_over == True:
            screen.fill((255, 150, 0))
            print_message("GAME OVER, Press P to play again or q to quit.", 20, 200, 16)
            pygame.display.update()
            # quit or play again option
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit()
                    if event.key == pygame.K_p:
                        game_over = False
                        game()

        clock.tick(snake_speed)
        draw_food(foodX, foodY)
        inc_length()
        print_message("Score : " + str(lenth_of_snake - 1), 10, 10, 15)

        pygame.display.update()


game()
