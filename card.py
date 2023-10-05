class Card:
    VALID_RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split() + [None]
    VALID_SUITS = 'Clubs Diamonds Hearts Spades'.split() + [None]

    # def __init__(self, *args):
    #     if len(args) == 2:
    #         pass
    #     if len(args) == 3:
    #         pass

    def __init__(self, rank=None, suit=None):
        self.rank = rank   # sets self._rank *implicitly
        self.suit = suit

    @property
    def suit(self):   # getter property
        return self._suit

    @suit.setter
    def suit(self, value):
        if value in self.VALID_SUITS:
            self._suit = value
        else:
            raise ValueError("Invalid suit")

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if value in self.VALID_RANKS:
            self._rank = value
        else:
            raise ValueError("Invalid rank")

    # human-readable representation
    def __str__(self):    # responds to str()  similar to OBJ.to_string() in Java/C#
        return f"{self.rank}-{self.suit}"

    # interpreter-friendly representation
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c = Card('5', 'Diamonds')
    # print(f"c._rank: {c._rank}")   # NAUGHTY!!
    print(f"c.rank: {c.rank}")
    print(f"c.suit: {c.suit}")
    c.rank = '8'
    print(f"c.rank: {c.rank}")
    
    c2 = Card()
    c3 = Card('8')

    print(f"c: {c}")
    print(c)   #  print(str(c))
    print(repr(c))