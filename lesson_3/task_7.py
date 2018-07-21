# 7.В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import random

list = []
for i in range(10):
    list.append(int(random() * 100))

print(list)

mn1 = min(list)
imn1 = list.index(mn1)

min1 = list.pop(imn1)

mn2 = min(list)

list.insert(imn1, min1)
imn2 = list.index(mn2)


print(f'\nMin1: {mn1} [{imn1}]')
print(f'Min2: {mn2} [{imn2}]')