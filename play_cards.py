from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck()
j1 = JokerDeck()

j1.shuffle()
for i in range(5):
    print(f"j1.draw(): {j1.draw()}")

print(f"j1.cards: {j1.cards}")
