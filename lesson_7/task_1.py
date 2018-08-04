# 1.Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.
import random


array = [int(random.randrange(-100, 100)) for i in range(20)]
print(array)


def sort_bubble(array):
    N = 20
    n = 1
    while n < N:
        for i in range(N - n):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n += 1


sort_bubble(array)
print(array)
