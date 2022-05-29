#Перемножить все нечетные значения в интервале от 1 до 100
proiz = int(1)
for i in range(1, 100):
    if i % 2 != 0:
        proiz *= i
print(proiz)

#Записать в массив все числа в диапазоне от 1 до 500 кратные 5
arr = []
for i in range(1, 500):
    if i % 5 == 0:
        arr.append(i)
print(arr)

#Вывести на экран все чётные значения в диапазоне от 1 до 497
for i in range(1, 497):
    if i % 2 == 0:
        print(i)

#Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив
arr = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3]
arr1 = []
for i in arr:
    if arr.count(i) > 2:
        arr1.append(i)
    for j in arr1:
        if arr1.count(j) > 1:
            arr1.remove(j)
print(arr1)