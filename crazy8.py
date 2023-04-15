from deck import Deck
from player import Player
import random


class Crazy:
    def __init__(self, players=4):
        self._deck = Deck()
        self.current_player_index = 0
        self.player_list = []
        for x in range(players):
            self.player_list.append(Player())

    def is_valid(self, card):
        if self._deck.discard_pile[len(self._deck.discard_pile) - 1].getSuit() == card.getSuit() or \
                self._deck.discard_pile[len(self._deck.discard_pile) - 1].getRank() == card.getRank():
            return True
        return False

    def draw_card(self, current_player):
        new_card = self._deck.draw()
        current_player.hand.append(new_card)
        if current_player.is_valid(new_card):
            self.play_card(self, current_player, len(current_player.hand)-1)

        else:
            self.next_turn()

    def play_card(self, current_player, index):
        played_card = current_player.play_card(index)
        self._deck.discard_pile.append(played_card)
        

    # this is unfinished, more of an idea of what we can do
    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.player_list)

    def set_up(self):
        random.shuffle(self._deck.cards)
        for player in self.player_list:
            player.hand = self._deck.deal(7)

    def start(self):
        self.set_up()
        win = False
        while not win:
            current_player = self.player_list[self.current_player_index]
            card_index = 0
            for card in current_player.hand:
                if self.is_valid(card):
                    self.play_card(current_player, card_index)
                    break
                elif card_index == len(current_player.hand) - 1:
                    self.draw_card(current_player)
                else:
                    card_index += 1

            if current_player.hand == 0:
                win = True
                print(current_player + ' wins!')
            self.next_turn
            
            








    
