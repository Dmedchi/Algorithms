# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from random import random
import timeit
import cProfile

def fnc(n):
    N = 10
    list_ = []
    for i in range(n):
        list_.append(int(random() * N) - n)
    number = 0
    index_ = -1
    while number < n:
        if list_[number] < 0 and index_ == -1:
            index_ = number
            return index_
        elif list_[number] < 0 and list_[number] > list_[index_]:
            index_ = number
            return index_
        number += 1


# print(timeit.timeit('spam = [i for i in range(10000)]', number=1000))
# 10 -    0.0029399996775673334
# 100 -   0.052538937408491415
# 10000 - 1.5564015341932516

# timeit:
# 10 loops, best of 3: 0.147 usec per loop
# 100 loops, best of 3: 0.0513 usec per loop
# 10000 loops, best of 3: 0.0358 usec per loop

cProfile.run('fnc(10000)')
#          10:
#  17 function calls in 0.001 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#   1     0.000    0.000    0.000    0.000 <string>:1(<module>)
#   1     0.000    0.000    0.000    0.000 task_4.py:10(<listcomp>)
#   1     0.000    0.000    0.000    0.000 task_4.py:9(often)
#   1     0.001    0.001    0.001    0.001 {built-in method builtins.exec}
#   2     0.000    0.000    0.000    0.000 {built-in method builtins.print}
#   1     0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   10    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}

#           100:
#  107 function calls in 0.002 seconds
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#   1      0.000    0.000    0.003    0.003 <string>:1(<module>)
#   1      0.000    0.000    0.000    0.000 task_4.py:10(<listcomp>)
#   1      0.002    0.002    0.003    0.003 task_4.py:9(often)
#   1      0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#   2      0.000    0.000    0.000    0.000 {built-in method builtins.print}
#   1      0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  100     0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}

#           10000:
#  20005 function calls in 0.081 seconds
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1      0.000    0.000    0.081    0.081 <string>:1(<module>)
#    1      0.046    0.046    0.081    0.081 task_5.py:11(fnc)
#    1      0.000    0.000    0.081    0.081 {built-in method builtins.exec}
#    1      0.030    0.030    0.030    0.030 {built-in method builtins.print}
#  10000    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#    1      0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  10000    0.002    0.000    0.002    0.000 {method 'random' of '_random.Random' objects}