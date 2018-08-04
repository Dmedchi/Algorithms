# 2.Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

N = 15
array = [int(random.randint(0, 50)) for i in range(N)]
print(array)


def sort_merge(array):

    if len(array) < 2:
        return array

    arr = len(array) // 2
    left = sort_merge(array[:arr])
    right = sort_merge(array[arr:len(array)])

    i = 0
    j = 0
    result = []

    while i < len(left) or j < len(right):
        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


new = sort_merge(array)
print(new)