s = input("Введите любой текст: ")
print(s[2])     # третий символ строки
print(s[-2])    # предпоследний символ строки
print(s[:5])    # первых пять символов
print(s[0:-2])  # кроме последних двух символов
print(s[0::2])  # символы с четными индексами
print(s[1::2])  # символы с нечетными индексами
print(s[-1::-1])# символы в обратном порядке
print(s[-1::-2])# символы через один в обратном порядке
print(len(s))   # длина строки