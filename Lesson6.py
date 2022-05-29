number = [1, 2, 3, [1, 2, 3], 4, 5]
print(number)
languages = ["кот", "дом", "слон"]
print(languages)

num = [1, 3, ["кот", "дом"], 5]
print(num)
num1 = list("Привет")
print(num1)
print(len(number))
if 6 in number:
    print("Yes")
else:
    print("No")
print(number[-1])
print([1, 2, 3] + [4, "Hi, Peter", 6])
print([1, 2, 3] * 3)
print(sum(number[4]))

a = int(input("введите число: "))
arr = list(range(1, a + 1, 2))
print(arr)


b = [2, 4, 3, 6, 7, 4, 3, 8]
c = []
for i in b:
    if b.count(i) == 1:
        c.append(i)
print(c)

slovo = input("Vvedite slovo: ")
uniq = []
for i in slovo:
    if slovo.count(i) == 1:
        uniq.append(i)
print(uniq)


IMENA = ["Артем", "Коля", "Антон", "Сергей"]
qw =[]
for i in IMENA:
    if IMENA.index(i) % 2 == 0:
        qw.append(i)
print(qw)


A = [[1, 2, 3], [4, 5, 6]]
for i in A:
    for elem in i:
        print(elem, end = " ")
    print()
s = 0
for i in A:
    for elem in i:
        s += elem
print(s)
num = [1, 2, 3, 4, 5, 6]
add = [7, 8, 9]
num.extend(add)
print(num)

z = [0 for i in range(10)]
print(z)


fruits = ["apple", "orange", "banana", "pineapple", "lemon", "kiwi", "cherry"]
fruits[2:5] = ["банан", "ананас", "лимон"]
print(fruits)