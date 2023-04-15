from deck import Deck
import random


class CPU:
    def __init__(self):
        self.hand = []

    def play_card(self, index):
        value = self.hand[index]
        self.hand.remove(index)
        return value
