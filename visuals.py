import pygame
import time, math
from crazy8 import Crazy

# Initialize Pygame
pygame.init()

# Init crazy8
game = Crazy()
game.setup()
print(game.player_list[0].hand)
win = False

# Loading card images
suit_list = ['spades', 'hearts', 'clubs', 'diamonds']
numbers_list = ['2','3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
key_numbers_list = ['two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
# Load multiple images
card_image_list = dict()
for i in range(4):
        for j in range(13):
            filename = f'{numbers_list[j]}_of_{suit_list[i]}.png'  # Replace with your image file name
            image = pygame.image.load(filename)
            card_image_list[f'{key_numbers_list[j]} of {suit_list[i]}'] = image
        
draw_pile_img = pygame.image.load('back_of_card.png')
draw_pile_img = pygame.transform.scale(draw_pile_img, (106, 146))
window.blit(draw_pile_img, (sw/2-106, sh/2-73))

discard_pile_img = image_list[str(game._deck.discard_pile[len(game._deck.discard_pile)-1]).lower()]
discard_pile_img = pygame.transform.scale(discard_pile_img, (100, 140))

window.blit(draw_pile_img, (sw/2-30, 0))
window.blit(draw_pile_img, (sw/2-50, 0))
window.blit(draw_pile_img, (sw/2-70, 0))
window.blit(draw_pile_img, (sw/2-90, 0))

draw_pile_img = pygame.transform.rotate(draw_pile_img, 90)
window.blit(draw_pile_img, (0, sh/2-30))
window.blit(draw_pile_img, (0, sh/2-50))
window.blit(draw_pile_img, (0, sh/2-70))
window.blit(draw_pile_img, (0, sh/2-90))

window.blit(draw_pile_img, (sw-140, sh/2-90))
window.blit(draw_pile_img, (sw-140, sh/2-70))
window.blit(draw_pile_img, (sw-140, sh/2-50))
window.blit(draw_pile_img, (sw-140, sh/2-30))

window.blit(discard_pile_img, (sw/2, sh/2-70))

pygame.display.update()

# Example of how to print cards
'''
counter_width = 0
counter_length = 0
for card in game.player_list[0].hand:
    card = pygame.transform.scale(card_image_list[str(card).lower()], (100, 140))
    window.blit(card, (counter_width, counter_length))
    pygame.display.update()
    counter_width += 100
    if counter_width == 900:
        counter_width = 0
        counter_length += 140
print(game.player_list[0].hand)
'''


# Set window size
screen_info = pygame.display.Info()
sw = screen_info.current_w
sh = screen_info.current_h
window_size = (int(sw - sw/4), int(sh - sh/4))

# Create window
window = pygame.display.set_mode((window_size[0], window_size[1]))
pygame.display.set_caption("crazy8")

# Fill background color
background_color= (0,0,0)
window.fill(background_color)

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
    text_rect.bottomleft = (x, y)
    window.blit(text_surface, text_rect)

def updateHand(handSize):
    colorTemp = (255,255,255)
    
    for i in range(handSize):
        size = (100,140)
        pos = (300 + ((25 + size[0]) * i), window_size[1] - (140+25))
        attr = pygame.Rect(pos, size)
        pygame.draw.rect(window, colorTemp, attr)
    pygame.display.flip()

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
    background_rect = pygame.Rect(150, window_size[1] - 240, 500, 50)
    pygame.draw.rect(window, background_color, background_rect)

# Main game loop
running = True
move = 0
playerTurn = 0
while running or not win:
    # Handle events
    handleEvents()

    # Current Player
    current_player = game.player_list[game.current_player_index]

    # Display welcoming text and button
    if move == 0:
        display_text("Hello, Player!", 3)
        display_persistent_text("Hand:", 140, window_size[1] - 75, 72)
        updateHand(7)
        move += 1

    if playerTurn == 0:
        myturn = True
    else:
        myturn = False
    
    # Check if turn
    if myturn:
        clearPlaySpace()
        if playerTurn == 1 and display_button("Play card", 150, window_size[1] - 240, 100, 50, (255, 0, 0), (200, 0, 10)): # Spawns button and If button is pressed do this
            display_text("Card played!", 1.5)
            clearPlaySpace()
            # Do play card stuff
            # input - p
            choice = 'p'

            display_persistent_text("Choose your card", 150, window_size[1] - 195, 50)
            # Wait until click to get cardChosen
            play_index = -1

            while play_index < 1 or play_index > len(game.user.hand) or not game.is_valid(self.user.hand[play_index-1]):
                #play_index = int(input('Which card would you like to play?: '))
                play_index = cardChosen
                if play_index < 1 or play_index > len(game.user.hand):
                    print('Invalid choice. Try Again.')
                    # Rechoose cardChosen
                elif not game.is_valid(game.user.hand[play_index-1]):
                    print('You cannot play that card. Try Again.')
                    # Rechoose cardChosen

            # clearPlaySpace()
            win = game.user_turn(game, choice, cardChosen, play_index)
            updateHand(7)
            playerTurn += 1
            if playerTurn == 4:
                playerTurn = 0
        
        if playerTurn == 1 and display_button("Draw card", 250, window_size[1] - 240, 100, 50, (255, 0, 0), (200, 0, 10)): # Spawns button and If button is pressed do this
            display_text("Card drawn!", 1.5)
            clearPlaySpace()
            # Do draw card stuff
            # input - d
            choice = 'd'
            updateHand(7)
            playerTurn += 1
            if playerTurn == 5:
                playerTurn = 0
        
    else:
        clearPlaySpace()
        text = "Doing Player " + str(playerTurn) + "'s turn"
        display_persistent_text(text, 150, window_size[1] - 195, 50)
    
    # If not my turn do next player turn
    if not myturn:
        time.sleep(.5)
        # Do bot's turn
        playerTurn += 1
        if playerTurn == 5:
            playerTurn = 0

    # Update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
