# 5.
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from random import random
N = 10
list_ = []

for i in range(N):
    list_.append(int(random() * N) - N)
print(list_)

number = 0
index_ = -1
while number < N:
    if list_[number] < 0 and index_ == -1:
        index_ = number
    elif list_[number] < 0 and list_[number] > list_[index_]:
        index_ = number
    number += 1

print(f'\nmax отрицательный элемент: {list_[index_]}')
print(f'       позиция:            [{index_}]')

