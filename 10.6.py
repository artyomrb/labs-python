s = 0
while True:
    n = input("Введите число или слово стоп для выхода: ")
    if n == "стоп":
        print("Конец программы!")
        break
    else:
        s = s + int(n)
        print(s)
