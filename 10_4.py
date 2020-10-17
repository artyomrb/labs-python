import random
N = random.randint(0,10)
while True:
    text = input("Введите число или выход для выхода: ")
    if text == "выход":
        print("Выход из программы! До встречи!")
        break
    elif int(text) > n:
        print(число больше загаданного)
    elif int(text) < n:
        print(число меньше загаданного)
    elif int(text) == n:
        print("Победа!")
        break
    
