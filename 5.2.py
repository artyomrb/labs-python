def comp(f,s):
    '''выводит наибольшее из двух чисел'''
    if f>s:
        print("Наибольшее число: {0}".format(f))
    else:
        print("Наибольшее число: {0}".format(s))

        
f = int(input("Введите первое число: "))
s = int(input("Введите второе число: "))
comp(f,s)
    
