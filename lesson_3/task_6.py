# 6.В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import random

list = []
for i in range(10):
    list.append(int(random() * 100))
print(list)

mn = min(list)
imn = list.index(mn)
print(f'Min: {mn} [{imn}]')

mx = max(list)
imx = list.index(mx)
print(f'Max: {mx} [{imx}]')

list2 = list[imn : imx]
if list2 == []:
    list2 = list[imx : imn]

summa = sum(list2) - list2[0]
print(f'Сумма элементов между min и max: {summa}')

