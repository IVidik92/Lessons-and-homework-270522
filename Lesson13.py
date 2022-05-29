# file = open('file.txt', mode = 'r', encoding = 'utf-8')
# text = file.read()
# print(text)
# file.close()

# with open('file.txt', mode = 'r', encoding = 'utf-8') as file:
#     text = file.read()
#     print(text)

# with open('file.txt', mode = 'r', encoding = 'utf-8') as file:
#     text = file.readlines() # считывает строки
#     print(text, type(text))

# with open('file.txt', mode = 'r', encoding = 'utf-8') as file:
#     text = file.read().split('\n')
#     print(text, type(text))

# with open('file.txt', mode = 'w', encoding = 'utf-8') as file:
#     text = file.write('Хорошего дня')
#     print(text, type(text))

# with open('file.txt', mode = 'w', encoding = 'utf-8') as file:
#     text = file.writelines(['Хорошего дня\n', 'bye\n'])
#     print(text, type(text))

# with open('file.txt', mode = 'a', encoding = 'utf-8') as file:
#     text = file.write('Хорошего дня')

# with open('shop.txt', mode = 'a', encoding = 'utf-8') as file:
#     while True:
#         a = str(input('Введите товар: '))
#         if a == '':
#             break
#         file.write(a + '\n')

# a = str(input('Введите товар: '))
# while a != '':
#     with open('shop.txt', mode='a', encoding='utf-8') as file:
#         file.write(a + '\n')
#     a = str(input('Введите товар: '))
# else:
#     print('Конец')

# import os
# name = os.getcwd()
# print(name)
# os.chdir('..')
# name = os.getcwd()
# print(name)
# os.chdir('LessonPYTHON')
# name = os.getcwd()
# print(name)
