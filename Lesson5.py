# Пример из лекции
i = 1
result = 0
while i <= 50:
    result += i
    i += 1
print(result)

print()

# Задача №1 из леции
i = 1
while i <= 10:
    print(i**2)
    i += 1

print()

# Задача №2 из лекции
i = 1
result = 1
while i <= 125:
    if i % 2 == 0:
        result *= i
    i += 1
print(result)

print()

# Задача №3 из лекции
i = 0
while i <= 15:
    print(15 - i)
    i += 1

print()

# Задача №4 из лекции
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a < b and a < 0 and b > 0:
    a += 1
    while a < 0:
        print(a)
        a += 1
elif a < b and a < 0 and b < 0:
    a += 1
    while a < b:
        print(a)
        a += 1
elif b < a and b < 0 and a > 0:
    b += 1
    while b < 0:
        print(b)
        b += 1
elif b < a and b < 0 and a < 0:
    b += 1
    while b < a:
        print(b)
        b += 1
else:
    print("Введены все положительные числа")

print()

# Задача №5 из лекции
i = 0
arr = []
while i <= 98:
    print(i)
    i += 7
    if i < 100:
        arr.append(i)
else:
    print(arr)
    print(len(arr))

print()

# Задача №6 из лекции
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input("Введите математическое действие: ")
while True:
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        if b == 0:
            print("Деление на ноль!")
        else:
            print(a/b)
    break

print()

#Задача №7 из лекции
arr = [2, 3, 4, 5, 6, 7, 8]
arrchet = []
arrnechet = []
for i in arr:
    if i % 2 == 0:
        arrchet.append(i)
    else:
        arrnechet.append(i)
ac = len(arrchet)
anc = len(arrnechet)
if ac > anc:
    print("Четных больше")
    sum_arr = int()
    for j in arr:
        sum_arr += j
    print(sum_arr)
else:
    print("Нечетных больше")
    pr_arr = int(1)
    for k in arr:
        pr_arr = arr[0]*arr[2]*arr[6]
    print(pr_arr)