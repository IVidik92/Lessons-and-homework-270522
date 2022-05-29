a = 54
b = 9184
for i in range(a, b):
    if i % 5 == 0:
        print(i)


arr = ["Рыба", "Говядина", "Суп", "Мороженое"]
print(arr)
a = input("Введите блюдо которое не едите: ")
for i in arr:
    if i != a:
        continue
    else:
        print("Я не ем " + a)


arr = [1, 3, 5, 7, 9]
for i in arr:
    i += 1
print(i)

