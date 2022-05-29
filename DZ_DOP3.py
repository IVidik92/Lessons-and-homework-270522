# my_list = ['apple', 'banana', 'pineapple']
# print(', '.join(my_list))
#
# my_list1 = 'apple, banana, pineapple'
# print(my_list1.split(', '))
#
# my_list = ['apple', 'banana', 'pineapple']
# print('_____'.join(my_list))
#
# lst = [8, 9, 4, 7, 'a']
# dct = dict(zip(lst, lst))
# print(dct)

dct = {'Торт': ['Яйца, Мука, Сахар, Сахар ванильный, Разрыхлитель, Какао-порошок, Бананы крупные, Сметана', 10, 5500],
       'Пироженое': ['Шоколад темный, Масло сливочное, Яйцо куриное, Сахар, Мука, Коньяк', 5, 3300],
       'Маффин': ['мука, миндаль, ореховая паста, яйца, сироп топинамбура, оливковое масло, ванильный экстракт, разрыхлитель, соль морская', 4, 950]}
a = 'описание'
b = 'цена'
c = 'количество'
name = input('Добрый день! Чего хотите? ')
summa = 0
if name in dct:
    question = input('Что хотите узнать о товаре? (описание, цена, количество, все) ')
    if question == a:
        print(dct[name][0])
    elif question == b:
        print(dct[name][1])
    elif question == c:
        print(dct[name][-1])
    else:
        print(dct[name][0], ', цена -', dct[name][1], ', количество -', dct[name][-1])
    n = 'Да'
    while n != 'Нет':
        buy = input('Что вы будете покупать? ')
        if buy == 'Ничего':
            print('С вас ', summa, 'рублей. До свидания!')
        elif buy in dct:
            amount = int(input('Введите количество: '))
            if amount <= dct[buy][-1]:
                summa = amount * dct[buy][1]
                print('Цена', buy, '-', summa)
                dct[buy][-1] -= amount
                print('Осталось', dct[buy][-1], buy)
            else:
                print('Нет необходимого количества товара')
        else:
            print('Данного товара нет в наличии')
        n = input('Будем еще что покупать? (Да, Нет)')
        print('Спасибо за покупку! Приходите еще')
else:
    print('Данного товара нет в наличии')