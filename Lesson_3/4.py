# 4.	Определить, какое число в массиве встречается чаще всего.

import random

n = int(input("Введите количество элементов массива: "))
a = [random.randint(1, 9) for _ in range(n)]

print(a)

# каждый элемент массива сравниваем с другими элементами массива, если есть такой же - прибавляем в другом массиве 1 элементу тогоже индекса
b = [0]*n
for i in range(n):
    for j in range(n):
        if a[i] == a[j] and i != j:
            b[i] += 1

print(b)

# получаем индекс максимального элемента во втором массиве (он равен индексу элемента из начального массива, который встречается чаще)
def get_index_max_num(a):
    max = 0
    max_i = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
            max_i = i
    return max_i

print(a[get_index_max_num(b)])

