# importing required library
import pygame
from crazy8 import Crazy

pygame.init()
window = pygame.display.set_mode((900, 840))
game = Crazy()
game.setup()
suit_list = ['spades', 'hearts', 'clubs', 'diamonds']
numbers_list = ['2','3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
key_numbers_list = ['two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
# Load multiple images
image_list = dict()
screen_info = pygame.display.Info()
sw = screen_info.current_w
sh = screen_info.current_h

for i in range(4):
        for j in range(13):
            filename = f'{numbers_list[j]}_of_{suit_list[i]}.png'  # Replace with your image file name
            image = pygame.image.load(filename)
            image_list[f'{key_numbers_list[j]} of {suit_list[i]}'] = image

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

counter_width = 100
counter_length = sh - 200
for card in game.player_list[0].hand:
    card = pygame.transform.scale(image_list[str(card).lower()], (100, 140))
    window.blit(card, (counter_width, counter_length))
    pygame.display.update()
    counter_width += 100
    if counter_width == 900:
        counter_width = 0
        counter_length += 140
print(game.player_list[0].hand)


'''
counter_width = 0
counter_length = 0
for image in image_list:
    image = pygame.transform.scale(image,(100,140))
    scrn.blit(image, (counter_width, counter_length))
    pygame.display.update()
    counter_width += 100
    if counter_width == 900:
        counter_width = 0
        counter_length += 140
'''

"""print(image_list)
# Display the images
image = image_list[0]
image = pygame.transform.scale(image,(100,140))
scrn.blit(image, (0,0))
pygame.display.update()
"""

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
