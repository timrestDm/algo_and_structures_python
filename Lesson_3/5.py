#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
import random

n = int(input("Введите количество элементов массива: "))
a = [random.randint(-100, 100) for _ in range(n)]

print(a)


def get_index_max_num(a):
    max = min(a)
    max_i = 0
    for i in range(len(a)):
        if a[i] < 0 and a[i] > max:
            max = a[i]
            max_i = i
    return max_i


print(f"Максимальное отрицательное число = {a[get_index_max_num(a)]} с индексом {get_index_max_num(a)}")