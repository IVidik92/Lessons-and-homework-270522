dct = {'мясо': [10, 5], 'картошка': [2, 100], 'огурец': [3, 50], 'хлеб': [1, 44], 'птица': [5, 13]}
for key in dct:
    print(key, '-', dct[key][0], '-', dct[key][-1])
n = 'Да'
lst1 = []
lst2 = []
while n != 'Нет':
    name = input('Введите товар: ')
    if name in dct:
        amount = int(input('Введите количество: '))
        if amount <= dct[name][-1]:
            summa = amount * dct[name][0]
            print('Цена', name, '-', summa)
            dct[name][1] -= amount
            print('Осталось', dct[name][1], name)
            lst1.append(name)
            lst2.append(summa)
        else:
            print('Нет необходимого количества товара')
    else:
        print('Данного товара нет в наличии')
    n = input('Будем еще что покупать? (Да, Нет)')
lst = dict(zip(lst1, lst2))
print('Покупка выглядит так: ')
for key in lst:
    print(key, '-', lst[key])
print('Остаток продуктов в магазине: ')
for key in dct:
    print(key, '-', dct[key][0], '-', dct[key][-1])
print('Приходите еще!')