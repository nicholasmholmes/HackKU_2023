from card import Card
import random


class Deck:
    def __init__(self):
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def __str__(self):
        return f"Deck of {len(self.cards)} cards"

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"
