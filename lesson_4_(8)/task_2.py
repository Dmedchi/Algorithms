# 2.
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import random
import cProfile

# N = 10
# list_ = [0] * N

def fnc(n):
    lst = [int(random() * 10) for i in range(n)]
    index = []
    i = 0
    while i < n:
        if lst[i] % 2 == 0:
            index.append(i)
        i += 1
    return f'Массив: {lst}\nИндексы четных элементов: {index}'


# "task_2.fnc(10)"
# 100 loops, best of 3: 30.8 usec per loop

# "task_2.fnc(100)"
# 100 loops, best of 3: 247 usec per loop

# "task_2.fnc(1000)"
# 100 loops, best of 3: 2.37 msec per loop


cProfile.run('fnc(1000)')

#             10
# 22 function calls in 0.000 seconds

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_2.py:13(fnc)
#      1    0.000    0.000    0.000    0.000 task_2.py:14(<listcomp>)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     10    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}


#             100
#  151 function calls in 0.001 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:13(fnc)
#         1    0.000    0.000    0.000    0.000 task_2.py:14(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        46    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       100    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}


#             1000
# 1506 function calls in 0.003 seconds

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#      1    0.001    0.001    0.003    0.003 task_2.py:13(fnc)
#      1    0.001    0.001    0.002    0.002 task_2.py:14(<listcomp>)
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#    501    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
