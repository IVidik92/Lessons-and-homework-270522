# a = input("Введите фразу с боквой о: ")
# b = "о"
# c = ""
# for i in a:
#     if i != b:
#         c += i
# print(c)

for i in range(5):
    if i % 2 == 0:
        continue
    print(i)