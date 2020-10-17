n = int(input("Введите число: "))
s = 0
while n > 0:
    if(n%10) % 2 != 0:
        s = s + (n%10)**2
    n = n//10
print(s)
