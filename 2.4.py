def sr(a=1, b=2, c=3):
    return ((a+b+c)/3)
print(sr())

a1,a2,a3 = map(int, input('Введите три числа через пробел').split())
sred = sr(a1,a2,a3)
print('Среднее арифметическое равно ',sred)
