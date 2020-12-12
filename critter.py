class Critter(object):
    def __init__(self, name, hubger = 0, boredom = 0):
        print("Появилась на свет новая зверюшка ")
        self.name = name
        self.hunger = hubger
        self.boredom = boredom

    def __str__(self):
        rep = 'Имя: ' + self.name + '\n' + 'Голод: ' + str(self.hunger) + '\n' + 'Скука: ' + str(self.boredom)
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def talk(self):
        print("Привет! Меня зовут ", self.name, " и сейчас я чувствую себя ", self.mood, "\n")
        self.__pass_time()

    def eat(self, food = 0):
        print("Ого! ЕДА!!!Теперь заполнено: ", food)
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
        print(food)

    def play(self, fun=4):
        print("Уииии! Хозяин со мной играет")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать, чтобы хорошо"
        else:
            m = "ужасно"
        return m


def main():
    crit_name=input("Как назовете свою зверюшку ?")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print \
            ("""
            Моя зверюшка
            0 - Выйти
            1 - Узнать о самочувствиии зверюшки
            2 - Покормить зверюшку
            3 - Поиграть со зверюшкой
            """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            food = int(input("Введите кол-во еды: "))
            crit.eat(food)
        elif choice == "3":
            crit.play()
        elif choice == "4":
            print(crit)
        else:
            print("Извините, в меню игры нет такого пункта ", choice)
main()
input("\n\nНажмите Enter, чтобы выйти")