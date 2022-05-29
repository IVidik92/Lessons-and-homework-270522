# a = 100 / 0
# print(a)
#
# print()
#
# try:
#     k = 1 / 0
# except ZeroDivisionError:
#     k = 0
# print(k)
#
# print()
#
# try:
#     k = 1 / 0
# except ArithmeticError:
#     k = 0
# print(k)
#
# print()
#
# try:
#     b = 2 + '1'
# except:
#     print("ERROR")
#
# print()
#
# my_dct = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dct['d']
# except KeyError:
#     print('Ключа не существует')
#
# print()
#
# my_list = [1, 2, 3, 4, 5]
# try:
#     my_list[6]
# except IndexError:
#     print("Этого индекса нет в списке!")
#
# print()
#
# my_dct = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dct['b']
# except KeyError:
#     print('Произошла ошибка KeyError!')
# else:
#     print('Ошибок не произошло!')
# finally:
#     print('Я выведусь в любом случае!')
#
# print()
#
# # Задание 1
# try:
#     num_1 = int(input('Введите первое число: '))
#     num_2 = int(input('Введите второе число: '))
#     a = num_1 / num_2
# except ZeroDivisionError:
#     print("Деление на ноль!")
# except ValueError:
#     print('Перепроверь что вводишь, пес!')
# else:
#     print('Результат в квадрате:', a**2)
# finally:
#     print("ФИНИШ!")
#
# print()
#
# Задание 2
try:
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    a = num_1 / num_2
    print(a)
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    print('Перепроверь что вводишь, пес!')
except Exception:
    print('Общее исключение')
print('Завершение программы')


# d = {1 : 2, 3 : 4}
# d.update({5 : 6})
# print(d)