# Задание 1
import random
a = [random.randint(0, 9) for i in range(10)]
a = tuple(a)
print(a)
print(sum(a))

print()

# Задание 2
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и','и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и')
print('т -', long_word.count('т'))
print('а -', long_word.count('а'))
print('и -', long_word.count('и'))