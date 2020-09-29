import math
x, y = map(int, input('Введите x и y через пробел: ').split( ))
z = (x + ((2 + y)/(x**2))) / (y + (1/(math.sqrt(x**2 + 10))))
q = 2.8 * (math.sin(x)) + abs(y)
print('z = ', z, '\n' 'q = ', q)
