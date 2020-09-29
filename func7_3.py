import math

def func(x):
    '''вычисляет значение функции'''
    return(math.sqrt(1-(math.sin(x)**2)))

if __name__ == "__main__":
    number = float(input('Введите x: '))
    print(math.sqrt(1 - (math.sin(number)**2)))
