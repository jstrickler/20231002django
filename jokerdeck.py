from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    # Card.add_rank('JOKER')  # class method

    def _make_deck(self):
        super()._make_deck()
        for i in range(2):
            joker = Card('JOKER', None)
            self._cards.append(joker)
