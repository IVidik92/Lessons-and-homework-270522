#1
i = 0
while True:
    a = str(input("Введите любое слово: "))
    i += 1
    if a == "стоп" or a == "хватит" or a == "достаточно":
        break
print(i)

#2
a = int(input("Введите число: "))
arr = []
arr1 = []
while a >= 10:
    b = a % 10
    a //= 10
    arr.append(b)
    if a < 10:
        arr.append(a)
for i in arr:
    if arr.count(i) > 1:
        arr1.append(i)
if len(arr1) >= 1:
    print("В заданном числе есть одинаковые цифры")
else:
    print("В заданном числе нет одинаковых цифр")

#3
a = int(input("Введите цену за победу Ведьмака над чудовищем: "))
s1 = 25; s2 = 10; s3 = 5; s4 = 1; i1 = 0; i2 = 0; i3 = 0; i4 = 0
while a >= s1:
    a -= s1
    i1 += 1
print(i1, "монеты 25")
if a < s1:
    while a >= s2:
        a -= s2
        i2 += 1
print(i2, "монеты 10")
if a < s2:
    while a >= s3:
        a -= s3
        i3 += 1
print(i3, "монеты 5")
if a < s3:
    while a >= s4:
        a -= s4
        i4 += 1
print(i4, "монеты 1")
i = (i1 + i2 + i3 + i4)
print(i)

#4
sss = int(input("Введите кол-во денег на карте: "))
i = 0
if sss == 0:
    print("На карте 0")
else:
    while sss >= 0:
        a = int(input("Сумма покупки: "))
        sss -= a
        i += 1
        if sss < 0:
            sss = sss + a
            break
    print(sss, "осталось на карте")
    print(i-1, "покупок")

#5
arr = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
for i in arr:
    i = 0
    arr1 = arr[i:20:4]
    i += 1
    arr2 = arr[i:20:4]
    i += 1
    arr3 = arr[i:20:4]
    i += 1
    arr4 = arr[i:20:4]
print(arr1)
print(arr2)
print(arr3)
print(arr4)