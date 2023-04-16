import pygame
import time, math
#from crazy8 import Crazy
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
        print('Player ' + str(self.current_player_index) + ' drew a ' + str(new_card) + " | " + "They have " + str(len(current_player.hand)) + " left.")
        if self.is_valid(new_card):
            self._deck.discard_pile.append(new_card)
            print('Player ' + str(self.current_player_index) + ' played a ' + str(new_card) + " | " + "They have " + str(len(current_player.hand)) + " left.")
        else:
            current_player.hand.append(new_card)

    #CPU plays a card
    def play_card(self, current_player, index):
        played_card = current_player.play_card(index)
        if self.is_valid(played_card):
            self._deck.discard_pile.append(played_card)
            print('Player ' + str(self.current_player_index) + ' played a ' + str(played_card) + " | " + "They have " + str(len(current_player.hand)) + " left.")
        else:
            current_player.hand.append(played_card)
            self.draw_card(current_player)

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
            print('Player ' + str(self.current_player_index) + " wins!")
            return True
        return False



# Initialize Pygame
pygame.init()

# Init crazy8
game = CrazyNew()
game.setup()
print(game.player_list[0].hand)
win = False

# Set window size
screen_info = pygame.display.Info()
sw = screen_info.current_w
sh = screen_info.current_h
window_size = (int(sw - sw/4), int(sh - sh/4))

# Create window
window = pygame.display.set_mode((window_size[0], window_size[1]))
pygame.display.set_caption("crazy8")

# Fill background color
background_color = (1,50,32)
window.fill(background_color)

