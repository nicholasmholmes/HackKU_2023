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
        self._player.hand = self._deck.deal(7)
        self._cpu1.hand = self._deck.deal(7)
        self._cpu2.hand = self._deck.deal(7)
        self._cpu3.hand = self._deck.deal(7)

        print(f'Player 1 hand: {self._player.hand}')
        print(f'CPU 1 hand: {self._cpu1.hand}')
        print(f'CPU 2 hand: {self._cpu2.hand}')
        print(f'CPU 3 hand: {self._cpu3.hand}')
