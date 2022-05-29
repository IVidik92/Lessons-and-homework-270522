# Задание №1
a = int(input("Введите число: "))
arr = []
for i in range(1, a):
    if i % 2 != 0:
       arr.append(i)
print(arr)

print()

# Задание №2
a = ["Аретмий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
arr = []
for i in a:
    if a.index(i) % 2 == 0:
       arr.append(i)
print(arr)

print()

# Задание №3
a = input("Введите слово: ")
arr = []
for i in a:
    if a.count(i) == 1:
       arr.append(i)
print(arr)

print()

# Задание №4
import random
n = int(input("Введите количество чисел в списке: "))
list = []
for i in range(n):
    list.append(random.randint(1, 50))
print(list)
list.sort()
print(list)

print()

# Задание №5
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
