import pygame
import time
import random
pygame.init()

steelblue = (70, 130, 180)
yellow = (255, 200, 102)
green = (0, 255, 0)
purple = (140, 8, 211)
red = (255, 0, 0)
black = (0, 5, 10)

dis_width = 700
dis_height = 500
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Python game by SABARI_AB!')

clock = pygame.time.Clock()
snake = 10
snake_speed = 20
font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 45)


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [200, 10])


def our_snake(snake, list):
    for x in list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake, snake])


def message(msg, color):
    messg = font_style.render(msg, True, color)
    dis.blit(messg, [dis_width/6, dis_height/3])


def gameloop():
    game = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    list = []
    length_snake = 1

    fx = round(random.randrange(0, dis_width - snake) / 10.0) * 10.0
    fy = round(random.randrange(0, dis_height - snake) / 10.0) * 10.0

    while not game:

        while game_close == True:
            dis.fill(steelblue)
            message("OOPS! YOU LOST! Press Q-Quit or C-Play again", red)
            your_score(length_snake - 1)
            pygame.display.update()

            for  event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(purple)
        pygame.draw.rect(dis, black, [fx, fy, snake, snake])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        list.append(snake_head)
        if len(list) > length_snake:
            del list[0]
        for x in list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake, list)
        your_score(length_snake - 1)

        pygame.display.update()

        if x1 == fx and y1 == fy:
            fx = round(random.randrange(0, dis_width - snake) / 10.0) * 10.0
            fy = round(random.randrange(0, dis_height - snake) / 10.0) * 10.0
            length_snake += 1

        clock.tick(snake_speed)

    pygame.display.update()
    time.sleep(0.7)

    pygame.quit()
    quit()


gameloop()