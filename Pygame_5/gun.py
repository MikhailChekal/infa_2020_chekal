from random import randrange as rnd, choice
import tkinter as tk
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
        '''if self.reduce_x_speed:
            self.x_timer += 1
        if self.reduce_x_speed:
            self.y_timer += 1
        self.x += self.vx
        self.y -= self.vy
        if self.x > 790 or self.x < 10:
            self.reduce_x_speed = True
            self.x_timer = 0
            self.vx = -self.vx
        if self.y > 590 or self.y < 10:
            self.reduce_y_speed = True
            self.y_timer = 0
            self.vy = -self.vy
        elif self.reduce_x_speed and self.x_timer >= 3:
            self.vx *= .1
            self.reduce_x_speed = False
            self.x_timer = 0
        elif self.reduce_y_speed and self.y_timer >= 3:
            self.vx *= .1
            self.reduce_x_speed = False
            self.x_timer = 0'''

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
            if self.f2_power < 40:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.color = 'red'
        self.r = rnd(60, 80)
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

        if self.x < 600 or self.x > 780:
            self.vx = -self.vx
        if self.y < 300 or self.y > 550:
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
        canv.itemconfig(self.id_points, text=self.points)

    def teleport(self):
        self.x = rnd(610, 770)
        self.y = rnd(310, 540)
        self.r = rnd(60, 80)
        self.vx = rnd(1, 2)
        self.vy = rnd(1, 2)


t1 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
'''targets = []
for _ in range(2):
    targets.append(target())'''


def new_game(event=''):
    global gun, t1, screen1, balls, bullet, timer
    t1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    while t1.live or balls:
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live and timer > 30:
                this_bullet = str(copy.copy(bullet))
                t1.live = 0
                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + this_bullet + ' выстрелов')
                timer = 0
                bullet = 0

                t1.teleport()
                t1.live = 1
                canv.bind('<Button-1>', g1.fire2_start)
                canv.bind('<ButtonRelease-1>', g1.fire2_end)
                canv.bind('<Motion>', g1.targetting)

        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
        t1.move_target()
        timer += 1
        if timer >= 40:
            canv.itemconfig(screen1, text='')
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()
root.mainloop()
