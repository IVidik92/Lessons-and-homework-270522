# num_set = {1, 2, 3, 4, 5}
# print(num_set)
#
# d = set()

# str_set = {'Max', 'Mike', 'Helen'}
# print(str_set)
#
# mixed_set = {2.0, 'Nicolas', (1, 2, 3)}
# print(mixed_set)
#
# num = [1, 2, 3, 4, 5, 6, 2, 5, 6]
# num_1 = set(num)
# print(num_1)

# days = set([1, 10, 33, 14, 5, 66, 17])
# for i in days:
#     print(i, end = " ")

# months = set(['Jan', 'March', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
# months.add('Febr')
# print(months)

# n = {1, 2, 3, 4, 5, 6}
# n.remove(4)
# n.discard(4)
# print(n)

# n = {1, 2, 3, 4, 5, 6}
# a = n.pop()
# print(n, a)
#
# months_a = set(['Jan', 'Febr', 'March', 'Apr', 'May', 'June'])
# months_b = set(['July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
# all = months_a.union(months_b)
# print(all)

# x = {1, 2, 3}
# y = {4, 3, 6}
# z = {7, 4, 9}
# all = x.union(y, z)
# print(all)

# months_a = set(['Jan', 'Febr', 'March', 'Apr', 'May', 'June'])
# months_b = set(['July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
# print(months_a | months_b)

# x = {1, 2, 3}
# y = {4, 3, 6}
# all = x.intersection(y)
# print(all)
#
# x = {1, 2, 3}
# y = {4, 3, 6}
# all = x & y
# print(all)

# # Задание 1
# import random
# a = []
# for i in range(10):
#     i += 1
#     a.append(random.randint(1, 100))
# print(a)
# num = set(a)
# if len(a) == len(num):
#     print('Дубликатов нет')
# else:
#     print('Дубликаты есть')
#
# print()
#
# # Задание 3
# a = [1, 3, 5, 7, 9]
# num_1 = set(a)
# num_2 = frozenset(a)
# un = num_1 | num_2
# print(un)
# inters = num_1 & num_2
# print(inters)
#
# print()
#
# # Задание 2
# dct = {'one': 1, 'two': 2, 'three': 3}
# print(dct)
# dct['str_key'] = 4
# print(dct)
# dct[(1, 2, 3)] = [4, 5, 6]
# print(dct)
# item = dct['two']
# print(item)
# item1 = dct.pop('three')
# print(item1)
# print(dct)
# keys = dct.keys()
# print(keys)