lst = []  
n = int(input("Введите кол-во элементов в списке: "))
if n % 2 != 0:
    print('нельзя поменять местами, т.к. невозможно поделить список')
else:
    for i in range(n): 
        lst.append(int(input()))
    print(lst)
    print(lst[n // 2:] + lst[0: n // 2])

