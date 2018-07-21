# 6.В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import random

list1 = []
for i in range(10):
    list1.append(int(random() * 100))
print(list1)

mn = min(list1)
imn = list1.index(mn)
print(f'Min: {mn} [{imn}]')

mx = max(list1)
imx = list1.index(mx)
print(f'Max: {mx} [{imx}]')

list2 = list1[imn : imx]
if list2 == []:
    list2 = list1[imx : imn]

summa = sum(list2) - list2[0]
print(f'Сумма элементов между min и max: {summa}')

