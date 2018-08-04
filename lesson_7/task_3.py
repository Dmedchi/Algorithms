# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.

from random import random

N = 5
array = [int(random() * 100) for i in range(2*N + 1)]
print(array)

def mediana(array):
    center = len(array) // 2

    for i in range(len(array)):
        mn = i

        for j in range(i+1, len(array)):
            if array[j] < array[mn]:
                mn = j
        lst = array[mn]
        array[mn] = array[i]
        array[i] = lst
    print(array)
    print(f'медиана под индексом[{center}] - {array[center]}')

mediana(array)


