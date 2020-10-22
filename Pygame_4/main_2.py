import math
import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
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
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    def __init__(self, r, x, y, v_x, v_y, color):
        self.r = r
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.color = color
        self.rect = rect
        self.surf = pygame.Surface((2 * r, 2 * r))
        self.ballrect = pygame.Surface((2 * r, 2 * r), pygame.SRCALPHA).get_rect(center=(x, y))
        # self.ball = circle(pygame.Surface((2 * r, 2 * r), pygame.SRCALPHA), color, (r,r), r)

    def ball(self, surf, color, r):
        circle(surf, color, (r, r), r)

    '''def ballrect(self, surf, x, y):
        surf.get_rect(center=(x, y))'''

    '''def draw(self, surf, ballrect):
        sc.blit(surf, ballrect)'''

    def move(self, surf, ballrect, v_x, v_y, x, y):
        sc.blit(surf, ballrect)
        ballrect = ballrect.move(v_x, v_y)
        if ballrect.left < 0 or ballrect.right > width:
            v_x = -v_x
        if ballrect.top < 0 or ballrect.bottom > height:
            v_y = -v_y
        x += v_x
        y += v_y


balls = []
for _ in range(1):
    new_ball = Ball(randint(30, 60), randint(50, 650), randint(50, 450), randint(1, 5), randint(1, 5),
                    COLORS[randint(1, 5)])
    # new_ball.ball(new_ball.surf, new_ball.color, new_ball.r)
    # new_ball.draw(new_ball.surf, new_ball.ballrect)
    balls.append(new_ball)
    print(new_ball.v_y, new_ball.v_x)

def score(surface, score):
    font = pygame.font.SysFont('arial', 25, True)
    text_1 = font.render("Score : {}".format(score), True, WHITE)
    surface.blit(text_1, (0, 0))


def dialog(surface, score):
    surface.fill(BLACK)
    font = pygame.font.SysFont('arial', 32, True)
    text_1 = font.render("Your score is {}".format(score), True, WHITE)
    text_2 = font.render("Please enter your name and press F1(or q to quit)", True, WHITE)
    surface.blit(text_1, text_1.get_rect(center=(width / 2, height / 3)))
    surface.blit(text_2, text_2.get_rect(center=(width / 2, height * 2 / 3)))


def user_text(surface, score):
    global user_name
    font = pygame.font.SysFont('arial', 32, True)
    text_1 = font.render(user_name, True, WHITE)
    surface.blit(text_1, text_1.get_rect(center=(width / 2, height / 2)))
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_BACKSPACE:
                user_name = user_name[:-1]
            elif events.key == pygame.K_ESCAPE or events.key == pygame.K_q:
                return True
            elif events.key == pygame.K_F1:
                if user_name != "":
                    with open('Best scores.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow([user_name, score, asctime()])
                return True
            else:
                user_name += events.unicode
'''
def distance(balls):
    b = []
    for k in range(len(balls)):
        for t in range(len(balls)):
            if t > k:
                b.append([math.sqrt((balls[k].x - balls[t].x)**2 + (balls[k].y - balls[t].y)**2), k, t])
            else:
                pass
    print(b)
    for i in range(len(b)):
        n_1 = b[i][1]
        n_2 = b[i][2]
        if b[i][0] < balls[n_1].r + balls[n_2].r:
                print("ERROR!", n_1, n_2)
    return b


print(distance(balls))
'''
count = 0

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    sc.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            while not finished:
                dialog(sc, score)
                finished = user_text(sc, score)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            delta = 0
            for i in balls:
                mouse_pos = event.pos
                distance = math.sqrt((i.x - mouse_pos[0]) ** 2 + (i.y - mouse_pos[1]) ** 2)
                if distance < i.r:
                    delta += 1
                    i = Ball(randint(30, 60), randint(50, 650), randint(50, 450), randint(1, 5), randint(1, 5),
                             COLORS[randint(1, 5)])
            count += delta
    for i in balls:
        # i.draw(i.surf, i.ballrect)
        i.move(i.surf, i.ballrect, i.v_x, i.v_y, i.x, i.y)
        i.ball(i.surf, i.color, i.r)

        print(i.x, i.x)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

print(count)
print(balls)
