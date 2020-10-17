L = [-8, 8, 6.0, 5, 'строка', -3.1]
print(L)
total = 0
for i in range (len(L)):
    if type(L[i]) == float or type(L[i]) == int:
        total = L[i] + total
print("сумма чисел в строке: {0}".format(total))
        
