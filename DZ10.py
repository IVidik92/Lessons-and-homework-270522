try:
    a = int(input('Введите певрое число: '))
    b = int(input('Введите второе число: '))
    c = a / b
except ValueError:
    print('Был введен текст вместо числа')
except ZeroDivisionError:
    while b == 0:
        print('Деление на ноль!', 'Повторите ввод чисел заново!!!')
        try:
            a = int(input('Введите певрое число: '))
            b = int(input('Введите второе число: '))
        except ValueError:
            print('Был введен текст вместо числа')
            break
    else:
        c = a / b
        print(c)
else:
    print(c)
finally:
    print('ФИНИШ')