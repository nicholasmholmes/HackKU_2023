from deck import Deck
import random


class CPU:
    def __init__(self):
        self.hand = []
        self.deck = Deck()

    def receive_cards(self, num_cards):
        for i in range(num_cards):
            card = self.deck.deal()
            self.hand.append(card)

    def play_card(self):
        return self.hand.pop()

    def show_hand(self):
        print("CPU hand:")
        for card in self.hand:
            print(card)

    def choose_card(self):
        # Choose a random card to play
        return random.choice(self.hand)
