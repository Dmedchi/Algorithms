# 5.Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
import random
import cProfile
import timeit

def matrix(n):
    array = [random.randint(32, 128) for i in range(n)]
    i = 0
    while i < n:
        i += 1
        if array[i] % 10 == 0:
            return ' '

        return f' {i}-{chr(i)} | '
        # print(f' {i}-{chr(i)} | ', end='')


# "task_1.matrix(10)"
# 100 loops, best of 3: 58.8 usec per loop

# "task_1.matrix(100)"
# 100 loops, best of 3: 550 usec per loop

# "task_1.matrix(1000)"
# 100 loops, best of 3: 6.01 msec per loop


# cProfile.run('matrix(1000)')
#           10:
#   57 function calls in 0.000 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        10    0.000    0.000    0.000    0.000 random.py:173(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:217(randint)
#        10    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.000    0.000 task_1.py:8(matrix)
#         1    0.000    0.000    0.000    0.000 task_1.py:9(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


#           100:
#    544 function calls in 0.001 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       100    0.000    0.000    0.001    0.000 random.py:173(randrange)
#       100    0.000    0.000    0.001    0.000 random.py:217(randint)
#       100    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.001    0.001 task_1.py:8(matrix)
#         1    0.000    0.000    0.001    0.001 task_1.py:9(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       139    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


#          1000:
#   5338 function calls in 0.009 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#      1000    0.003    0.000    0.006    0.000 random.py:173(randrange)
#      1000    0.001    0.000    0.007    0.000 random.py:217(randint)
#      1000    0.002    0.000    0.003    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.009    0.009 task_1.py:8(matrix)
#         1    0.001    0.001    0.008    0.008 task_1.py:9(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1332    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

