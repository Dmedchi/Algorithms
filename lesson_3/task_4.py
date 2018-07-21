# 4.
# Определить, какое число в массиве встречается чаще всего.

from random import random

N = 10
list_ = [0] * N

for i in range(N):
    list_[i] = int(random() * N)
print(list_)

number = list_[0]
max_number_of_times = 1

for num in range(N):   #  1 число
    meeting = 1

    for second_number in range(num + 1, N):  # сравниваем с последующим
        if list_[num] == list_[second_number]:
            meeting += 1

    if meeting > max_number_of_times:
        max_number_of_times = meeting
        number = list_[num]

if max_number_of_times > 1:
    print(f'\n{number} встречается {max_number_of_times} разa.')
else:
    print('\nВсе числа уникальны.')
