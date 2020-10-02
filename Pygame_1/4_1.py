import pygame
from pygame.draw import *
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (237, 237, 200)
GREEN = (128, 255, 38)
DARK_GREEN = (0, 129, 0)
YELLOW = (255, 255, 0)
RED = (255, 38, 37)
PINK = (234, 199, 177)
ORANGE = (255, 102, 0)
VIOLET = (213, 38, 255)
BLUE = (129, 180, 255)
BROWN = (121, 66, 27)
GRAY = (191, 201, 184)

sc = pygame.display.set_mode((1000, 1000))


########################################################################################################################

def draw_a_boy(dx, poster_type, shirt_color, eye_color, hair_color):
    body = circle(sc, shirt_color, (500 + dx, 700), 200)
    face = circle(sc, PINK, (500 + dx, 450), 150)

    eye_left = ellipse(sc, eye_color, (420 + dx, 380, 70, 50), 0)
    eye_right = ellipse(sc, eye_color, (510 + dx, 380, 70, 50), 0)
    eye_left = ellipse(sc, BLACK, (420 + dx, 380, 70, 50), 1)
    eye_right = ellipse(sc, BLACK, (510 + dx, 380, 70, 50), 1)

    eye1_left = circle(sc, BLACK, (450 + dx, 405), 10)
    eye1_right = circle(sc, BLACK, (550 + dx, 405), 10)

    nose = polygon(sc, BROWN, ((480 + dx, 450), (520 + dx, 450), (500 + dx, 470)))
    mouth = polygon(sc, RED, ((430 + dx, 490), (570 + dx, 490), (500 + dx, 530)))
    nose = polygon(sc, BLACK, ((480 + dx, 450), (520 + dx, 450), (500 + dx, 470)), 1)
    mouth = polygon(sc, BLACK, ((430 + dx, 490), (570 + dx, 490), (500 + dx, 530)), 1)

    def regular_polygon(x0, y0, R, n):
        vertex_coord = []
        phi = (n - 2) / n * math.pi
        for i in range(n):
            xi = x0 + R * math.cos(phi + 2 * math.pi * i / n)
            yi = y0 + R * math.sin(phi + 2 * math.pi * i / n)
            vertex_coord.append((xi, yi))
        return vertex_coord

    def rotated_rectangle(a, b, x0, y0, alpha):
        beta = math.atan(b / a)
        d = math.sqrt((a * a) + (b * b))
        alpha = alpha / 180 * math.pi
        x1 = x0 + (d * math.cos(alpha + (math.pi - beta)) / 2)
        y1 = y0 + (d * math.sin(alpha + (math.pi - beta)) / 2)
        x2 = x0 + (d * math.cos(alpha + beta) / 2)
        y2 = y0 + (d * math.sin(alpha + beta) / 2)
        x3 = x0 + (d * math.cos(alpha - beta) / 2)
        y3 = y0 + (d * math.sin(alpha - beta) / 2)
        x4 = x0 + (d * math.cos(alpha - (math.pi - beta)) / 2)
        y4 = y0 + (d * math.sin(alpha - (math.pi - beta)) / 2)
        vert = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        return vert

    arm_left = polygon(sc, PINK, (rotated_rectangle(400, 30, 200 + dx, 390, 70)))
    arm_right = polygon(sc, PINK, (rotated_rectangle(400, 30, 800 + dx, 390, 110)))

    surf1 = pygame.Surface((200, 200), pygame.SRCALPHA)
    shoulder_left = polygon(sc, shirt_color, (regular_polygon(300 + dx, 600, 70, 5)))
    shoulder_right = polygon(surf1, shirt_color, (regular_polygon(100, 100, 70, 5)))
    shoulder_right = polygon(surf1, BLACK, (regular_polygon(100, 100, 70, 5)), 1)
    surf2 = pygame.transform.rotate(surf1, -45)

    sc.blit(surf2, (560 + dx, 460))
    shoulder_left = polygon(sc, BLACK, (regular_polygon(300 + dx, 600, 70, 5)), 1)

    hand_left = ellipse(sc, PINK, [100 + dx, 100, 60, 120])
    hand_right = ellipse(sc, PINK, [840 + dx, 100, 60, 120])
    hand_left = ellipse(sc, WHITE, [100 + dx, 100, 60, 120], 1)
    hand_right = ellipse(sc, WHITE, [840 + dx, 100, 60, 120], 1)

    # hair
    def stuck_polygons(angle, k, x0, y0, sign, R):
        for i in range(k):
            surf3 = pygame.Surface((50, 50), pygame.SRCALPHA)
            triangle = polygon(surf3, hair_color, ((0, 50), (50, 50), (25, 0)))
            triangle = polygon(surf3, BLACK, ((0, 50), (50, 50), (25, 0)), 1)
            surf4 = pygame.transform.rotate(surf3, 90 - angle * i)

            X = R * math.cos(angle * i / 180 * math.pi)
            sc.blit(surf4, (x0 - X + dx, y0 - math.sqrt(R ** 2 - X ** 2)))

    stuck_polygons(16, 12, 470, 410, 1, 170)

    rect(sc, GREEN, (100 + dx, 100, 800, 100))

    font = pygame.font.Font(None, 72)
    if poster_type == 1:
        rect(sc, GREEN, (100 + dx, 100, 800, 100))
        text = font.render("PYTHON is AMAZING", 1, BLACK)
        place = text.get_rect(center=(500, 150))
    else:
        rect(sc, GREEN, (100 + dx, 100, 800, 100))
        text = font.render("PYTHON is REALLY AMAZING", 1, BLACK)
        place = text.get_rect(center=(850, 150))

    sc.blit(text, place)


draw_a_boy(0, 1, ORANGE, BLUE, VIOLET)

pygame.display.update()
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    pygame.time.delay(20)
