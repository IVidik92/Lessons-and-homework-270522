# 1. Написать map-выражение, которое принимет список и возвращает множество (сет), в котором все элементы списка возведены во квадрат.
lst1 = [1, 2, 3, 4, 5]

def omg(x):
    return x ** 2

l = set(map(omg, lst1))
print(l)

print()

# 2. Написать фильтер-выражение, котрое принимает список строк и возвращает кортеж, содержащий только строки, где есть цифры.
# 2.1
lst2 = ['banana1', 'ap1ple', '1orange', 'strawberry', '1lemon']
lst22 = []
for i in lst2:
    if list(filter(str.isdigit, i)):
        lst22.append(i)
print(tuple(lst22))

print()

# 2.2
lst2 = ['banana1', 'ap1ple', '1orange', 'strawberry', '1lemon']
lst22 = []

def numbers(x):
    for i in x:
        if list(filter(str.isdigit, i)):
            lst22.append(i)

numbers(lst2)
print(tuple(lst22))

print()

# 3. Написать функцию-генератор, которая будет возращать по очереди элементы списка.
lst3 = ['banana1', 'ap1ple', '1orange', 'strawberry', '1lemon']

def gener(x):
    for i in x:
        yield i

for i in gener(lst3):
    print(i)