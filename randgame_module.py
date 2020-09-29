import random
def guess():
    """Запускает игру 'Угадай число'"""
    rand_m = random.randint(1, 5)
    n = int(input('Введите целое число от 1 до 5: '))
    if n != rand_m:
        print('Повторите еще раз')
    else:
        print('Победа')

if __name__ == "__main__":
    startgame()
