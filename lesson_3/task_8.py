# 8.Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

matrix = []

for i in range(4):
    list = []
    summa = 0
    print(f'Строка {i + 1}: ')
    for k in range(4):
        number = int(input('>> '))
        summa += number
        list.append(number)
    list.append(summa)
    matrix.append(list)

for i in matrix:
    print(i)
