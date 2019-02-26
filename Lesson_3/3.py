#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

n = int(input("Введите количество элементов массива: "))
a = [random.randint(1, 100) for _ in range(n)]

print(a)

# способ 1
# будем хранить max и min числа и их индексы в словаре
help = {"max": 0, "max_i": 0, "min": a[0], "min_i": 0}

for i in range(n):
    if a[i] > help["max"]:
        help["max"] = a[i]
        help["max_i"] = i
    if help["min"] >= a[i]:
        help["min"] = a[i]
        help["min_i"] = i

#print(help)

# меняем местами
a[help["max_i"]], a[help["min_i"]] = a[help["min_i"]], a[help["max_i"]]

print(a)

# способ 2 храним индексы в переменных

max_i = 0
min_i = 0

for i in range(n):
    if a[i] > a[max_i]:
        max_i = i
    if a[min_i] >= a[i]:
        min_i = i

a[max_i], a[min_i] = a[min_i], a[max_i]

print(a)


# способ 3
def get_index_max_no(a):
    for i in range(len(a)):
        if a[i] == max(a):
            return i

def get_index_min_no(a):
    for i in range(len(a)):
        if a[i] == min(a):
            return i

m = get_index_max_no(a)
n = get_index_min_no(a)
a[m], a[n] = a[n], a[m]


print(a)