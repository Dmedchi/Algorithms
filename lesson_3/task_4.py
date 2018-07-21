# 4.
# Определить, какое число в массиве встречается чаще всего.

from random import random

list = [0] * 10

for i in range(10):
    list[i] = int(random() * 10)
print(list)

number = list[0]
max_number_of_times = 1

for num in range(10):   #  1 число
    meeting = 1

    for second_number in range(num + 1, 10):  # сравниваем с последующим
        if list[num] == list[second_number]:
            meeting += 1

    if meeting > max_number_of_times:
        max_number_of_times = meeting
        number = list[num]

if max_number_of_times > 1:
    print(f'\n{number} встречается {max_number_of_times} разa.')
else:
    print('\nВсе числа уникальны.')
