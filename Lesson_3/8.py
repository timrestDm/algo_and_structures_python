"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""


M = 5
N = 4
a = []
# формируем матрицу
for i in range(N):
    b = input(f"Введите через пробел 4 элемента {i + 1} строки: ")
    b = b.split()
    b = [int(i) for i in b]
    sum = 0
    for j in range(len(b)):
        sum += b[j]
    b.append(sum)
    a.append(b)


# выводим сформированную матрицу
for i in range(N):
    for j in range(M):
        print("%4d" % a[i][j], end='')
    print()