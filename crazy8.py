from deck import Deck
from player import Player
import random


class CrazyNew:
    def __init__(self, players=4):
        self._deck = Deck()
        self.current_player_index = 0
        self.player_list = []
        for x in range(players-1):
            self.player_list.append(Player())
        self.user = Player()
        self.player_list.insert(0, self.user)

    #Checks if a card is valid to play
    def is_valid(self, card):
        if self._deck.discard_pile[len(self._deck.discard_pile) - 1].getSuit() == card.getSuit() or \
                self._deck.discard_pile[len(self._deck.discard_pile) - 1].getRank() == card.getRank():
            return True
        return False

    #Checks if there is a valid card in a player's deck and returns the index; returns -1 otherwise
    def valid_deck(self, player):
        for card in player.hand:
            if self.is_valid(card):
                return player.hand.index(card)
        return -1

    #Draws a card from the deck into the players hand, if they can play it, they do
    def draw_card(self, current_player):
        new_card = self._deck.draw()
        print('Player ' + str(self.current_player_index) + ' drew a ' + str(new_card))
        if self.is_valid(new_card):
            self._deck.discard_pile.append(new_card)
            print('Player ' + str(self.current_player_index) + ' played a ' + str(new_card))
        else:
            current_player.hand.append(new_card)

    #CPU plays a card
    def play_card(self, current_player, index):
        played_card = current_player.play_card(index)
        if self.is_valid(played_card):
            self._deck.discard_pile.append(played_card)
            print('Player ' + str(self.current_player_index) + ' played a ' + str(played_card))
        else:
            current_player.hand.append(played_card)
            self.draw_card(current_player)

    #User plays a card
    def user_play_card(self, user):
        play_index = int(input('Which card would you like to play?: '))
        while play_index < 1 or play_index > len(self.user.hand) or not self.is_valid(self.user.hand[play_index-1]):
            play_index = int(input('Invalid choice. Try Again: '))
        print('You played the ' + str(self.user.hand[play_index-1]))
        played_card = self.user.hand[play_index-1]
        self.user.hand.remove(played_card)
        self._deck.discard_pile.append(played_card)

    #sets the current player index to the next player
    def next_turn(self):
        if self.current_player_index == len(self.player_list) - 1:
            self.current_player_index = 0
        else:
            self.current_player_index += 1
            
    #Starts the game and deals the cards
    def setup(self):
        random.shuffle(self._deck.cards)
        for player in self.player_list:
            player.hand = self._deck.deal(7)
        first_card = self._deck.cards.pop()
        self._deck.discard_pile.append(first_card)
        print('Hands are dealt!')

    def check_win(self, current_player):
        if len(current_player.hand) < 1:
            return True
        return False

    def start(self):
        self.setup()
        win = False
        while not win:
            current_player = self.player_list[self.current_player_index]
            
            #CPU turn
            if self.current_player_index != 0:
                card_index = self.valid_deck(current_player)
                if card_index >= 0:
                    self.play_card(current_player, card_index)
                else:
                    self.draw_card(current_player)

            #Player turn
            else:
                #Printing your hand and top card
                print('\nYour Hand: ')
                x = 1
                for card in self.user.hand:
                    print(str(x) + ': ' + str(card))
                    x+=1                    
                print('\nTop card: ' + str(self._deck.discard_pile[len(self._deck.discard_pile)-1]))

                #Checking for valid card ## ISSUE TURN INTO FUNCTION OR INPUT
                card_index = self.valid_deck(current_player)
                if card_index >= 0:
                    choice = input('What would you like to do? (Type p for play or d for draw): ')
                    while choice.lower() != 'd' and choice.lower() != 'p':
                        choice = input('Invalid Choice. Try Again: ')
                else:
                    choice == 'd'
                    print("Oops! Looks like you can't play! You will now draw.")      

                 
                if choice.lower() == 'd':
                    self.draw_card(current_player)

                elif choice.lower() == 'p':
                    self.user_play_card(current_player)
                    
                print()
            
            win = self.check_win(current_player)
            self.next_turn()