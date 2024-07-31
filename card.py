class Card:  # inherit from 'object'

    def __init__(self, rank, suit):
        self._rank = rank   # private variables (aka instance vars)
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __repr__(self):
        # return code to reproduce object
        return f"Card('{self.rank}', '{self.suit}')"

    def __str__(self):
        # return human-friendly view of object
        return f"{self.rank}-{self.suit}"

if __name__ == "__main__":
    # execute this code only if running this script directly
    c1 = Card("2", "Spades")
    print(f"{c1 = }")
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")

    c2 = Card('A', 'Diamonds')
    print(f"{c2 = }")
    print(f"{c2.rank = }")
    
    print(c1, c2)