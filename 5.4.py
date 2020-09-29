def f(x):
    '''вычисляет значение функции'''
    if x >= -2.4 and x <= 5.7:
        f = round((x**2), 2)
    else:
        f = 4
    print("f(x) = {0}".format(f))
x = float(input("Введите x(вещественное): "))
f(x)
