import random


class Farm(object):

    def __init__(self, name):  # Метод конструктор
        self.name = name
        self.hunger = random.randint(0, 16)
        self.boredom = random.randint(0, 16)

    def __str__(self):  # Метод вывода на экран
        rep = 'Имя: ' + self.name + '\n' + 'Голод: ' + str(self.hunger) + '\n' + 'Скука: ' + str(self.boredom)
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "Прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "Неплохо"
        elif 11 <= unhappiness <= 15:
            m = "Не сказать, чтобы хорошо"
        else:
            m = "Ужасно"
        return m

    def talk(self):
        print("Привет! Меня зовут ", self.name, "и сейчас я чувствую себя ", self.mood, "\n")
        self.__pass_time()

    @staticmethod
    def number(number=None, c=0, m=0):
        while c == 0:
            number = input('How many? Write from 0 to infinity ')
            try:
                m = int(number)
                c = 1
            except:
                print('Try again')

        if int(number) < 0:
            number = 0
        else:
            number = m
        return number

    def eat(self, food):
        print("Ого! ЕДА!!!Теперь заполнено: ", food)
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
        print(food)

    def play(self, fun):
        print("Уииии! Хозяин со мной играет")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    print('Welcome to the farm! Теперь у вас есть корова, поросёнок и козлик. Давайте дадим  им имена.')
    crit_name = input("Как вы хотите назвать корову?: ")
    cow = Farm(crit_name)
    crit_name = input("Как вы хотите назвать поросёнка?: ")
    pig = Farm(crit_name)
    crit_name = input("Как вы хотите назвать козлика?: ")
    goat = Farm(crit_name)

    choice = None
    numb = None
    while choice != "0":
        print \
            ("""
        Моя зверюшка

        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)

        choice = input("Ваш выбор: ")
        print()

        # exit
        if choice == "0":
            print("До свидания.")


        elif choice == "1":
            cow.talk()
            print('Муууу.\n')
            pig.talk()
            print('Хрю-хрю.\n')
            goat.talk()
            print('Беееее.\n')


        elif choice == "2":
            numb = Farm.number()
            cow.eat(numb)
            pig.eat(numb)
            goat.eat(numb)


        elif choice == "3":
            numb = Farm.number()
            cow.play(numb)
            pig.play(numb)
            goat.play(numb)


        elif choice == "4":
            print(cow)
            print(pig)
            print(goat)

        else:
            print("Извините, в меню игры нет такого пункта.", choice)


main()
("\n\nНажмите клавишу enter для выхода.")