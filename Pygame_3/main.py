import math
import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
sc = pygame.display.set_mode((700, 500))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

font = pygame.font.Font(None, 72)


def new_ball():
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(10, 20)
    surf = pygame.Surface((r, r))
    color = COLORS[randint(0, 5)]
    ball = circle(surf, color, (x, y), r)
    ballrect = surf.get_rect()
    return x, y, r, ball, ballrect


speed = [2, 2]
ball = new_ball()[3]


count = 0
misses =0

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Ваш счет - ", count, "очков")
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            distance = math.sqrt((ball[0] - mouse_pos[0]) ** 2 + (ball[1] - mouse_pos[1]) ** 2)
            if distance < ball[2]:
                count += 1
            else:
                misses += 1

    ballrect = ballrect.move(speed)

    text = font.render("Score: " + str(count), 1, (0, 200, 0))
    place = text.get_rect(center=(100, 50))
    sc.blit(text, place)
    pygame.display.update()
    sc.fill(BLACK)

pygame.quit()
