def func(x):
    def add(a):
        return x + a
    return add

test = func(100)
print(test(200))

print()

def list1(l):
    l.append(1)
    return l
print(list1([1,2,3,4]))

print()

l = [1,2,3,4]
def list1():
    l.append(1)
    return l
print(list1())

print()

def list1(l: list, n: int) -> tuple:
    l.append(n)
    return tuple(l)

print()

# map(func, iterables)
a = [1, 2, 3, -1, -2, -3]
b = dict(map(lambda x: (x, x+1), a))
print(b)

print()

# вид функции, осуществляет отбор тех элементов итерируемого объекта, которые удовлетворяют условию
# принимает 2 обекта - функцию условие и итеррируемый объект
def uslovie(x):
    return x % 3 == 0
    # return x % 2 == 0
    # return x % 10 == 2
object = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(filter(uslovie, object))
# b = [i for i in object if i % 2 == 0]
print(b)

print()

# отфильтровать встроенные функции
a = [0, "", False, " ", "hello", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(filter(bool, a))  # bool -  не пустые значения
print(b)

print()

# отфильтровать по лямбде функции
a = ["а", "роза", "упала", "на", "лапу", "азора"]
b = list(filter(lambda x: len(x) <= 2, a))  # условие по длине строки
print(b)

print()

# отфильтровать по методу
a = "qwerty123456ASDFG"
# b = list(filter(str.isdigit, a)) # выбрать цифры
# b = list(filter(str.isalpha, a)) # выбрать буквы
b = list(filter(str.isupper, a))  # выбрать заглавные буквы
print(b)

print()

# фильтровать словари
d = {
    "minsk": 1949070,
    "gomel": 526901,
    "mogilev": 374713,
    "grodno": 361445,
    "vitebsk": 373859,
    "brest": 337445
}
b = list(filter(lambda x: d[x] > 500000, d))
c = list(filter(lambda x: d[x] < 375000, d))
print(b)
print(c)

print()

def test():
    for i in range(0, 10, 2):
        yield i
for i in test():
    print(i)

def max(x, y):
    if x > y:
        return x
    else:
        return y

print(max(2, 8))

a = [1, 2, 3, 4, 5]

def times_ten(x):
    return x * 10
l = list(map(times_ten, a))
print(l)

b = [1, 2, 3, 4, 5]

def check(y):
    return y > 2
lst = list(filter(check, b))
print(lst)

def decor(func):
    def wrap():
        print('========')
        func()
        print('========')
    return wrap

@decor
def show():
    print('FUCK OFF!!!')

show()