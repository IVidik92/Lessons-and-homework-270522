#ОПРЕДЕЛИТЬ, ЯВЛЯЕТСЯ ЛИ ГОД ВИСОКОСНЫМ
a = int(input("Введите любой год: "))
if a % 400 == 0:
    print("Год високосный")
elif a % 100 == 0:
    print("Год не високосный")
elif a % 4 == 0:
    print("Год високосный")
else:
    print("Год не високосный")


#ОПРЕДЕЛИТЬ СУЩЕСТВОВАНИЕ ТРЕУГОЛЬНИКА И ЕГО ТИП
a = int(input("Введите первую сторону треугольника = "))
b = int(input("Введите вторую сторону треугольника = "))
c = int(input("Введите третью сторону треугольника = "))
if (a+b) > c and (a+c) > b and (b+c) > a:
    print("Треугольник существует")
    if a == b and a == c and b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольника не существует")


#ОПРЕДЕЛИТЬ ПРИНАДЛЕЖНОСТЬ ТОЧКИ К КРУГУ С ЦЕНТРОМ В НАЧАЛЕ КООРДИНАТ
x = float(input("Введите координату Х: "))
y = float(input("Введите координату У: "))
r = float(input("Введите радиус круга: "))
import math
s = math.sqrt(x**2 + y**2)
if s <= r:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")