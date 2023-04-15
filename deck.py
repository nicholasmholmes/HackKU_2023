from card import Card
import random


class Deck:
    def __init__(self):
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        self.discards = []

    def add_to_deck(self, car):
        self.cards.append(car)
    
    def shuffle(self):
        while len(self.discards) != 0:
            self.add_to_deck(self.discards.pop())
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def __str__(self):
        return f"Deck of {len(self.cards)} cards"
