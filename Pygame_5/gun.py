from random import randrange as rnd, choice
import csv
import tkinter as tk
from tkinter import *
import math
import time
import copy

# print (dir(math))


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
timer = 0

'''ent = Entry(root, width=100)
lbl = Label(root, width=100)'''

class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 10
        self.vy = 0
        self.x_timer = 0
        self.y_timer = 0
        self.reduce_x_speed = False
        self.reduce_y_speed = False
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy

        if self.x > 790 or self.x < 10:
            self.vx = -self.vx
            self.vy /= 2
        if self.y > 590 or self.y < 10:
            self.vy = -self.vy
            self.vx /= 2

        self.vy -= 2
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

                Args:
                    obj: Обьект, с которым проверяется столкновение.
                Returns:
                    Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
                """
        if math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) < obj.r + self.r:
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        bullet - число выстрелов

        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 20:
                self.f2_power += 5
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.color = choice(['blue', 'green', 'red', 'yellow'])
        self.r = rnd(10, 50)
        self.x = rnd(610, 770)
        self.y = rnd(310, 540)
        self.vx = rnd(1, 2)
        self.vy = rnd(1, 2)
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def move_target(self):
        self.x -= self.vx
        self.y -= self.vy

        if self.x < 300 + self.r or self.x > 800 - self.r:
            self.vx = -self.vx
        if self.y < 300 + self.r or self.y > 550 - self.r:
            self.vy = -self.vy
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def new_target(self):
        """ Инициализация новой цели. """
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        # l1 = Label(root, text="Счёт:" + str(self.points),
        #          font="Arial 25")
        # l1.pack()
        # canv.itemconfig(self.id_points, text=self.points)

    def teleport(self):
        self.x = rnd(610, 770)
        self.y = rnd(310, 540)
        self.r = rnd(60, 80)
        self.vx = rnd(1, 2)
        self.vy = rnd(1, 2)


# t1 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
targets = []
for _ in range(5):
    targets.append(target())

message = StringVar()
message_entry = Entry(textvariable=message)
message_entry.pack()
message_entry.place(relx=.5, rely=.1, anchor="c")


def table_of_leaders():
    message_entry.insert(0, "")
    username = message.get()
    print("<"+username+">")
    with open('best_scores.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([username])


class ExitButton:
    def __init__(self):
        self.b = Button(text='Выход', width=10, height=3, font="Arial 10")
        self.b.bind('<Button-1>', self.exit_, table_of_leaders())
        self.b.pack()

    def change(self, event):
        self.b['fg'] = "red"
        self.b['activeforeground'] = "red"

    def dialog(self, event):
        root.configure(background='black')
        canv.itemconfig(screen1, text="Ваш счет: {}")

    def exit_(self, event):
        root.destroy()


ExitButton()

'''def score():
    canv.itemconfig(screen1, text="Счет : {}")
    # text_1 = font.render("Счет : {}".format(count), True, WHITE)
    # surface.blit(text_1, (0, 0))'''

'''
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
                username += events.unicode'''








def new_game(event=''):
    global gun, targets, screen1, balls, bullet, timer
    count = 0



    for i in targets:
        i.new_target()
        i.live = 1
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    """canv.bind('<Escape>', dialog)"""
    while True:
        for i in targets:
            for b in balls:
                b.move()
                if b.hittest(i) and i.live and timer > 30:
                    this_bullet = str(copy.copy(bullet))
                    i.live = 0
                    i.hit()
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + this_bullet + ' выстрелов')
                    count += 1
                    timer = 0
                    bullet = 0

                    i.teleport()
                    i.live = 1
                    canv.bind('<Button-1>', g1.fire2_start)
                    canv.bind('<ButtonRelease-1>', g1.fire2_end)
                    canv.bind('<Motion>', g1.targetting)

            canv.update()
            time.sleep(0.003)
            g1.targetting()
            g1.power_up()
            for i in targets:
                i.move_target()
            timer += 1
            if timer >= 40:
                canv.itemconfig(screen1, text='')
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)
    return count

l1 = Label(root, text="Счёт:" + str(new_game()),
           font="Arial 25")
# l1.config(bd=5, bg='#ffaaaa')
l1.place(relx=0.0,
         rely=1.0,
         anchor='sw')
l1.pack()

new_game()
root.mainloop()
