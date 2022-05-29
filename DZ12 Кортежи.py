# Кортежи
# 1
# phone_numbers = ('+792345678', '+792345478', '+792355678', '+592345678', '+392345678', '+7923456558')
# for i in phone_numbers:
#     if '+7' in i:
#         print(i)
# # 2
# a = input('Введите оценки через запятую: ')
# lst = []
# for i in a:
#     if i != ',':
#         lst.append(int(i))
# b = tuple(lst)
# print(b)
# # 3
# a = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# for i in a:
#     print(*i, sep = ' - ')
# # 4
# print()
# import random
# a = []
# b = []
# for i in range(10):
#     a.append(random.randint(0, 5))
# for j in range(10):
#     b.append(random.randint(-5, 0))
# c = tuple(a) + tuple(b)
# print(c)
# print(c.count(0))
# 5
lst = []
line1 = input('Введите 1-ю символьную строку: ')
lst.append(line1)
line2 = input('Введите 2-ю символьную строку: ')
lst.append(line2)
line3 = input('Введите 1-ю последовательность из чисел: ')
line3 = tuple(line3.split(' '))
lst.append(line3)
line4 = input('Введите 2-ю последовательность из чисел: ')
line4 = tuple(line4.split(' '))
lst.append(line4)
print(lst)
lst = tuple(lst)
my_tuple_1 = lst[::2]
my_tuple_2 = lst[1::2]
print(my_tuple_1)
print(my_tuple_2)
if my_tuple_1 > my_tuple_2:
    print(my_tuple_1[0])
else:
    print(my_tuple_2[1])