from deck import Deck
from cpu import CPU
import random

class Crazy:
    def __init__(self):
        self._deck = Deck()
        self._cpu1 = CPU()
        self._cpu2 = CPU()
        self._cpu3 = CPU()
        self._player = CPU()

    def start(self):
        random.shuffle(self._deck.cards)
        for i in range(7):
            self._player.hand.append(self._deck.deal)
        for i in range(7):
            self._cpu1.hand.append(self._deck.deal)
        for i in range(7):
            self._cpu2.hand.append(self._deck.deal)
        for i in range(7):
            self._cpu3.hand.append(self._deck.deal)
        
        for i in range(7):
            print(self._cpu1.hand[i])
