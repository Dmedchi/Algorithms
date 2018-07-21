# 9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

matrix = []
for i in range(4):
    list_ = []
    for k in range(5):
        number = int(random() * 100)
        list_.append(number)
    matrix.append(list_)

for i in matrix:
    print(i)

a = -1
for k in range(5):
    b = 100
    for i in range(4):
        # print(matrix[i][k])
        if matrix[i][k] < b:
            b = matrix[i][k]
    if b > a:
        a = b
# print('a', a)
print(f'Максимальный элемент среди минимальных: {a}')