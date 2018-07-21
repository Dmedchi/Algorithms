# 3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random

list = [0] * 10

for i in range(10):
    list[i] = int(random() * 100)
    print(list[i], end='  ')

minimum = min(list)
maximum = max(list)

index_min = list.index(minimum)
index_max = list.index(maximum)

print(f'\nMin: {minimum} - [{index_min}]\nMax: {maximum} - [{index_max}]')

list[index_min], list[index_max] = list[index_max], list[index_min]

for i in range(10):
    print(list[i], end='  ')



