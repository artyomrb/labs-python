import random
import sys

class Card:
    card_suits = ['\u2666', '\u2665', '\u2663', '\u2660']  # ["Трефы", "Бубны", "Черви", "Пики"]
    card_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Возвращает читаемые человеком строки """
        return '%s %s' % (Card.card_suits[self.suit], Card.card_ranks[self.rank])

    def __lt__(self, other):
        """перегрузка сравнения"""
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit
        return t1 < t2


class Deck:
    def __init__(self):
        """Инициализирует доску с 52 картами."""
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)
        self.shuffle()

    def __str__(self):
        """Возвращает строковое представление доски."""
        res = []
        for card in self.cards:
            res.append(str(card))
        return ', '.join(res)

    def __len__(self):
        """перегрузка len"""
        return len(self.cards)

    def add_card(self, card):
        """Добавляет карту на доску."""
        self.cards.append(card)

    def pop_card(self, i=-1):
        """Убирает и возвращает карту на доску.
        i: индекс карты для показа; показывается последняя карта.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """перемешивает карты на доске."""
        random.shuffle(self.cards)

    def sort(self):
        """Сортировка карт в порядке возрастания."""
        self.cards.sort()

    def wincard(self, cards):
        """выбирает самую сильную выигрышную карту"""
        winner = cards[0]
        for card in cards:
            if winner < card:
                winner = card
        return winner


class Hand(Deck):
    """Рука с колодой игральных карт."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.wincount = 0

    def getlabel(self):
        """ Имя игрока """
        return self.label

    def roundwinner(self):
        """ Увеличивает количество выигрышных очков игрока """
        self.wincount += 1

    def getwincount(self):
        """ Подсчитывает очки победителя"""
        return self.wincount

    def __str__(self):
        return "Карты " + self.label + " is " + Deck.__str__(self)


def play(argv):
    deck = Deck()
    hands = []
    for i in range(1, 5):
        player = 'Игрок %d' % i
        if len(argv) > i:
            player = argv[i]
        hands.append(Hand(player))  # добавляем игрока

    while len(deck) > 0:
        for hand in hands:
            hand.add_card(deck.pop_card())  # забрать карту с доски в руки

    print(hands[0])  # print first player card
    input("Для начала игры нажмите клавишу Enter и продолжайте каждый раунд: ")  # ожидание действия

    for i in range(1, 14):
        cards = []  # собирает карты для раунда
        fl = []  # текстовый дисплей раундов
        for hand in hands:
            card = hand.pop_card()
            cards.append(card)
            fl.append(hand.getlabel() + " : " + str(card))

        winner_card = deck.wincard(cards)  # проверяет карты победителя
        winner_hand = hands[cards.index(winner_card)]  # определяет победителя по карте
        winner_hand.roundwinner()  # счёт
        print("Раунд", i, ":-", ", ".join(fl), " \n Победитель - ", winner_hand.getlabel(), ":", winner_card)
        input()  # ожидание действия

    for hand in hands:  #счёт для 13 раундов
        print("Счёт для ", hand.getlabel(), " - ", hand.getwincount())


def main(argv=[]):
    answer = "Д"
    while answer.upper() == "Д":
        play(argv)
        answer = input("Играть снова (Д/Н)? : ")
    print("До встречи!")


if __name__ == '__main__':
    main(sys.argv)