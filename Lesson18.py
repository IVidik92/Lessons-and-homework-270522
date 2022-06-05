# def double(*args, **kwargs):
#     print(args)
#     print(kwargs.get('name'))
# double('hey', 'lol', 'kek', 'oru', name='masha', surname='burdo')

# def pass_exam(mark, **kwargs):
#     lst = []
#     # print(mark, kwargs)
#     for k, v in kwargs.items():
#         if v >= mark:
#             lst.append(k)
#             # print(k, v)
#     return lst
#
# students = pass_exam(3, masha = 4, sasha = 1, sergey = 9, olga = 7)
# print(students)
# написать функцию, которая принимает проходной балл
# и далее именованными аргументами имена учеников и баллы
# таких аргументо может быть много
# возвращает функция список имен сдавших

# # генератор списка
# def pass_exam(mark, **kwargs):
#     lst = [k for k, v in kwargs.items() if v >= mark]
#     return lst
#
# students = pass_exam(3, masha = 4, sasha = 1, sergey = 9, olga = 7)
# print(students)

# def summator(a, b):
#     return a + b
#
# x = lambda a, b: a + b
#
# print(summator(1, 2))
# print(x(1, 2))

# напсиать лямбла функцию которая принимает строки и букву и
# возвращает количество этой буквы в строке не считая регистра

# letters_num = lambda string, word: string.lower().count(word)
#
# print(letters_num('Hahaha', 'h'))

# написать функцию которая все запятые в тексте меняет на "блин"
# def ups_replace(string):
#     return string.replace(',', ' блин')

ups_replace = lambda string: string.replace(',', ' блин')

print(ups_replace('привет, я хотела сказать, что ты мне ок'))