# a = str(input('Введите товар: '))
# ab = []
# while a != '':
#     with open('shop.txt', mode = 'a', encoding = 'utf-8') as file:
#         file.write(a + '\n')
#         ab.append(a)
#     a = str(input('Введите товар: '))
# else:
#     b = str(input('Какой товар хотите купить? '))
#     while b != '':
#         if b in ab:
#             with open('buy.txt', mode='a', encoding='utf-8') as file:
#                 file.write(b + '\n')
#             print('Товар добавлен в корзину покупок')
#         else:
#             print('Такого товара нет')
#         b = str(input('Какой товар хотите купить? '))
#     else:
#         print('Спасибо за заказ!')

# import os
# print(os.listdir(path = "."))
# print()
# name_dir1 = input("С каким именем создать директорию? ")
# print()
# os.mkdir(name_dir1)
# os.chdir(name_dir1)
# print()
# while True:
#     name_dir2 = input("С каким именем создать директорию? ")
#     if name_dir2 == '':
#         break
#     else:
#         os.mkdir(name_dir2)
# print()
# print(os.listdir(path = "."))
# print()
# name_dir3 = input("С каким именем удалить директорию? ")
# print(os.removedirs(name_dir3))