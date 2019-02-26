# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 11))
        print("%4d" % b[j], end='')
    a.append(b)
    print()


for i in range(M):
    print("  --", end='')
print()

# ищем и выводим минимальные числа в столбцах, записывая их в массив
c = []
for i in range(M):
    min_c_i = 0
    for j in range(N):
        if a[min_c_i][i] >  a[j][i]:
            min_c_i = j
    c.append(a[min_c_i][i])
    print("%4d" % a[min_c_i][i], end='')
print()

print(f"Максимальное число из минимальных в столбцах = {max(c)}")

