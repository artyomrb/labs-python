import random


class darts:
    """Класс "Дартс" для кол-ва секторов, черного сектора и значений секторов"""
    n = 0
    k = 0
    playfield = []

    def __init__(self, n, k, field):
        """Конструктор класса Дартс"""
        self.n = n
        self.k = k
        self.playfield = field

    def getdarts(self):
        """Получение информации об объекте класса Дартс"""
        return self.n, self.k, self.playfield

    def setdarts(self, newn, newk, newfield):
        """Присвоение новых значений полям объекта класса Дартс"""
        self.n = newn
        self.k = newk
        self.playfield = newfield

    def FindMaxScoreDark(self):
        """Метод поиска максимально возможного результата игры при данных значениях с черным сектором"""
        max_sum = 0
        if self.k >= 0 and self.k <= self.n - 1:
            snd_half = self.playfield[:self.k]
            fst_half = self.playfield[self.k + 1:]
            self.playfield = fst_half + snd_half
            for i in range(0, len(self.playfield), 1):
                for j in range(0, -(len(self.playfield)), -1):
                    if j == 0:
                        iter_sum = sum(self.playfield[i:])
                    else:
                        iter_sum = sum(self.playfield[i:j])
                    if max_sum < iter_sum:
                        max_sum = iter_sum
        if max_sum != 0:
            return (max_sum)
        else:
            return ('Черный сектор не установлен')

    def FindMaxScore(self):
        """Метод поиска максимально возможного результата игры при данных значениях без черным сектором"""
        max_sum = 0
        for k in range(0, len(self.playfield), 1):
            for i in range(0, len(self.playfield), 1):
                for j in range(0, -(len(self.playfield)), -1):
                    if j == 0:
                        iter_sum = sum(self.playfield[i:])
                    else:
                        iter_sum = sum(self.playfield[i:j])
                    if max_sum < iter_sum:
                        max_sum = iter_sum
            self.playfield = self.playfield[1:] + self.playfield[:1]
        return (max_sum)

    def BeHeading(self):
        """Стать ведущим и задать значения игровому полю"""
        print('Теперь вы ведущий!')
        self.n = (int(input('Введите число секторов: ')))
        self.k = (int(input('Введите число черного сектора или -1 при его отсутствии: ')))
        field = (str(input('Ввести поле самому(Иначе компьютер создаст поле случайных чисел)[Y/N]?')))
        if field == 'Y':
            self.playfield = list(map(int, input('Введите список баллов секторов через пробел: ').split()[:self.n]))
        elif field == 'N':
            self.playfield = [random.randint(-30, 30) for i in range(self.n)]
        else:
            print('Введено неверное значение!')


darkdarts = darts(8, 2, [2, 3, 4, 5, -30, 6, -1, 2])  # Проверка значений, данных в задании
justdarts = darts(6, -1, [1, -3, 2, -2, 3, 4])
print('Тест №1: ', darkdarts.FindMaxScoreDark())
print('Тест №2: ', justdarts.FindMaxScore())

somedarts = darts(0, 0, [])  # Интерактивный режим
somedarts.BeHeading()
print('Баллы на игровом поле: ', somedarts.playfield)
if somedarts.k >= 0 and somedarts.k <= somedarts.n - 1:
    print('Максимально возможный результат: ', somedarts.FindMaxScoreDark())
else:
    print('Максимально возможный результат: ', somedarts.FindMaxScore())
