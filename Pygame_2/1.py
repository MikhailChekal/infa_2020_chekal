"""
Program by Tsurkis Vera, refactored by Chekal Mikhail
02.10.2020
"""

import pygame
from pygame.draw import *

pygame.init()

FPS = 1
screen = pygame.display.set_mode((700, 500))

# цвета, использованные на картинке
LIGHT_BLUE = (0, 190, 255)
BLUE = (0, 0, 255)
SAND_YELLOW = (255, 255, 20)
SUN_YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
BROWN = (200, 100, 0)
PINK = (255, 100, 180)
DARK_BROWN = (100, 50, 50)
BLACK = (0, 0, 0)
KHAKI = (223, 214, 154)


########################################################################################################################

# фон рисунка
def background(sky_colour, sea_colour, sand_colour, x_wave, y_wave, r_wave):
    """
    Функция рисует небо, море и пляж
    :param r_wave: Радиус волны
    :param y_wave: Центр первой волны по x
    :param x_wave: Центр первой волны по y
    :param sky_colour: Цвет неба
    :param sea_colour: Цвет моря
    :param sand_colour: Цвет песка
    """
    screen.fill(sky_colour)
    rect(screen, sea_colour, (0, 200, 700, 120))
    rect(screen, sand_colour, (0, 320, 700, 180))
    wave_number = int(700 / (4 * r_wave)) + 1
    for _ in range(wave_number):
        circle(screen, SAND_YELLOW, (x_wave, y_wave), r_wave)
        circle(screen, BLUE, (x_wave + 2 * r_wave, y_wave), r_wave)
        x_wave += 4 * r_wave


def sun(x_sun, y_sun, r_sun):
    """
    Функция рисует солнце
    :param x_sun: Центр солнца по x
    :param y_sun: Центр солнца по y
    :param r_sun: Центр солнца по z
    """
    circle(screen, SUN_YELLOW, (x_sun, y_sun), r_sun)


def cloud(x_cl, y_cl, r_cl, delta_x, delta_y, cloud_size):
    """
    Функция рисует облако из нескольких кругов со сдвигом по x на
    :param x_cl: Координата центра первого круга
    :param y_cl: Координата центра первого круга
    :param r_cl: Радиус кругов
    :param delta_x: Расстояние между центрами облаков по x
    :param delta_y: Расстояние между центрами облаков по y
    :param cloud_size: Количество кругов в облаке
    """
    for _ in range(cloud_size):
        circle(screen, WHITE, (x_cl, y_cl), r_cl)
        circle(screen, GRAY, (x_cl, y_cl), r_cl, 1)
        x_cl += delta_x
        y_cl -= delta_y * (-1) ** _


# umbrella
def umbrella(x_um, y_um, width_rect_um, height_rect_um, width_polygon_um, height_polygon_um, colour_um):
    """
    :param x_um: Координата центра зонта по x
    :param y_um: Координата центра зонта по y
    :param width_rect_um: Ширина ножки зонта
    :param height_rect_um: Высота ножки зонта
    :param width_polygon_um: Ширина треугольника зонта
    :param height_polygon_um: Высота треугольника зонта
    :param colour_um: Цвет зонта
    """
    # рисует ножку зонта
    rect(screen, BROWN, (x_um, y_um, width_rect_um, height_rect_um))
    # рисует треугольник зонта
    polygon(screen, colour_um, [(x_um, y_um), (x_um - width_polygon_um, y_um + height_polygon_um),
                                (x_um + width_polygon_um + width_rect_um, y_um + height_polygon_um),
                                (x_um + width_rect_um, y_um)])
    # рисует спицы
    for _ in range(5):
        # спицы слева от ножки
        line(screen, DARK_BROWN, (x_um, y_um),
             (x_um - width_polygon_um + width_polygon_um * (_ + 1) / 5, y_um + height_polygon_um))
        # спицы справа от ножки
        line(screen, DARK_BROWN, (x_um + width_rect_um, y_um),
             (x_um + width_rect_um + width_polygon_um - width_polygon_um * (_ + 1) / 5, y_um + height_polygon_um))


