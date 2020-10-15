import math
import pygame
from pygame.draw import *
from random import randint
import csv

pygame.init()

FPS = 50
sc = pygame.display.set_mode((700, 500))
width = 700
height = 500

# Colours of balls and background
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Font for text on screen
font = pygame.font.Font(None, 36)
#######################################################################################################################
"""S O U N D"""
# Sound effects for shooting and exploding balls
shooting = pygame.mixer.Sound('LAZER.wav')
explosion = pygame.mixer.Sound('explode.wav')
time = 0


def new_ball():
    """
    This function creates a number of parameters, surface and circle objects
    """
    # Center of ball
    x = randint(100, 600)
    y = randint(100, 400)
    # Radius of ball
    r = randint(30, 80)
    # Surface on which the ball is located
    surf = pygame.Surface((2 * r, 2 * r), pygame.SRCALPHA)
    # Color of the ball
    color = COLORS[randint(0, 5)]
    # Circle object representing a ball
    ball = circle(surf, color, (r, r), r)
    # Setting location of the center of surface
    ballrect = surf.get_rect(center=(x, y))
    # Setting speed
    speed = [randint(-5, 5), randint(-5, 5)]
    return x, y, r, ball, ballrect, surf, speed


def new_square():
    """
    This function is analogical to the previous except it creates squares
    """
    x = randint(100, 600)
    y = randint(100, 400)
    a = randint(60, 80)
    surf = pygame.Surface((a, a), pygame.SRCALPHA)
    color = COLORS[randint(0, 5)]
    square = rect(surf, color, (0, 0, a, a))
    squarerect = surf.get_rect(center=(x, y))
    speed = [8, 8]
    return x, y, a, square, squarerect, surf, speed


# This cycle fills list with data from function new_circle
balls = []
for _ in range(5):
    this_ball = new_ball()
    balls += [this_ball]

    ball = this_ball[3]
    ballrect = this_ball[4]
    surf = this_ball[5]
    speed = this_ball[6]
    x_cord = this_ball[0]
    y_cord = this_ball[1]

# This cycle fills list with data from function new_square
squares = []
for i in range(2):
    this_square = new_square()
    squares += [this_square]

    square = this_square[3]
    squarerect = this_square[4]
    surf = this_square[5]
    speed = this_square[6]
    x_cord = this_square[0]
    y_cord = this_square[1]

# Points
count = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

tbl = []
Name = input("Type your name: ")
table = open("records.csv")

for line in table:
    tbl.append(line)
print(tbl[2])

########################################################################################################################
"""E V E N T S"""

while not finished:
    sc.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # shooting.play()
            delta = 0
            for i in range(len(balls)):
                mouse_pos = event.pos
                distance = math.sqrt((balls[i][0] - mouse_pos[0]) ** 2 + (balls[i][1] - mouse_pos[1]) ** 2)
                if distance < balls[i][2]:
                    delta += 1
                    # Explosion
                    explosion_surf = pygame.image.load('explosion.png')
                    explosion_rect = explosion_surf.get_rect(center=(balls[i][0], balls[i][1]))
                    sc.blit(explosion_surf, explosion_rect)
                    balls[i] = new_ball()
                    explosion.play()
            for k in range(len(squares)):
                mouse_pos = event.pos
                distance_x = abs(squares[k][0] - mouse_pos[0])
                distance_y = abs(squares[k][1] - mouse_pos[1])
                if (distance_x < (squares[k][2] / 2)) and (distance_y < (squares[k][2] / 2)):
                    delta += 3
                    squares[k] = new_square()
                    # explosion.play()
            count += delta
    # Moving ball
    for j in range(len(balls)):

        ball = balls[j][3]
        ballrect = balls[j][4]
        surf = balls[j][5]
        x_cord = balls[j][0]
        y_cord = balls[j][1]
        speed = balls[j][6]

        sc.blit(surf, ballrect)
        ballrect = ballrect.move(speed[0], speed[1])
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        x_cord += speed[0]
        y_cord += speed[1]

        balls[j] = (x_cord, y_cord, balls[j][2], ball, ballrect, surf, speed)
    # Moving square
    for n in range(len(squares)):

        square = squares[n][3]
        squarerect = squares[n][4]
        surf = squares[n][5]
        speed = squares[n][6]
        x_cord = squares[n][0]
        y_cord = squares[n][1]

        sc.blit(surf, squarerect)
        prob = randint(1, 20)
        if prob == 7:
            speed[0] = -speed[0]
        elif prob == 6:
            speed[1] = -speed[1]
        else:
            pass
        squarerect = squarerect.move(speed[0], speed[1])
        if squarerect.left < 0 or squarerect.right > width:
            speed[0] = -speed[0]
        if squarerect.top < 0 or squarerect.bottom > height:
            speed[1] = -speed[1]
        x_cord += speed[0]
        y_cord += speed[1]

        squares[n] = (x_cord, y_cord, squares[n][2], square, squarerect, surf, speed)

    text = font.render("Score: " + str(count), 1, (0, 200, 0))
    table_of_records = font.render("Your record: " + str(tbl[2]), 1, (100, 200, 0))

    place_1 = text.get_rect(center=(100, 50))
    place_2 = text.get_rect(center=(100, 100))

    sc.blit(text, place_1)
    sc.blit(table_of_records, place_2)

    pygame.display.update()
    time += 1 / FPS
    clock.tick(FPS)
pygame.quit()

print(time)

data = [{Name: count}]

with open('records.csv', 'w') as f:
    writer = csv.DictWriter(
        f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data:
        writer.writerow(d)
