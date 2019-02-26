"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

n = int(input("Введите количество элементов массива: "))
a = [random.randint(0, 100) for _ in range(n)]

print(a)

max_i = 0
min_i = 0

for i in range(n):
    if a[i] > a[max_i]:
        max_i = i
    if a[min_i] >= a[i]:
        min_i = i

# max_i = a.index(max(a))
# min_i = a.index(min(a))

print(max_i)
print(min_i)

sum = 0
for i in range(min(max_i,min_i) + 1, max(max_i,min_i)):
    sum += a[i]

print(sum)