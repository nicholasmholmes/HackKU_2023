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
        print('Player ' + str(self.current_player_index) + ' drew a ' + str(new_card))
        current_player.hand.append(new_card)
        if self.is_valid(new_card):
            self._deck.discard_pile.append(new_card)
            print('Player ' + str(self.current_player_index) + ' played a ' + str(new_card))

    def play_card(self, current_player, index):
        played_card = current_player.play_card(index)
        if self.is_valid(played_card):
            self._deck.discard_pile.append(played_card)
            print('Player ' + str(self.current_player_index) + ' played a ' + str(played_card))
        else:
            current_player.hand.append(played_card)
            self.draw_card(current_player)

    def next_turn(self):
        if self.current_player_index == len(self.player_list) - 1:
            self.current_player_index = 0
        else:
            self.current_player_index += 1

    def setup(self):
        random.shuffle(self._deck.cards)
        for player in self.player_list:
            player.hand = self._deck.deal(7)
        first_card = self._deck.cards.pop()
        self._deck.discard_pile.append(first_card)
        print('Hands are dealt!')

    def user_turn(self, choice, cardChosen, play_index):
        print('\nYour Hand: ')
        x = 1
        for card in self.user.hand:
            print(str(x) + ': ' + str(card))
            x+=1
        print('\nTop card: ' + str(self._deck.discard_pile[-1]))
        #card_index = self.choose_card_index(self) # Replace with input from game
        card_index = -1
        
        if choice.lower() == 'p':
            #card_index = self.choose_play_index(self)
            card_index = play_index #something
            

        elif choice.lower() == 'd':
            card_index = -1


        if card_index != -1:
            self.play_user_card(card_index)
            return False
        else:
            self.draw_user_card(self)
            return self.check_user_win(self)

    def choose_card_index(self):
        card_index = -1
        while card_index < 0 or card_index >= len(self.user.hand):
            choice = input('What would you like to do? (Type p for play or d for draw): ')
            if choice.lower() == 'p':
                card_index = self.choose_play_index(self)
            elif choice.lower() == 'd':
                return -1
            else:
                print('Invalid choice. Try Again.')
        return card_index

    def choose_play_index(self):
        play_index = -1
        while play_index < 1 or play_index > len(self.user.hand) or not self.is_valid(self.user.hand[play_index-1]):
            play_index = int(input('Which card would you like to play?: '))
            if play_index < 1 or play_index > len(self.user.hand):
                print('Invalid choice. Try Again.')
            elif not self.is_valid(self.user.hand[play_index-1]):
                print('You cannot play that card. Try Again.')
        return play_index - 1

    def play_user_card(self, card_index):
        played_card = self.user.play_card(card_index)
        print('You played the ' + str(played_card))
        self._deck.discard_pile.append(played_card)

    def draw_user_card(self):
        new_card = self._deck.draw()
        print('You drew a ' + str(new_card))
        self.user.hand.append(new_card)
        if self.is_valid(new_card):
            self.play_user_card(len(self.user.hand)-1)

    def check_user_win(self):
        if len(self.user.hand) == 0:
            print(f'Player {self.current_player_index} wins!')
            return True
        return False

    def computer_turn(self, current_player):
        card_index = self.choose_computer_card(current_player)
        if card_index != -1:
            self.play_computer_card(current_player, card_index)
            return False
        else:
            self.draw_card(current_player)
            return self.check_computer_win(current_player)

    def choose_computer_card(self, current_player):
        card_index = 0
        for card in current_player.hand:
            if self.is_valid(card):
                return card_index
            else:
                card_index += 1
        return -1

    def play_computer_card(self, current_player, card_index):
        played_card = current_player.play_card(card_index)
        print(f'Player {self.current_player_index} played a {played_card}')
        self._deck.discard_pile.append(played_card)

    def check_computer_win(self, current_player):
        if len(current_player.hand) == 0:
            print(f'Player {self.current_player_index} wins!')
            return True
        return False


    def start(self):
        self.setup()
        win = False
        while not win:
            current_player = self.player_list[self.current_player_index]
            if self.current_player_index == 0:
                win = self.user_turn()
            else:
                print('\nYour Hand: ')
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
                
                if card_index != len(self.user.hand):        
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
                print()
            
            if len(current_player.hand) < 1:
                win = True
                print(f'Player {self.current_player_index} wins!')
            else:
                self.next_turn()




