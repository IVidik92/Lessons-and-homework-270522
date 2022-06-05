import turtle
import random

def draw_square(side):
    for i in range(n):
        t.forward(side)
        t.left(a)

def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()

colors = ['red', 'blue', 'green', 'orange', 'pink', 'black', 'brown']
t = turtle.Pen()
t.width(5)
for i in range(10):
    n = random.randint(3, 11)
    a = 180 - (n - 2) * 180 / n
    t.color(random.choice(colors))
    x_cor = random.randint(-100, 100)
    y_cor = random.randint(-100, 100)
    move(x_cor, y_cor)
    draw_square(random.randint(10, 50))

turtle.mainloop()