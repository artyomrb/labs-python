import math
def texp(x):
    """Вычисляет exp(x) путем разложения в ряд Тейлора"""
    eps = 0.001
    n = 0
    An = x
    exptotal = 0
    while math.fabs(An) > eps :
            An = (math.pow(x, n))/(math.factorial(n))
            exptotal += An
            n += 1
    return exptotal, n

def tsin(x):
    """Вычисляет sin(x) путем разложения в ряд Тейлора"""
    eps = 0.001
    n = 0
    An = x
    sintotal = 0
    while math.fabs(An) > eps :
        if n == 0:
            An = x/math.factorial(1)
            sintotal
            n += 1
        else:
            An = (math.pow(-1, n+1) * math.pow(x, 2*n-1))/math.factorial(2*n-1)
            sintotal += An
            n += 1
    return sintotal, n

def tcos(x):
    """Вычисляет cos(x) путем разложения в ряд Тейлора"""
    eps = 0.001
    n = 0
    An = x
    costotal = 0
    while math.fabs(An) > eps :
            An = (math.pow(-1, n)*math.pow(x, 2*n))/math.factorial(2*n)
            costotal += An
            n += 1
    return costotal, n

print('Сумма и количество итераций для exp(x): ', texp(int(input('Введите x для exp(x): '))))
print('Сумма и количество итераций для sin(x): ', tsin(int(input('Введите x для sin(x): '))))
print('Сумма и количествво итераций для cos(x): ', tcos(int(input('Введите x для cos(x): '))))
