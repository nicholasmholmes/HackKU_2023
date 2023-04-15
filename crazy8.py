from deck import Deck
from player import Player
import random


class Crazy:
    def __init__(self, players=4):
        self._deck = Deck()
        self.current_player_index = 0
        self.player_list = []
        for x in range(players-1):
            self.player_list.append(Player())
        self.user = Player()
        self.player_list.insert(0, self.user)

    def is_valid(self, card):
        if self._deck.discard_pile[len(self._deck.discard_pile) - 1].getSuit() == card.getSuit() or \
                self._deck.discard_pile[len(self._deck.discard_pile) - 1].getRank() == card.getRank():
            return True
        return False

    def draw_card(self, current_player):
        new_card = self._deck.draw()
        current_player.hand.append(new_card)
        if self.is_valid(new_card):
            self.play_card(current_player, len(current_player.hand)-1)
        else:
            self.next_turn()

    def play_card(self, current_player, index):
        played_card = current_player.play_card(index)
        if self.is_valid(played_card):
            self._deck.discard_pile.append(played_card)
            self.next_turn()
        else:
            self.current_player.hand.append(played_card)
            self.draw_card(current_player)

    def next_turn(self):
        if self.current_player_index == len(self.player_list) - 1:
            self.current_player_index = 0
        else:
            self.current_player_index += 1

    def setup(self):
        random.shuffle(self._deck.cards)
        for player in self.player_list:
            print(str(player) + ' is dealt their cards!')
            player.hand = self._deck.deal(7)
        first_card = self._deck.cards.pop()
        self._deck.discard_pile.append(first_card)

    def start(self):
        self.setup()
        win = False
        while not win:
            current_player = self.player_list[self.current_player_index]
            card_index = 0
            if self.current_player_index != 0:
                for card in current_player.hand:
                    if self.is_valid(card):
                        self.play_card(current_player, card_index)
                        break
                    elif card_index == len(current_player.hand) - 1:
                        self.draw_card(current_player)
                    else:
                        card_index += 1
            else:
                print('Your Hand: ')
                x = 1
                for card in self.user.hand:
                    print(str(x) + ': ' + str(card))
                    x+=1
                    
                print('\nTop card: ' + str(self._deck.discard_pile[len(self._deck.discard_pile)-1]))

                card_index = 0
                for card in self.user.hand:
                    if self.is_valid(card):
                        break
                    else:
                        card_index += 1
                
                if card_index != len(self.user.hand) - 1:        
                    choice = input('What would you like to do? (Type p for play or d for draw): ')
                    while choice.lower() != 'd' and choice.lower() != 'p':
                        choice = input('Invalid Choice. Try Again: ')
                else:
                    print("Oops! Looks like you can't play! You will now draw.")
                    choice = 'd'     
                    
                if choice.lower() == 'd':
                    new_card = self._deck.draw()
                    print('You drew a ' + str(new_card))
                    if self.is_valid(new_card):
                        play_drawn_card = input('Would you like to play this card? y or n: ')
                        if play_drawn_card.lower() == 'y':
                            self._deck.discard_pile.append(new_card)
                        else:                           
                            self.user.hand.append(new_card)
                    else:
                        self.user.hand.append(new_card)

                elif choice.lower() == 'p':
                    play_index = int(input('Which card would you like to play?: '))
                    while play_index < 1 or play_index > len(self.user.hand) or not self.is_valid(self.user.hand[play_index-1]):
                        play_index = int(input('Invalid choice. Try Again: '))
                    print('You played the ' + str(self.user.hand[play_index-1]))
                    played_card = self.user.hand[play_index-1]
                    self.user.hand.remove(played_card)
                    self._deck.discard_pile.append(played_card)
            
            if len(current_player.hand) < 1:
                win = True
                print(f'Player {self.current_player_index} wins!')
            else:
                self.next_turn()






