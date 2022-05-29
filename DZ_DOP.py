# Задание №9
strochechka = str(input("Введите ряд чисел: "))
arr1 = []
arr2 = []
for i in strochechka:
    arr1.append(i)
for j in arr1:
    if j != " ":
        arr2.append(j)
arr2.sort()
print(arr2)
arr2.sort(reverse = True)
print(arr2)

print()

# Задание №10
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
qwerty = [len(i) for i in keywords]
print(qwerty)