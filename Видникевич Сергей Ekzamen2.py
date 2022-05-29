# # Задача 1
# lst = [1, 2, 3, 2, 4, 5, 1]
# lst1 = []
# for i in lst:
#     if lst.count(i) == 1:
#         lst1.append(i)
# print(lst1)
# print()
# # Задача 2
# lst = [1, 2, 3, 2, 4, 5, 1, 5, 4]
# count = 0
# for i in lst:
#     if lst.count(i) == 2:
#         lst.pop(i)
#         count += 1
# print(count)
# print()
# # Задача 3
# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# summa1 = sum(C_1)
# summa2 = sum(C_2)
# if summa1 > summa2:
#     print('Сумма больше в кортеже - C_1')
# else:
#     print('Сумма больше в кортеже - C_2')
# print(C_1.index(min(C_1)) + 1, 'элемент - минимальный в C_1;', C_1.index(max(C_1)) + 1, 'элемент- максимальный в C_1')
# print(C_2.index(min(C_2)) + 1, 'элемент - минимальный в C_2;', C_2.index(max(C_2)) + 1, 'элемент- максимальный в C_2')
# print()
# # Задача 4
# str = 'An apple a day keeps the doctor away'
# lst = []
# lst1 = []
# for i in str:
#     lst.append(i)
# for k in lst:
#     lst1.append(lst.count(k))
# d = dict(zip(lst, lst1))
# print(d)
# print()
# Задача 5
# dct = {'Торт': ['Яйца, Мука, Сахар, Сахар ванильный, Разрыхлитель, Какао-порошок, Бананы крупные, Сметана', 10, 5500],
#        'Пироженое': ['Шоколад темный, Масло сливочное, Яйцо куриное, Сахар, Мука, Коньяк', 5, 3300],
#        'Маффин': ['мука, миндаль, ореховая паста, яйца, сироп топинамбура, оливковое масло, ванильный экстракт, разрыхлитель, соль морская', 4, 950]}
# a = 'описание'
# b = 'цена'
# c = 'количество'
# name = input('Добрый день! Чего хотите? ')
# summa = 0
# if name in dct:
#     question = input('Что хотите узнать о товаре? (описание, цена, количество, все) ')
#     if question == a:
#         print(dct[name][0])
#     elif question == b:
#         print(dct[name][1])
#     elif question == c:
#         print(dct[name][-1])
#     else:
#         print(dct[name][0], ', цена -', dct[name][1], ', количество -', dct[name][-1])
#     n = 'Да'
#     while n != 'Нет':
#         buy = input('Что вы будете покупать? ')
#         if buy == 'Ничего':
#             print('С вас ', summa, 'рублей. До свидания!')
#         elif buy in dct:
#             amount = int(input('Введите количество: '))
#             if amount <= dct[buy][-1]:
#                 summa = amount * dct[buy][1]
#                 print('Цена', buy, '-', summa)
#                 dct[buy][-1] -= amount
#                 print('Осталось', dct[buy][-1], buy)
#             else:
#                 print('Нет необходимого количества товара')
#         else:
#             print('Данного товара нет в наличии')
#         n = input('Будем еще что покупать? (Да, Нет)')
#         print('Спасибо за покупку! Приходите еще')
# else:
#     print('Данного товара нет в наличии')
# print()
# Задача 6

print()
# # Задача 7
# try:
#     a = int(input('Введите певрое число: '))
#     b = int(input('Введите второе число: '))
#     c = a / b
# except ValueError:
#     print('Был введен текст вместо числа')
# except ZeroDivisionError:
#     while b == 0:
#         print('Деление на ноль!', 'Повторите ввод чисел заново!!!')
#         try:
#             a = int(input('Введите певрое число: '))
#             b = int(input('Введите второе число: '))
#         except ValueError:
#             print('Был введен текст вместо числа')
#             break
#     else:
#         c = a / b
#         print(c)
# else:
#     print(c)
# finally:
#     print('ФИНИШ')
# Задача 8
