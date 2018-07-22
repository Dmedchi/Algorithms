# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

number = int(input('>> '))

a = 1
summa = 0

for i in range(number):
    summa += a
    a /= -2
print(summa)
