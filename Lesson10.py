# d = dict()
# d2 = {"one": 1, "two": 2}
# print(d2["one"])
# d2["three"] = 3
# print(d2)
# if "four" in d2:
#     print(d2["four"])
# else:
#     print("Такого нет")
#
# print(d2.items())
# print(d2.values())
# print(d2.keys())
# num = d2.pop("one")
# print(d2)
#
# d3 = {}
# lst = ["a", "b", "c"]
# d3 = d3.fromkeys(lst, "=")
# print(d3)
# del lst[0]
# print(lst)
#
# d3["some_dict"] = {1:"list", 2:True}
# print(d3)
#
# lst1 = ['p', 'y', 't', 'h', 'o', 'n']
# lst2 = [10, 20, 30, 40, 50, 60]
# lst3 = [True, False, True, False, True, False]
# zip_ = zip(lst1, lst2, lst3)
# for i in zip_:
#     print(i)
# zip_dict = print(dict(zip(lst1, lst2)))
# print(zip_dict)

# person = {'name': 'Neo', 'age': 150}
# person['city'] = 'Zeon'
# print(f"{person['name']} is {person['age']} old")

# for i in range(10):
#     print("Number is", i, "LOH")
# #1 Создайте словарь person, в котором будут присутствовать ключи name, age, city.
# # Выведите значение возраста из словаря person.
# person = {'name': 'Neo', 'age': 150, 'city': 'Zeon'}
# print(person['age'])
#
# print()
#
# #2 Значениями словаря могут быть и списки. Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
# # Выведите первое и последнее значения каждого из ключей.
# lst1 = ['M3', 'X5', 'X6']
# lst2 = ['T1', 'T2', 'T3']
# car = {'BMW': lst1, 'Tesla': lst2}
# print(car['BMW'][::2])
# print(car['Tesla'][::2])
#
# print()
#
# # 3 задание
# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
# print(d1["b"] == d2["b"])
#
# print()
#
# # 4 Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
# dct = {'a': 1, 'b': 3, 'c': 5, 'd': 7, 'e': 9}
# i = 1
# for key in dct:
#     i *= dct[key]
# print(i)
#
# print()
#
# # 5 Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка были ключами,
# # а элементы второго — соответственно значениями нашего словаря.
# lst1 = [1, 2, 3, 4, 5]
# lst2 = ['a', 'b', 'c', 'd', 'e']
# if len(lst1) == len(lst2):
#     dct = dict(zip(lst1, lst2))
#     print(dct)
# else:
#     print('NO')
#
# print()
#
# # 6 Создайте словарь из строки 'pythonist' следующим образом: в качестве ключей возьмите буквы строки,
# # а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
# word = 'pythonist'
# dct = {i: word.count(i) for i in word}
# print(dct)