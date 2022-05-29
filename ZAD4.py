arr = ["Рыба", "Говядина", "Суп", "Мороженое"]
print(arr)
a = input("Введите блюдо которое не едите: ")
for i in arr:
    if i != a:
        continue
    else:
        print("Я не ем " + a)