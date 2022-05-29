# Словари
# 1
# person = {"name": "Kelly", "age": 25, "city": "New york"}
# print(person['age'])
# 2
# models_data = {"Tesla": ["Model S"]}
# models_data['Tesla'].append('Modes X')
# models_data['Tesla'].append('Modes Y')
# models_data.update({'BMW': ['M3', 'X5', 'X6'], 'ВАЗ': [2101, 2105, 2120]})
# print(models_data)
# 3
# a = input('Введите текст: ')
# my_list = a.split(' ')
# arr1 = []
# arr2 = []
# for i in my_list:
#     arr1.append(i)
#     arr2.append(my_list.count(i))
# dct = dict(zip(arr1, arr2))
# for key, value in dct.items():
#     print(f'{key}: {value}')
# 4
a = input('Введите текст: ')
my_list = a.split(' ')
arr1 = []
arr2 = []
for i in my_list:
    arr1.append(i)
    arr2.append(my_list.count(i))
dct = dict(zip(arr1, arr2))
print(dct)
print(arr1)
print(arr2)
for value in dct.values():
    print()

