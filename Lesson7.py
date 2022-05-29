# #1
# print("I", "like", "Python", sep = "***")
#
# print()

# #2
# name = input("Ввести имя: ")
# print("Привет", name, sep =", ", end = "!")

# #print()

# #3
# a = int(input("Ввести число: "))
# print(a+1, " - Следующее число")
# print(a-1, " - Предыдущее число")

# print()

# #4
# parol = input("Введите пароль: ")
# parol_check = input("Повторите: ")
# if parol == parol_check:
#     print("Пароль принят")
# else:
#     print("Пароли отличаются")

# print()

# #5
# number = int(input("Введите число: "))
# if number > 999 and number % 77 == 0 or number % 1717 == 0:
#     print("Yes")
# else:
#     print("NO")

# print()

# #6
# age = int(input("Введите возраст: "))
# sex = input("Пол ребенка (m - мальчик, f - девочка): ")
# if 10 <= age <= 15 and sex == "f":
#     print("YES")
# else:
#     print("NO")

# print()

# # 7
# color1 = input("Введите первый цвет: ")
# color2 = input("Введите второй цвет: ")
# if color1 == "красный":
#     if color2 == "синий":
#         print("фиолетовый")
#     elif color2 == "желтый":
#         print("оранжевый")
#     elif color2 == color1:
#         print("красный")
# elif color1 == "синий":
#     if color2 == "красный":
#         print("фиолетовый")
#     elif color2 == "желтый":
#         print("зеленый")
#     elif color2 == color1:
#         print("синий")
# elif color1 == "желтый":
#     if color2 == "красный":
#         print("оранжевый")
#     elif color2 == "синий":
#         print("зеленый")
#     elif color2 == color1:
#         print("желтый")
# else:
#     print("ERROR")
#
# print()
#
# #8
# num = int(input("Введите число: "))
# if num == 0:
#     print("Карман зеленый")
# elif 1 <= num <= 10:
#     if num % 2 == 0:
#         print("Карман черный")
#     else:
#         print("Карман красный")
# elif 11 <= num <= 18:
#     if num % 2 == 0:
#         print("Карман красный")
#     else:
#         print("Карман черный")
# elif 19 <= num <= 28:
#     if num % 2 == 0:
#         print("Карман черный")
#     else:
#         print("Карман красный")
# elif 29 <= num <= 36:
#     if num % 2 == 0:
#         print("Карман красный")
#     else:
#         print("Карман черный")
# else:
#     print("ERROR")
# print()

# #9
# a = int(input("Результат первого экзамена: "))
# b = int(input("Результат второго экзамена: "))
# c = int(input("Результат третьего экзамена: "))
# if a > 100 and b > 100 and c > 100:
#     print("ЛГУН")
# else:
#     summa = a + b + c
#     if summa >= 270:
#         print("Поступил")
#     else:
#         print("Не поступил")

# print()
#
# #10
# a = input("Введите название первого города: ")
# b = input("Введите название второго города: ")
# c = input("Введите название третьего города: ")
# s1 = min(len(a), len(b), len(c))
# s2 = max(len(a), len(b), len(c))
# if s1 == len(a):
#     print(a)
# elif s1 == len(b):
#     print(b)
# else:
#     print(c)
# if s2 == len(a):
#     print(a)
# elif s2 == len(b):
#     print(b)
# else:
#     print(c)
#
# print()
#
# #11
# a = input("Введите строку: ")
# if "синий" in a:
#     print("YES")
# else:
#     print("NO")
#
# print()
#
# #12
# adress = input("Введите электронный адрес: ")
# if "@" and "." in adress:
#     print("Корректный адрес")
# else:
#     print("Некорректный адрес")
# print()
#
# #13
#
# print()
#
# #14
# n = int(input("Длина катета: "))
# a = input("Символ: ")
# for i in range(n):
#     print(a * (n-i))
#
# print()
#
# #15
# n = int(input("Введите первое число: "))
# m = int(input("Введите второе число: "))
# if m > n:
#     for i in range(n, m+1):
#         print(i, end = " ")
# elif m < n:
#     for i in range(m, n+1):
#         print(i, end = " ")
# else:
#     print("m = n = ", m)
# print()
#
# #16
# n = int(input("Введите число на которое умножаем:"))
# for i in range(1, 11):
#     print(n, "*", i, "=", n*i)
#
# print()
#
# #17
# n = int(input("Вводи: "))
# a, b = 1, 1
# for i in range(n):
#     print(a, end = " ")
#     a, b = b, a + b
#
# print()
#
# #18
# n = int(input("Введите число: "))
# kol_vo_cifr = 0
# summa_cifr = 0
# proiz_cifr = 1
# last = n % 10
# sumfl = 0
# while n != 0:
#     last_digit = n % 10
#     kol_vo_cifr += 1
#     summa_cifr += last_digit
#     proiz_cifr *= last_digit
#     sr = summa_cifr / kol_vo_cifr
#     sumfl = last_digit + last
#     n = n // 10
# print(summa_cifr, kol_vo_cifr, proiz_cifr, sr, last_digit, sumfl, end = " ")
#
# print()
#
# # 19
# n = int(input("Введите число: "))
# if n <= 11:
#     print("ERROR")
# else:
#     for i in range(11, n+1):
#         if 55 <= i <= 99 or 1717 <= i <= 3737 or 7878 <= i <= 8787:
#             continue
#         print(i)
#
# print()
#
# # 20
# n = int(input("Введите число от 0 до 9: "))
# for i in range(1, n+1):
#     for j in range(1, 10):
#         print(i, " + ", j, " = ", i+j)
#
# print()
#
# #21
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# s = 0
# n = 0
# if a < b:
#     for i in range(a, b+1):
#         if i % 3 == 0:
#             s += i
#             n += 1
#     print(s / n)
# elif a > b:
#     for i in range(b, a+1):
#         if i % 3 == 0:
#             s += i
#             n += 1
#     print(s / n)
# else:
#     print("Введенные числа равны!!!")
#
# print()
#
# #22
# s = input("Введите текст: ")
# print(s.swapcase())
#
# print()
#
# #23
# c = input("Введите текст на английском языке: ")
# LowerCount = 0
# for i in range(len(c)):
#     if c[i] in "abcdefghijklmnopqrstuvwxyz":
#         LowerCount = LowerCount + 1
# print(LowerCount)
#
# print()
#
# #24
# t = input("Введите текст: ")
# print(t.replace("1", "one"))
#
# print()
#
# #25
# s = input("Введите текс: ")
# print(s[1:5])
#
# print()
#
# #26
# s = input("Введите текст: ")
# print(len(s))