# ship
def ship(x_ship, y_ship, width_ship, height_ship, width_mast, height_mast, width_sail):
    """
    :param x_ship: Координата левого верхнего угла корпуса по x
    :param y_ship: Координата левого верхнего угла корпуса по y
    :param width_ship: Ширина корпуса
    :param height_ship: Высота корпуса
    :param width_mast: Ширина мачты
    :param height_mast: Высота мачты
    :param width_sail: Ширина паруса
    """
    # находим координаты различных частей корабля
    # координаты носа
    ship_nose_coordinates = [(x_ship + width_ship, y_ship), (x_ship + width_ship + int(1 / 3 * width_ship), y_ship),
                             [x_ship + width_ship, y_ship + height_ship]]
    # координаты глаза корабля
    ship_eye_coordinates = (x_ship + width_ship + int(1 / 9 * width_ship), y_ship + int(0.4 * height_ship))
    # координаты паруса корабля
    ship_sail_coordinates = [(x_ship + int(0.4 * width_ship) + width_mast, y_ship - height_mast), (
        x_ship + int(0.4 * width_ship) + width_mast + width_sail, y_ship - int(0.5 * height_mast)),
                             (x_ship + int(0.4 * width_ship) + width_mast, y_ship), (
                                 x_ship + int(0.4 * width_ship) + width_mast + int(0.2 * width_sail),
                                 y_ship - int(0.5 * height_mast))]
    # координаты линии на парусе корабля
    ship_sail_line_coordinates = [(x_ship + int(0.4 * width_ship) + width_mast + width_sail + 1,
                                   y_ship - int(0.5 * height_mast)),
                                  [x_ship + int(0.4 * width_ship) + width_mast + int(0.2 * width_sail) - 1,
                                   y_ship - int(0.5 * height_mast)]]

    # рисует корпус корабля
    rect(screen, DARK_BROWN, (x_ship, y_ship, width_ship, height_ship))
    # рисует корму корабля
    circle(screen, DARK_BROWN, (x_ship, y_ship), height_ship)
    # рисует прямоугольник, закрывающий верхнюю часть кормы
    rect(screen, (0, 0, 255), (x_ship - height_ship, y_ship - height_ship, 2 * height_ship, height_ship))
    # рисует нос корабля
    polygon(screen, DARK_BROWN, ship_nose_coordinates)
    # рисует глаз корабля
    circle(screen, WHITE, ship_eye_coordinates, int(0.25 * height_ship))
    # рисует контур глаза корабля
    circle(screen, BLACK, ship_eye_coordinates, int(0.25 * height_ship) + 1, 1)
    # рисует мачту корабля
    rect(screen, BLACK, (x_ship + int(0.4 * width_ship), y_ship - height_mast, width_mast, height_mast))
    # рисует парус корабля
    polygon(screen, KHAKI, ship_sail_coordinates)
    # рисует контур паруса
    polygon(screen, DARK_BROWN, ship_sail_coordinates, 1)
    # рисует линию посередине паруса
    line(screen, DARK_BROWN, ship_sail_line_coordinates[0], ship_sail_line_coordinates[1])


# вызов функций, рисует все части картинки
background(LIGHT_BLUE, BLUE, SAND_YELLOW, 0, 320, 25)
sun(600, 60, 40)
cloud(150, 100, 20, 20, 10, 7)
cloud(100, 150, 25, 20, 10, 7)
cloud(300, 100, 35, 20, 10, 7)
umbrella(120, 260, 7, 200, 70, 40, PINK)
umbrella(220, 290, 3, 100, 35, 20, PINK)
ship(420, 250, 150, 35, 7, 100, 60)
ship(200, 220, 75, 15, 3, 50, 30)

########################################################################################################################

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
