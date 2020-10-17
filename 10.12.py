import random


n, m = map(int, input('Введите размер массива N*M: ').split( ))
arr = [[random.randint(-10, 10) for i in range(n)] for i in range(m)]
for i in arr:
    for j in i:
        print(j, '\t', end = " ")
    print()
q_u = 0
i_str = 0
for i in range(m):
    for j in range(n):
        q_u_max = arr[i].count(arr[i][j])
        if q_u_max > q_u:
            q_u = q_u_max
            i_str = i
print()
print('Номер строки с максимальным кол-вом одинаковых эл-тов: ', i_str)
