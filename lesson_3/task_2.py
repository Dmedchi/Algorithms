#  2.
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import random

N = 10
list_ = [0] * N
index_ = []

for i in range(N):
    list_[i] = int(random() * 100) + N
    if list_[i] % 2 == 0:
        index_.append(i)

print(f'Массив: {list_}')
print(f'Индексы четных элементов: {index_}')


