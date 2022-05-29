#1
a1 = input("Введите город вылета: ")
a2 = input("Введите город прилета: ")
print(a1, a2, sep = "-")

print()

#2
a = input("Введите текст: ")
print(a.title())

print()

#3
import random
a = str(random.randint(0, 10))
i = 0
vvod = input("Введите число от 0 до 10: ")
while vvod != a:
    if vvod < a:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
        vvod = input("Введите число от 0 до 10: ")
        i += 1
    elif vvod > a:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
        vvod = input("Введите число от 0 до 10: ")
        i += 1
else:
    i += 1
    print("Вы угадали!", "Число попыток: ", i)

print()

#4
sum = int(input("Введите количество должников: "))
sum_dolg = 0
for i in range(0, sum+1, 5):
    print("Должник с номером ", i)
    dolg = int(input("Сколько вы должны? "))
    sum_dolg += dolg
print("Общая сумма долга: ", sum_dolg)