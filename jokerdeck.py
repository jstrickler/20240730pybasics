from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _build_deck(self):
        super()._build_deck()  # call method in parent class
        for num in range(1, 3):
            card = Card(f"** JOKER{num} **", f"** JOKER{num} **")
            self._cards.append(card)

if __name__ == "__main__":
    j1 = JokerDeck()
    j1.shuffle()
    print(f"{j1.cards = }\n")
    print(f"{j1.draw() = }\n")
