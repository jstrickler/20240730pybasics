from carddeck import CardDeck

deck = CardDeck()
deck.shuffle()

player1 = deck.deal(5)
print(player1)