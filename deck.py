from card import Card
import random


class Deck:
    def __init__(self):
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.discard_pile = []

    def deal(self, num_cards=1):
        if len(self.cards) < num_cards:
            self.reshuffle()
        dealt_cards = []
        for i in range(num_cards):
            card = self.cards.pop()
            dealt_cards.append(card)
        return dealt_cards

    def reshuffle(self):
        while len(self.discard_pile) != 0:
            temp = self.discard_pile.pop()
            self.cards.append(temp)
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) < 1:
            self.reshuffle()
        value = self.cards.pop()
        return value

    def __str__(self):
        return f"Deck of {len(self.cards)} cards"

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"
