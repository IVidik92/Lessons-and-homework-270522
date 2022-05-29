# # Дан кортеж. Написать программу, определяющую сколько раз менялся знак в кортеже.
# import math; import random
# tup = []
# for a in range(5):
#     tup.append(random.randint(-50, 50))
# print(tuple(tup))
# lst0 = []
# lst = []
# for k in tup:
#     if k != 0:
#         lst0.append(k)
#     else:
#         k = 1
#         lst0.append(k)
# count = 0
# for i in lst0:
#     a = int(math.fabs(i) / i)
#     lst.append(a)
# lst = tuple(lst)
# for j in range(len(lst) - 1):
#     if lst[j] != lst[j +1]:
#         count += 1
# print(count)
# print()
# Альтернативный вариант
# for j in range(len(lst)-1):
#     if (lst[j] > 0 and lst[j + 1] < 0) or (lst[j] < 0 and lst[j + 1] > 0):
#         count += 1
# print(count)

# # Дан кортеж. Посчитать сумму элементов между максимальным и минимальным не включая эти элементы.
# import random
# tup = []
# for i in range(5):
#     tup.append(random.randint(0, 50))
# tup = tuple(tup)
# print(tup)
# mini = tup.index(min(tup))
# maxi = tup.index(max(tup))
# if maxi < mini:
#     tup1 = tup[maxi + 1:mini]
# else:
#     tup1 = tup[mini + 1:maxi]
# print(sum(tup1))
# print()

# # Задан список из k чисел. Определить количество инверсий в списке
# # (т. е. таких пар элементов, в которых большее число находится слева от меньшего).
# import random
# k = int(input('Введите количество элементов в списке: '))
# lst = []
# for i in range(k):
#     lst.append(random.randint(0, 50))
# print(lst)
# count = 0
# for j in range(len(lst) - 1):
#     if lst[j] > lst[j + 1]:
#         count += 1
# print(count)
# print()

# # Дан список . Продублировать все неповторяющиеся элементы.
# import random
# lst = []
# arr = []
# N = int(input('Введите количество элементов в списке: '))
# for i in range(N):
#     lst.append(random.randint(0, 50))
# print(lst)
# for j in lst:
#     el = lst.count(j)
#     if el == 1:
#         arr.append(j)
# print(arr)
# print(lst + arr)
# print()

# # Во входной строке записана последовательность чисел через пробел.
# # Для каждого числа выведите слово YES (в отдельной строке),
# # если это число ранее встречалось в последовательности или NO, если не встречалось.
# input_numbers = [int(i) for i in input('Введите числа через пробел: ').split()]
# print(input_numbers)
# double = set()
# for j in input_numbers:
#     if j in double:
#         print('YES')
#     else:
#         print('NO')
#         double.add(j)
# print()
#
# # Даны два списка чисел. Найдите все числа, которые не содержатся одновременно в этих двух списках.
# import random
# lst1 = []
# lst2 = []
# for i in range(10):
#     lst1.append(random.randint(1, 20))
#     lst2.append(random.randint(1, 20))
# print(lst1)
# print(lst2)
# lst = lst1 + lst2
# lst0 = [i for i in range(1, 21)]
# st = []
# for i in lst0:
#     if i not in lst:
#         print(i, end = ' ')
# print()

# # Создайте словарь, связав его с переменной school...
# import random
# N = int(input('Введите количество 9-х классов: '))
# classroom = []
# students = []
# alfavit = []
# for i in range(65, 65 + N):
#     alfavit.append(chr(i))
# for j in alfavit:
#     classroom.append('9' + j)
# for k in range(N):
#     students.append(random.randint(16, 31))
# school = dict(zip(classroom, students))
# print(school)
# # a
# classroom_change = input('Введите класс, в котором изменилось количество учеников: ')
# if classroom_change in school:
#     school[classroom_change] = random.randint(16, 31)
#     print(school)
# else:
#     print('Такого класса в школе нет!')
# # b
# for i in range(65 + N, 65 + N + 1):
#     alfavit.append(chr(i))
#     school['9' + alfavit[-1]] = random.randint(16, 31)
# print(school)
# # c
# classroom_change = input('Введите класс, который был расформирован: ')
# if classroom_change in school:
#     del school[classroom_change]
#     print(school)
# else:
#     print('Такого класса в школе нет!')
# # d
# sum = 0
# for value in school.values():
#     sum += value
# print('Количество учащихся в 9-х классах -', sum)
# print()

# Вам дан словарь, состоящий из пар слов...
import random
with open('synonim', mode = 'r', encoding = 'utf-8') as file:
    text = file.read().split()
with open('synonim1', mode = 'r', encoding = 'utf-8') as file:
    text1 = file.read().split()
N = random.randint(1, 10)
syn1 = text[:N]
syn2 = text1[:N]
dct = dict(zip(syn1, syn2))
print(dct)
syn = input('Введите слово-синоним: ')
if syn in dct:
    print(dct[syn])
elif syn not in dct:
    dct = dict(zip(syn2, syn1))
    if syn in dct:
        print(dct[syn])
    else:
        print('Введенного слова нет в словаре')

