# 'Выведите все квадраты натруальных чисел, не превосходящих числа N'
# N = int(input('Введите число: '))
# for i in range(1, N + 1):
#     print(i**2, end = ' ')
# print()
# a = int(input())
# summa = 0
# while a != 0:
#     summa += a % 10
#     a = a // 10
# print(summa)
# list tuple set dict frozenset frozendict str
s = "hello world"
# неизменяемые

#перебор итерируемого объекта
# for el in s:
#     print(el)
# for i in range(len(s)):
#     print(s[i])
# for ind, el in enumerate(s):
#     print(ind,el)

# tup = (5, 2, 5, (2, 4, 1), 2)
# for i in range(len(tup)):
#     if type(tup[i]) != int:
#         for j in range(len(tup[i])):
#             print(tup[i][j], end=" ")
#     else:
#         print(tup[i], end=" ")

# s1 = {4, 1, 51, 2, 1, 5}
# print(s1)
# lst = [4, "hello", {5, 1, 2}]
# print(lst)
# if 4 in lst:
#     print("yes")
# else:
#     print("no")
# d = {1: "value1", "key": {"key": 'value'}}
# print(d)
# исключения
# try:
#     s = 10/0
#     print(s)
# except TypeError:
#     print("error ;(")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# else:
#     print("else work")
# finally:
#     print("always work")
# except Exception as e:
#     print(type(e))

# name = input()
# if name.capitalize() == name:
#     print("hello "+name)
# else:
#     raise NameError("name is not correct")

# файлы
# with open("test.txt",'a') as f:
#     s = input()
#     f.write(s+"\n")
# lst = []
# with open("test.txt",'r') as f:
#     for line in f:
#         line = line.rstrip().split()
#         lst.extend(line)
    # s1 = f.read()
#
#     # print(repr(s1))
#     # # s1 = s1[:-1]
#     # s1 = s1.rstrip()
#     # s1 = s1.replace("\n"," ")
#     # print(repr(s1))
# print(lst)
# 1.Дан кортеж. Вывести все его совершенные числа.
# tup = (5, 2, 6, 16, 18, 28, 32)
# for i in range(len(tup)):
#     summa = 0
#     for j in range(1, tup[i]):
#         if tup[i] % j == 0:
#             summa += j
#     if summa == tup[i]:
#         print(f"{tup[i]} совершенное")
#
# проверка является ли число простым
# number = int(input())
# count = 0  # счётчик делителей
# for i in range(1, number + 1):
#     if number % i == 0:
#         count += 1
# if count == 2:
#     print("простое")
# else:
#     print("не простое")

#вывод строк
name = "ivan"
age = 21
print('name:',name.capitalize(),"age:",age)
print(f"name: {name.capitalize()} age: {age}")
print("name: {} age: {}".format(name.capitalize(),age))