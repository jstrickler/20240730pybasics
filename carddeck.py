import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._build_deck()

    def _build_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()  # remove card and return it

    def deal(self, number_of_cards):
        cards = []
        for i in range(number_of_cards):
            cards.append(self.draw())
        return cards

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    d1.shuffle()
    print(f"{d1.cards = }\n")
    c = d1.draw()
    print(f"{c = }")
    print(c)
    hand = d1.deal(5)
    print(f"{hand = }\n")
    