t = input()
ls = []
s = 0
for i in t:
    if i in '1234567890':
        ls.append(int(i))
        s += int(i)
        m = max(ls)
print("Все цифры в тексте: ", ls)
print("Сумма цифр в тексте: ", s)
print("Максимальная цифра в тексте: ",m)
