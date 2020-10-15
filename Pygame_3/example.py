import sys, pygame
pygame.init()

size = width, height = 800, 800
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

surf = pygame.Surface((50, 50))
ball = pygame.draw.circle(surf, (100, 200, 100), (50, 50), 30)
ballrect = surf.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(surf, ballrect)
    pygame.display.flip()