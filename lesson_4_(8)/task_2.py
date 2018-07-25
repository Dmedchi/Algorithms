# 4. Определить, какое число в массиве встречается чаще всего.

from random import random
import timeit
import cProfile

def often(n):
    lst = [int(random() * 10) for i in range(n)]
    print(lst)
    number = lst[0]
    max_number_of_times = 1

    for num in range(n):   #  1 число
        meeting = 1
        for second_number in range(num + 1, n):  # сравниваем с последующим
            if lst[num] == lst[second_number]:
                meeting += 1
        if meeting > max_number_of_times:
            max_number_of_times = meeting
            number = lst[num]
    if max_number_of_times > 1:
        print(f'{number} встречается {max_number_of_times} разa.')
    else:
        print('\nВсе числа уникальны.')


# print(timeit.timeit('spam = [i for i in range(1000)]', number=1000))
# 10 -  0.02360646799929065
# 100 - 0.10600193752720527
# 1000 - 0.44822903857906854

# timeit:
# 10 loops, best of 3: 0.147 usec per loop
# 100 loops, best of 3: 0.044 usec per loop
# 1000 loops, best of 3: 0.0359 usec per loop


cProfile.run('often(1000)')
#           10:
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
#   100    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}

#          1000:
# 1007 function calls in 0.358 seconds
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#   1      0.000    0.000    0.358    0.358 <string>:1(<module>)
#   1      0.356    0.356    0.358    0.358 task_4.py:8(often)
#   1      0.001    0.001    0.002    0.002 task_4.py:9(<listcomp>)
#   1      0.000    0.000    0.358    0.358 {built-in method builtins.exec}
#   2      0.000    0.000    0.000    0.000 {built-in method builtins.print}
#   1      0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  1000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}