# Задание №1
num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(num[0:6])

print()

# Задание №2
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
summa = min(numbers) + max(numbers)
print(summa)

print()

# Задание №3
n = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
sa = sum(n) / len(n)
print(sa)

print()

# Задание №4
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3::3] = ["Зеленый", "Фиолетовый"]
print(rainbow)

print()

# Задание №5
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
languages.reverse()
print(languages)

print()

# Задание №6
numbers111 = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers111))
print(numbers111[-1])
numbers111.reverse()
print(numbers111)
if 5 and 17 in numbers111:
    print("YES")
else:
    print("NO")
numbers111.pop(0)
numbers111.pop()
print(numbers111)

print()

# Задание №7
numbers7 = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
sum7 = 0
for i in numbers7:
    sum7 += i**2
print(sum7)

print()

# Задание №8
numbers8 = [8, 9, 10, 11]
numbers8[1] = 17
a = [4, 5, 6]
numbers8.extend(a)
numbers8.pop(0)
numbers8 *= 2
numbers8.insert(3,25)
print(numbers8)

print()

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