import random
from card_dc import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return tuple(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)
    
    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_ranks(cls):
        return cls.RANKS


if __name__ == "__main__":
    d1 = CardDeck()
    d1.shuffle()
    print(f"d1.cards: {d1.cards}")
    for i in range(5):
        print(f"d1.draw(): {d1.draw()}")
    
    print(f"d1.cards: {d1.cards}")
    r = d1.get_ranks()
    print(f"r: {r}")
    r = CardDeck.get_ranks()
    print(f"r: {r}")
    