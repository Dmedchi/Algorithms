# 3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random

N = 10
list_ = [0] * N

for i in range(N):
    list_[i] = int(random() * 100)
    print(list_[i], end='  ')

minimum = min(list_)
maximum = max(list_)

index_min = list_.index(minimum)
index_max = list_.index(maximum)

print(f'\nMin: {minimum} - [{index_min}]\nMax: {maximum} - [{index_max}]')

list_[index_min], list_[index_max] = list_[index_max], list_[index_min]

for i in range(10):
    print(list_[i], end='  ')



