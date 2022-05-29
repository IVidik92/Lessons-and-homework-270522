# number = int(input("Какое число ты загадал?: "))
# count = 0
# while True:
#     count += 1
#     attempt = int(input("Введите число: "))
#     if attempt < number:
#         print("Число меньше, чем нужно. Попробуй еще раз!")
#     if attempt > number:
#         print("Число больше, чем нужно. Попробуй еще раз!")
#     if attempt == number:
#         print("Вы угадали! Число попыток: ", count)
#         break
#
# print()
#
# number = int(input("Введите число: "))
# i1 = 0
# i2 = 0
# while number != 0:
#     if number < 0:
#         i1 += 1
#         number = int(input("Введите число: "))
#     if number > 0:
#         i2 += 1
#         number = int(input("Введите число: "))
# print("Количество положительных отзывов: ", i2)
# print("Количество отрицательных отзывов: ", i1)
#
# print()
#
# calls_wife = False
# count = 0
# hours = 0
# print("Начался рабочий день")
# for i in range(1, 9):
#     hours += 1
#     print(hours, "час")
#     zad = int(input("Сколько задач решит Максим?"))
#     count += zad
#     calls = int(input("Звонит жена. Взять трубку? (1 - да, 0 - нет)"))
#     if calls == 1:
#         calls_wife = True
# print("Рабочий день закончился. Всего задач выполнено: ", count)
# if calls_wife == True:
#     print("Нужно зайти в магазин")
#
# print()
#
N = int(input("Введите число: "))
s = 1
for i in range(1, N + 1):
    s *= i
print(s)