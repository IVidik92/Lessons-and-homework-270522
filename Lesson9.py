# a = ('a', 'bc', 'def', 'ghij')
# item = a[2]
# print(item)
#
# print()
#
# b = (a, a[1], True)
# print(b)
# c = (1, [2, 3, 4], 'Text')
# print(c[1])
# print(c[1][0])
# c[1][1] = 8
# print(c)
#
# print()
#
# A = (2.5, ['a', True, 3.17], 8, False, 'z')
# B = ('Hello', 123)
# print(B[0][3])
#
# print()
#
# name, age, company = ('Tom', 37, 'Google')
# print(name)
# print(age)
# print(company)
# C = A +B
# print(C)
#
# print()
#
# A = ('mon', 'tue', 'wen', 'thu', 'fri', 'sat', 'sun')
# day = str(input("Введите день недели: "))
# if day in A:
#     num = A.index(day)
#     print(num+1)
# else:
#     print("Wrong day")
#
# print()
#
# A = ('ab', 'ac', 'ab', 'ab', 'ca', 'ad', 'jktl')
# d1 = A.count('ab')
# d2 = A.count('jktl')
# d3 = A.count('ca')
# print(d1)
# print(d2)
# print(d3)
#
# print()
#
# import random
# a = [random.randint(i, 100) for i in range(10)]
# a = tuple(a)
# print(a)
# print(a.index(min(a)), a.index(max(a)))
#
# print()
#
# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# c_1 = sum(C_1)
# c_2 = sum(C_2)
# if c_1 > c_2:
#     print('Сумма первого кортежа больше', c_1)
# else:
#     print('Сумма второго кортежа больше', c_2)
# print(C_1.index(min(C_1)), C_1.index(max(C_1)))
# print(C_2.index(min(C_2)), C_2.index(max(C_2)))
#
# print()
#
import random
a = [random.randint(i, 100) for i in range(10)]
print(a)
b = [(a[j], a[j + 1]) for j in range(0, len(a), 2)]
print(b)

import random
my_list = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список:', my_list)
answer = [(my_list[i_num], my_list[i_num + 1]) for i_num in range(0, len(my_list), 2)]
print('Новый список:', answer)