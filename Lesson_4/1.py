"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""


"""
Урок2 Задание 4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

import timeit
import cProfile

# Изначальная реализация через рекурсию
# n = int(input('Введите количество элементов: '))

n = 10

def fsum(sum, b, n):
    if n == 0:
        return sum
    else:
        sum += b;
        return fsum(sum, -b/2, n-1)

# print(fsum(0, 1, n))

# print(timeit.timeit("fsum(0, 1, n)", setup="from __main__ import fsum, n"))
# результат выполнения timeit = 1.6539793999999999

# получаем просто числа
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return - f(n-1)/2

# print(timeit.timeit("f(n)", setup="from __main__ import f, n"))
# результат выполнения timeit = 1.3126710999999998

# print('--------')
# cProfile.run('fsum(0, 1, n)')
# результат выполнения cProfile:
# 14 function calls (4 primitive calls) in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 11/1    0.000    0.000    0.000    0.000 1.py:21(fsum)
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g

@memorize
def f_memorized(n):
    if n < 2:
        return 1
    else:
        return - f_memorized(n-1)/2

# print(fq(n))
# print(timeit.timeit("f_memorized(n)", setup="from __main__ import f_memorized, n"))
# результат выполнения timeit = 0.18141830000000025 (примерно в 10 раз меньше, чем без memorized)


# вывод числа не рекурсивным методом
def f_new(n):
    b = [0]*n
    b[0] = 1
    for i in range(1, n):
        b[i] = -(b[i-1])/2
    return b[n-1]

# print(timeit.timeit("f_new(n)", setup="from __main__ import f_new, n"))
# результат выполнения timeit = 1.3154049 (примерно также, как и рекурсивным методом)

@memorize
def f_new_memo(n):
    b = [0]*n
    b[0] = 1
    for i in range(1, n):
        b[i] = -(b[i-1])/2
    return b[n-1]

print(timeit.timeit("f_new_memo(n)", setup="from __main__ import f_new_memo, n"))
# если применить memorize результат выполнения timeit = 0.173023 (что сопоставимо с меморайзом рекурсии)

# вывод - так как функция линейная от n, то результаты рекурсивного и циклического методов примерно одинаковы
# но использование меморайза увеличивает скорость примерно в 10 раз

