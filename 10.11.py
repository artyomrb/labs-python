import random


n = int(input('Введите размер массива NxN: '))
arr = [[random.randint(-10, 10) for i in range(n)] for i in range(n)]
for i in arr:
    for j in i:
        print(j, '\t', end = " ")
    print()
