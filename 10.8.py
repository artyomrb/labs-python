str = (input("Введите строку: "))
def longword(text):
    stroka=text.split(' ')
    list1 = list(map(len,stroka))
    return list1.index(max(list1))+1

s = longword(str)
print(s)
