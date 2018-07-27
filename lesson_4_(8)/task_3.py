# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import timeit
import cProfile

def fnc(n):
    # N = 10
    list_ = [random.randint(n * -10, n * 10) for number in range(n)]
    # for i in range(n):
        # list_.append(int(random() * N) - n)
    number = 0
    index = -1
    while number < n:
        if list_[number] < 0 and index == -1:
            index = number
            # return index
        elif list_[number] < 0 and list_[number] > list_[index]:
            index = number
            # return index
        number += 1
    return f'\nmax отрицательный элемент: {list_[index]}\nпозиция: [{index}]'



# "task_3.fnc(10)"
# 100 loops, best of 3: 85 usec per loop

# "task_3.fnc(100)"
# 100 loops, best of 3: 699 usec per loop

# "task_3.fnc(1000)"
# 100 loops, best of 3: 7.68 msec per loop

# cProfile.run('fnc(10000)')
#          10:
#   56 function calls in 0.000 seconds

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        10    0.000    0.000    0.000    0.000 random.py:173(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:217(randint)
#        10    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.000    0.000 task_3.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_3.py:8(fnc)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        11    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


#           100:
#  509 function calls in 0.005 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#       100    0.004    0.000    0.004    0.000 random.py:173(randrange)
#       100    0.000    0.000    0.004    0.000 random.py:217(randint)
#       100    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.005    0.005 task_3.py:10(<listcomp>)
#         1    0.000    0.000    0.005    0.005 task_3.py:8(fnc)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       104    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


#           10000:
#  53042 function calls in 0.190 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.190    0.190 <string>:1(<module>)
#     10000    0.054    0.000    0.118    0.000 random.py:173(randrange)
#     10000    0.020    0.000    0.138    0.000 random.py:217(randint)
#     10000    0.025    0.000    0.065    0.000 random.py:223(_randbelow)
#         1    0.043    0.043    0.181    0.181 task_3.py:10(<listcomp>)
#         1    0.008    0.008    0.189    0.189 task_3.py:8(fnc)
#         1    0.000    0.000    0.190    0.190 {built-in method builtins.exec}
#     10000    0.003    0.000    0.003    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     13037    0.037    0.000    0.037    0.000 {method 'getrandbits' of '_random.Random' objects}