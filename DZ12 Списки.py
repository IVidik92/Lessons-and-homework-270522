# Списки
# # 1
# lst = []
# for i in range(20):
#     if i == 0 or i == 19:
#         lst.append(1)
#     else:
#         lst.append(0)
# print(lst)
# # 2
# lst = []
# for i in range(5):
#     a = int(input('Введите число: '))
#     lst.append(a)
# print(lst)
# print(max(lst))
# # 3
# import random
# lst = []
# for i in range(10):
#     lst.append(random.randint(1, 1000))
# print(lst)
# # 4
# print()
# import random
# lst = []
# for i in range(10):
#     lst.append(random.randint(1, 1000))
# print(lst)
# lst1 = []
# lst2 = []
# for j in lst:
#     if j % 2 == 0:
#         lst2.append(j)
#     else:
#         lst1.append(j)
# print(lst2)
# print(lst1)
# 5
# lst1 = ['beer', 'potato', 'meat', 'milk', 'sugar', 'candy']
# lst2 = ['beer', 'banana', 'chocolate', 'milk', 'tea', 'candy', 'orange']
# for i in lst1:
#     for j in lst2:
#         if i == j:
#             print(j)
# # 6
# import random
# cent = random.randint(1,2)
# a = int(input('Орел или решка? '))
# k = 0
# i = 0
# while a != 0:
#     if a == cent:
#         print('Верно!')
#         cent = random.randint(1, 2)
#         a = int(input('Орел или решка? '))
#         k += 1
#         i += 1
#     else:
#         print('Не верно!')
#         cent = random.randint(1, 2)
#         a = int(input('Орел или решка? '))
#         i += 1
# else:
#     print('- - - +')
# print('Угадано', k, 'раз', k/i*100, 'процентов')
# # 7
# import random
# lst = []
# for i in range(10):
#     lst.append(random.randint(1, 100))
# true = True
# while true:
#     true = False
#     for i in range(len(lst) - 1):
#         if lst[i] > lst[i + 1]:
#             lst[i], lst[i + 1] = lst[i + 1], lst[i]
#             true = True
# print(lst)
# print()
# import random
# lst = []
# for i in range(10):
#     lst.append(random.randint(1, 100))
# lst.sort()
# print(lst)