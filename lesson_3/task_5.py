# 5.
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from random import random

list = []

for i in range(10):
    list.append(int(random() * 10) - 10)
print(list)

number = 0
index = -1
while number < 10:
    if list[number] < 0 and index == -1:
        index = number
    elif list[number] < 0 and list[number] > list[index]:
        index = number
    number += 1

print(f'\nmax отрицательный элемент: {list[index]}')
print(f'       позиция:            [{index}]')

