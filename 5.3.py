def bin(m):
    '''проверяет целое число на четность'''
    if m%2 == 0:
        print('Число чётное')
    else:
        print('Число нечётное')

m = int(input("Введите число: "))
bin(m)
