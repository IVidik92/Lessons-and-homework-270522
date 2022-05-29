import random
a = str(random.randint(1, 10))
b = random.randint(1, 2)
if a == 1:
    cvet = "красный"
else:
    cvet = "черный"
s = a + " " + cvet
i = 1
while i <= 5:
    vvod = input("Введите номер от 1 до 10 и цвет (красный либо черный): ")
    if vvod == s:
        print("Вы выиграли!")
        break
    else:
        print("Не угадали!")
        i += 1
        continue
else:
    print("Вы проиграли!")
    print(s)