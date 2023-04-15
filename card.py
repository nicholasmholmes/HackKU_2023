class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    def getSuit(self):
        return self._suit

    def getRank(self):
        return self._rank

    def __lt__(self, other):
        return (self._rank < other._rank)

    def __gt__(self, other):
        return (self._rank > other._rank)

    def __le__(self, other):
        return (self._rank <= other._rank)

    def __ge__(self, other):
        return (self._rank >= other._rank)

    def __eq__(self, other):
        return (self._rank == other._rank)

    def __ne__(self, other):
        return (self._rank != other._rank)

    def __str__(self):
        return f"{self._rank} of {self._suit}"
    
    def __repr__(self):
        return f"{self._rank} of {self._suit}"

