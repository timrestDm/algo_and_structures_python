"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import random

n = int(input("Введите количество элементов массива: "))
a = [int(random()*100) for _ in range(n)]

print(a)

min1_i = 0
min2_i = 0

for i in range(n):
    if a[min1_i] >= a[i]:
        min1_i = i
    if a[min2_i] >= a[i] and min1_i != min2_i:
        min1_i = i

print(f"Наименьшие элементы массива - {a[min1_i]}({min1_i}) и {a[min2_i]}({min2_i})")