# Loading card images
suit_list = ['spades', 'hearts', 'clubs', 'diamonds']
numbers_list = ['2','3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
key_numbers_list = ['two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
# Load multiple images
card_image_list = dict()
for i in range(4):
        for j in range(13):
            filename = f'{numbers_list[j]}_of_{suit_list[i]}.png'  # Replace with your image file name
            image = pygame.image.load("cards/" + filename)
            card_image_list[f'{key_numbers_list[j]} of {suit_list[i]}'] = image
        
draw_pile_img = pygame.image.load('cards/back_of_card.png')
draw_pile_img = pygame.transform.scale(draw_pile_img, (106, 146))
window.blit(draw_pile_img, (int(window_size[0]/2)- 110, int(window_size[1]/2) - 152/2))

discard_pile_img = card_image_list[str(game._deck.discard_pile[len(game._deck.discard_pile)-1]).lower()]
discard_pile_img = pygame.transform.scale(discard_pile_img, (100, 140))

window.blit(draw_pile_img, (window_size[0]/2-30, 0))
window.blit(draw_pile_img, (window_size[0]/2-50, 0))
window.blit(draw_pile_img, (window_size[0]/2-70, 0))
window.blit(draw_pile_img, (window_size[0]/2-90, 0))

draw_pile_img = pygame.transform.rotate(draw_pile_img, 90)
window.blit(draw_pile_img, (0, window_size[1]/2-30))
window.blit(draw_pile_img, (0, window_size[1]/2-50))
window.blit(draw_pile_img, (0, window_size[1]/2-70))
window.blit(draw_pile_img, (0, window_size[1]/2-90))

window.blit(draw_pile_img, (window_size[0]-140, window_size[1]/2-90))
window.blit(draw_pile_img, (window_size[0]-140, window_size[1]/2-70))
window.blit(draw_pile_img, (window_size[0]-140, window_size[1]/2-50))
window.blit(draw_pile_img, (window_size[0]-140, window_size[1]/2-30))

window.blit(discard_pile_img, (window_size[0]/2, window_size[1]/2 - 146/2))

pygame.display.update()

# Set font and font size
font_size = 72
font = pygame.font.Font(None, font_size)

# Define font properties
button_font_size = 24
button_font = pygame.font.Font(None, button_font_size)

# Create function to display text on window
def display_text(text, seconds, x=None, y=None):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()

    # If x and y are given, use them as the center position
    if x is not None and y is not None:
        text_rect.center = (x, y)
    else:
        text_rect.center = (window_size[0] // 2, window_size[1] // 2)

    window.blit(text_surface, text_rect)
    pygame.display.flip()
    time.sleep(seconds)
    # Fill the background color only around the text
    background_rect = pygame.Rect(text_rect.left, text_rect.top, text_rect.width, text_rect.height)
    pygame.draw.rect(window, background_color, background_rect)

    # Update the screen to show the cleared background
    pygame.display.update()

# Create function to display button on window
def display_button(text, x, y, w, h, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Check if mouse is over button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, active_color, (x, y, w, h))
        if click[0] == 1:
            return True  # button clicked
    else:
        pygame.draw.rect(window, inactive_color, (x, y, w, h))

    # Draw button text
    text_surface = button_font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x + w // 2, y + h // 2)
    window.blit(text_surface, text_rect)

def display_persistent_text(text, x, y, fsize):
    fontP = pygame.font.Font(None, fsize)
    text_surface = fontP.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

def updateHand(handSize):
    background_rect = pygame.Rect(0, window_size[1] - 190, window_size[0], window_size[1])
    pygame.draw.rect(window, (0,0,0), background_rect)
    discard_pile_img = card_image_list[str(game._deck.discard_pile[len(game._deck.discard_pile)-1]).lower()]
    discard_pile_img = pygame.transform.scale(discard_pile_img, (100, 140))
    window.blit(discard_pile_img, (window_size[0]/2, window_size[1]/2 - 146/2))
    pygame.display.update()
    
    for i in range(handSize):
        size = (100,140)
        pos = (50 + ((25 + size[0]) * i), window_size[1] - (140+25))
        counter_width = 0
        counter_length = 0
        card = pygame.transform.scale(card_image_list[str(game.user.hand[i]).lower()], size)
        window.blit(card, pos)
        pygame.display.update()
        # attr = pygame.Rect(pos, size)
        # pygame.draw.rect(window, colorTemp, attr)
    pygame.display.flip()

def chooseCard():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(game.player_list[0].hand)):
                    colorHover = (200, 200, 200)
                    colorTemp = (255,255,255)
                    size = (100, 140)
                    pos = (50 + ((25 + size[0]) * i), window_size[1] - (140 + 25))
                    attr = pygame.Rect(pos,size)
                    # Check if mouse is hovering over the rectangle
                    if attr.collidepoint(pygame.mouse.get_pos()):
                        pygame.draw.rect(window, colorHover, attr)
                        pygame.display.update()
                        cardChosen = i
                        return cardChosen
                    else:
                        pygame.draw.rect(window, colorTemp, attr)
                        pygame.display.update()                    
        # return -1

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            return running
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
        pygame.quit()
        return running

def clearPlaySpace():
    background_rect = pygame.Rect(150, window_size[1] - 240, window_size[0], 50)
    pygame.draw.rect(window, background_color, background_rect)

# Main game loop
updateHand(len(game.player_list[0].hand))
while not win:
    # Handle events
    handleEvents()
    
    #Current Player
    current_player = game.player_list[game.current_player_index]
    
    # Check if turn
    if game.current_player_index == 0:
        # print('\nYour Hand: ')
        # x = 1
        # for card in game.user.hand:
        #     print(str(x) + ': ' + str(card))
        #     x+=1                    
        # print('\nTop card: ' + str(game._deck.discard_pile[len(game._deck.discard_pile)-1]))

        # Validate
        card_index = game.valid_deck(current_player)
        ButtonClicked = False

        clearPlaySpace()
        # updateHand(len(game.player_list[0].hand))
        if card_index >= 0: # and display_button("Play card", 150, window_size[1] - 240, 100, 50, (255, 0, 0), (200, 0, 10)): # Spawns button and If button is pressed do this
            clearPlaySpace()
            updateHand(len(game.player_list[0].hand))
            # Do play card stuff
            display_persistent_text("Choose your card", 300, window_size[1] - 225, 50)
            pygame.display.update() 
            played_index = chooseCard()
            game.play_card(game.player_list[0], played_index)
            #
            ButtonClicked = True
            clearPlaySpace()
            updateHand(len(game.player_list[0].hand))
            win = game.check_win(current_player) 
            game.next_turn()
        # if card_index >= 0 and display_button("Draw card", 250, window_size[1] - 240, 100, 50, (255, 0, 0), (200, 0, 10)): # Spawns button and If button is pressed do this
        #     #clearPlaySpace()
        #     updateHand(len(game.player_list[0].hand))
        #     # Do draw card stuff
        #     game.draw_card(game.player_list[0])
        #     #
        #     ButtonClicked = True
        #     #clearPlaySpace()
        #     updateHand(len(game.player_list[0].hand))
        #     win = game.check_win(current_player) 
        #     game.next_turn()
        if card_index < 0:
            clearPlaySpace()
            # Forced Draw here and then do you want to play
            text = "Oops! Looks like you can't play! You will now draw."
            display_persistent_text(text, window_size[0] // 2, window_size[1] - 225, 50)
            time.sleep(1)
            game.draw_card(game.player_list[0])
            #
            win = game.check_win(current_player) 
            game.next_turn()
    # If not my turn do next player turn
    else:
        clearPlaySpace()
        text = "Doing Player " + str(game.current_player_index) + "'s turn"
        display_persistent_text(text, window_size[0] // 2, window_size[1] - 225 , 50)
        time.sleep(1)
        # Do bot's turn
        #CPU turn
        card_index = game.valid_deck(current_player)
        if card_index >= 0:
            game.play_card(current_player, card_index)
        else:
            game.draw_card(current_player)
        win = game.check_win(current_player)    
        game.next_turn()
        updateHand(len(game.player_list[0].hand))  
    # Update screen
    pygame.display.flip()
    pygame.display.update() 
text = 'Player ' + str(game.current_player_index) + ' wins!'
display_persistent_text(text, window_size[0] // 2, window_size[1] // 2, 200)
pygame.display.update()
time.sleep(5)
# Quit Pygame
pygame.quit()
