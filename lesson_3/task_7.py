# 7.В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import random

list_ = []
for i in range(10):
    list_.append(int(random() * 100))

print(list_)

mn1 = min(list_)
imn1 = list_.index(mn1)

min1 = list_.pop(imn1)

mn2 = min(list_)

list_.insert(imn1, min1)
imn2 = list_.index(mn2)


print(f'\nMin1: {mn1} [{imn1}]')
print(f'Min2: {mn2} [{imn2}]')