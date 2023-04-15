class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def getSuit(self):
        return self._suit

    def getValue(self):
        return self._value

    def __lt__(self, other):
        return (self._value < other._value)

    def __gt__(self, other):
        return (self._value > other._value)

    def __le__(self, other):
        return (self._value <= other._value)

    def __ge__(self, other):
        return (self._value >= other._value)

    def __eq__(self, other):
        return (self._value == other._value)

    def __ne__(self, other):
        return (self._value != other._value)

    def __str__(self):
        return f'Value: {self._value}\tSuit: {self._suit}'
    
    

