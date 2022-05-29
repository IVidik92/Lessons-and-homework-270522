# #1
# s = int(input("Введите длину в см: "))
# print(s // 100, " - целое значение длины в метрах")
#
# print()
#
# #2
# min = int(input("Введите интервал времени в минутах:"))
# hour = min // 60
# min -= 60*hour
# print(hour, "часов", min, "минут")
#
# print()
#
# #3
# s = int(input("Введите двузначное число: "))
# print(s // 10, "десятков", s % 10, "единиц")
#
# print()
#
# #4
# s = int(input("Введите число: "))
# if 10 <= s <= 99:
#     print(s // 10 + s % 10)
# else:
#     print("ERROR")
#
# print()
#
# #5
# s = int(input("Введите число: "))
# if 100 <= s <= 999:
#     print(s // 100, (s // 10) % 10, s % 10 , sep = " ,")
# else:
#     print("ERROR")
#
# print()
#
# #6
# s = int(input("Введите чило: "))
# a = s // 100
# b = (s // 10) % 10
# c = s % 10
# if 100 <= s <= 999:
#     if a != b and a != c and b != c:
#         print(a, b, c, sep = "")
#         print(a, c, b, sep="")
#         print(b, a, c, sep="")
#         print(b, c, a, sep="")
#         print(c, a, b, sep="")
#         print(c, b, a, sep="")
# else:
#     print("ERROR")
#
# print()
#
# #7
# s = int(input("Введите число: "))
# if 1000 <= s <= 9999:
#     print(s // 1000, (s // 100) % 10, (s // 10) % 10, s % 10 , sep = " ,")
# else:
#     print("ERROR")