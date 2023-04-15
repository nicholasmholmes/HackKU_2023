from deck import Deck
from player import Player
import random


class Crazy:
    def __init__(self, players):
        self._deck = Deck()
        self._current_player_index = 0
        self.player_list = []
        for x in range(players):
            self.player_list.append(Player())


    def start(self):
        random.shuffle(self._deck.cards)
        for player in self.player_list:
            player.hand = self._deck.deal(7)

        win = False
        while not win:


        print(f'Player 1 hand: {self.player.hand}')


        self.player_draw()

    def valid_move(self, card):
        pass

    def player_draw(self, current_player):
        new_card = self._deck.draw()
        current_player.hand.append(new_card)
        if current_player.valid_move(new_card) is True:
            # need to make new_card get played

        else:
            pass

    # this is unfinished, more of an idea of what we can do
    def next_turn(self):
        current_player = self.players[self.current_player_index]
        # do something with the current player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
