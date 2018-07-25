# 5.Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

import cProfile
import timeit

def matrix(n):
    count = 0
    for i in range(n):
        print(f' {i}-{chr(i)} | ', end='')
        count += 1
        if count % 10 == 0:
            print()

# print(timeit.timeit('spam = [i for i in range(100)]', number=1000))
# 10 -   0.0025376916459161703
# 100 -  0.03062743931304255
# 1000 - 0.3604174330549176

# timeit:
# 10 loops, best of 3: 0.0733 usec per loop
# 100 loops, best of 3: 0.044 usec per loop
# 1000 loops, best of 3: 0.0366 usec per loop


cProfile.run('matrix(100)')
#           10:
#   25 function calls in 0.000 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#   1     0.000    0.000    0.000    0.000 <string>:1(<module>)
#   1     0.000    0.000    0.000    0.000 task_5.py:8(matrix)
#   10    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#   1     0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#   11    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#   1     0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#           100:
#    214 function calls in 0.001 seconds
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1     0.000    0.000    0.001    0.001 <string>:1(<module>)
#    1     0.000    0.000    0.001    0.001 task_5.py:8(matrix)
#   100    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#    1     0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#   110    0.001    0.000    0.001    0.000 {built-in method builtins.print}
#    1     0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#          1000:
#  2104 function calls in 0.061 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#   1      0.000    0.000    0.061    0.061 <string>:1(<module>)
#   1      0.005    0.005    0.061    0.061 task_5.py:8(matrix)
#  1000    0.001    0.000    0.001    0.000 {built-in method builtins.chr}
#   1      0.000    0.000    0.061    0.061 {built-in method builtins.exec}
#  1100    0.055    0.000    0.055    0.000 {built-in method builtins.print}
#   1      0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

