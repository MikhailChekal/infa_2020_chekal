import math
import pygame
from pygame.draw import *
import random
import csv

pygame.init()

FPS = 30
sc = pygame.display.set_mode((700, 500))
width = 700
height = 500
time = 0
username = ""
count = 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    def __init__(self, x, y):

        self.r = random.randint(30, 50)
        self.x = x
        self.y = y
        self.v_x = random.choice([-2, -1, 1, 2])
        self.v_y = random.choice([-2, -1, 1, 2])
        self.color = random.choice([RED, CYAN, MAGENTA, GREEN, BLUE, YELLOW])
        self.rect = rect
        self.surf = pygame.Surface((2 * self.r, 2 * self.r), pygame.SRCALPHA)
        self.ballrect = pygame.Surface((2 * self.r, 2 * self.r), pygame.SRCALPHA).get_rect(center=(x, y))

    def ball(self):
        circle(self.surf, self.color, (self.r, self.r), self.r)

    def square(self):
        rect(self.surf, self.color, (0, 0, self.r, self.r))

    def move_ball(self):
        sc.blit(self.surf, self.ballrect)
        self.ballrect = self.ballrect.move(self.v_x, self.v_y)
        if self.ballrect.left < 0 or self.ballrect.right > width:
            self.v_x = -self.v_x
        if self.ballrect.top < 0 or self.ballrect.bottom > height:
            self.v_y = -self.v_y
        self.x += self.v_x
        self.y += self.v_y

        for k in balls:
            dist = math.sqrt((self.x - k.x) ** 2 + (self.y - k.y) ** 2)
            if (dist < self.r + k.r) and (int(dist) > 0):
                self.v_x = -self.v_x
                self.v_y = -self.v_y
            print(self.x, self.y)

    def distance(self):
        dist = [1000]
        for k in balls:
            dist.append(math.sqrt((self.x - k.x) ** 2 + (self.y - k.y) ** 2))
        return min(dist)

    def move_square(self):
        sc.blit(self.surf, self.ballrect)
        self.ballrect = self.ballrect.move(self.v_x, self.v_y)
        if self.ballrect.left < 0 or self.ballrect.right > width:
            self.v_x = -self.v_x
        if self.ballrect.top < 0 or self.ballrect.bottom > height:
            self.v_y = -self.v_y
        else:
            self.v_x *= 1.01
            self.v_y *= 1.01
        self.x += self.v_x
        self.y += self.v_y

    def shot(self):
        mouse_pos = event.pos
        distance = math.sqrt((self.x - mouse_pos[0]) ** 2 + (self.y - mouse_pos[1]) ** 2)
        if distance < self.r:
            shot = True
            points = 1
        else:
            shot = False
            points = 0
        return shot, points

    '''def collision(self):
        for k in balls:
            dist = math.sqrt((self.x - k.x) ** 2 + (self.y - k.y) ** 2)
            if (dist < self.r + k.r) and (int(dist) > 0):
                self.v_x = 0
                self.v_x = 0
                print('error', dist, (self.r + k.r))'''
    # def shot(self, event):


balls = []
for _ in range(7):
    new_ball = Ball(random.randint(50, 650), random.randint(50, 450))
    while new_ball.distance() < 100:
        new_ball = Ball(random.randint(50, 650), random.randint(50, 450))
    balls.append(new_ball)

squares = []
for _ in range(2):
    new_square = Ball(random.randint(50, 650), random.randint(50, 450))
    squares.append(new_square)


pygame.display.update()
clock = pygame.time.Clock()
finished = False


def score(surface, count):
    font = pygame.font.SysFont('arial', 25, True)
    text_1 = font.render("Счет : {}".format(count), True, WHITE)
    surface.blit(text_1, (0, 0))


def dialog(surface, count):
    surface.fill(BLACK)
    font = pygame.font.SysFont('arial', 32, True)
    text_1 = font.render("Ваш счет: {}".format(count), True, WHITE)
    text_2 = font.render("Введите имя и нажмите Enter", True, WHITE)
    surface.blit(text_1, text_1.get_rect(center=(width / 2, height / 3)))
    surface.blit(text_2, text_2.get_rect(center=(width / 2, height * 2 / 3)))


def user_text(surface, count):
    global username
    font = pygame.font.SysFont('arial', 32, True)
    text_1 = font.render(username, True, WHITE)
    surface.blit(text_1, text_1.get_rect(center=(width / 2, height / 2)))
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_BACKSPACE:
                username = username[:-1]
            elif events.key == pygame.K_RETURN:
                if username != "":
                    with open('best_scores.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow([username, count, time])
                return True
            else:
                username += events.unicode


while not finished:
    sc.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            while not finished:
                dialog(sc, count)
                finished = user_text(sc, count)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in balls:
                if i.shot()[0]:
                    balls.remove(i)
                    i = Ball(random.randint(50, 650), random.randint(50, 450))
                    balls.append(i)
                    count += i.shot()[1]
            for j in squares:
                if j.shot()[0]:
                    squares.remove(j)
                    squares.append(Ball(random.randint(50, 650), random.randint(50, 450)))
                    count += j.shot()[1] * 2
    for i in balls:
        i.move_ball()
        i.ball()
    for j in squares:
        j.move_square()
        j.square()

    font_1 = pygame.font.SysFont('arial', 32, True)
    text = font_1.render("Счет: " + str(count), True, WHITE)
    place = text.get_rect(center=(100, 50))
    sc.blit(text, place)

    pygame.display.update()
    time += 1 / FPS
    clock.tick(FPS)
pygame.quit()
