import pygame
from pygame.draw import *
import math


pygame.init()

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (220, 20, 60)


FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((230, 230, 230))

'''surf_1 = pygame.Surface((700, 700))
surf_1.fill(YELLOW)'''
# face
face = circle(screen, YELLOW, (200, 200), 100, 0)

# eyes
circle(screen, RED, (170, 170), 15, 0)
circle(screen, BLACK, (170, 170), 5)
circle(screen, RED, (230, 170), 15, 0)
circle(screen, BLACK, (230, 170), 5)
# eyebrows
#img_1 = rect(screen, BLACK, (150, 150, 100, 10))
x1 = 130
y1 = 150 - 20

x2 = 180
y2 = 170 - 20

x3 = 120
y3 = 160 - 20

x4 = 170
y4 = 180 - 20

polygon(screen, BLACK, ((x1, y1), (x2, y2), (x4, y4), (x3, y3)))
polygon(screen, BLACK, ((400 - x1, y1), (400 - x2, y2), (400 - x4, y4), (400 - x3, y3)))

# mouth
rect(screen, BLACK, (170, 230, 60, 10))



'''rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100, 100), (200, 50),
                                (300, 100), (100, 100)])
polygon(screen, (0, 0, 255), [(100, 100), (200, 50),
                              (300, 100), (100, 100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)'''

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
