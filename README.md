# HackKU_2023 🌐
Hack KU event, team project made by Nicholas Holmes, Alex Doehring, Colin Treanor, and Raymann Singh.
We are all freshmen Engineering Students -- *three Computer Science students, One Aerospace* -- at Kansas University.

For this event we are trying to make a user playable version of the Crazy Eights card game using the pygame extension.

### <align center> *_How to play:_* ###
  Crazy Eights is a card game where the goal is to be the first player to get rid of all the cards in his hand. The game can be played with a standard playing card deck for 4 players, with 7 cards dealt to each player. The remaining cards go in a stack face down in the middle. Turn the top card over. The player to the left of the dealer starts the game by placing a matching card on the discard pile. The game continues clockwise, and each player must play a card that matches the current card in either suit or rank. If no card is matching, draw one card from the draw pile. The player who is the first to have no cards left wins the game. 

  ## 🔧 _Pygame_ 🔧
  This program requires the usage of a python extension called  `pygame` 
  
  1. Pygame is a popular extension module for the Python programming language that allows developers to create interactive games and multimedia applications. It provides a powerful set of tools and libraries for creating and manipulating graphics, sound, and input events.

  2. Pygame is built on top of the SDL (Simple DirectMedia Layer) library, which provides low-level access to computer hardware, such as graphics cards and sound cards. This means that Pygame can be used to create high-performance applications that utilize hardware acceleration for smooth graphics and fast sound processing.

  3. Pygame provides a number of useful features, such as sprites, collision detection, event handling, and sound effects, which make it easy to create complex games and applications.

  4. It also supports a wide range of file formats for images, sounds, and fonts, making it easy to import and use existing assets in your game or application. Additionally, Pygame provides support for various input devices, such as keyboards, mice, and joysticks, which makes it easy to create interactive applications that respond to user input.

  #### Implementation:
  This extension can be easily implemented like most other functions in python by beginning the file with:
  
  ```bash
import pygame
```
  #### Example:
   ```bash
  import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
win_width = 640
win_height = 480

# Create the window
win = pygame.display.set_mode((win_width, win_height))

# Set the title of the window
pygame.display.set_caption("My Pygame Window")

# Set the color of the rectangle
rect_color = (255, 0, 0)  # Red

# Set the dimensions and position of the rectangle
rect_x = 100
rect_y = 100
rect_width = 50
rect_height = 50

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    win.fill((255, 255, 255))  # White

    # Draw the rectangle
    pygame.draw.rect(win, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # Update the screen
    pygame.display.update()

# Clean up Pygame
pygame.quit()

```
  This code creates a base display template by setting the height and width parameters using the x and y axis. 
  It also implmements a basic running loop that most games would utilize -- *including ours* -- in order to run the game 
  until the win condition(or something similar) is met.
  
  ## 🔗 How do we make a *multiplayer* game work using python? 🔗
  
  First we need to clarify what multiplayer means in this context. We are not referring to an online multiplayer game that allows you to connect to other players on a server, but simply a game that requires multiple people or *players* in order to properly function.
  
  With this basic undertsanding, we can get into the process of our game creation!
  
  We first began by creating a simple player class that could operate the functions a computer player might need, which looked something like this:
   
  ```bash
  class Player:
    def __init__(self):
        self.hand = []

    def play_card(self, index):
        value = self.hand[index]
        self.hand.remove(index)
        return value
```
 
It ended up being much simpler than we had initially thought, as our "players" only needed a function allowing them to play a card, which the valid parameters for are described in our actual game class. Along with simple `__str__` and `__repr__` methods.

This was one of many components necessary to properly run our game. We also relied on a `deck`, `card`, `crazy8` -- *main code that operates the game* -- and `visuals`

## Speaking of visuals... 🔍

After finishing the skeleton for the game and making sure it runs properly we had to tackle our next hurdle: visual implementation of cards and a display that players can properly navigate and interact with.

This was definitely one of the more entertaining parts of the project, as we progressively watched our game develop in front of us on a screen. 
  
### One of the Main Functions
  The `blit()` function is a Pygame method that is used to copy a surface onto another surface. It is short for "block transfer", and is used to transfer the pixel data from one surface to another.

Here is the general syntax for the `blit()` function:
 
  ```bash
  target_surface.blit(source_surface, target_position)
```
  
  - Here, `target_surface` is the surface onto which you want to draw, `source_surface` is the surface that you want to copy, and `target_position` is the position on the target surface where you want to draw the source surface.
  - The `blit()` function takes the pixel data from the source surface and copies it onto the target surface at the specified position. You can use the `blit()` function in a variety of ways to create complex graphics and animations in your Pygame game. For example, you can use it to draw images, sprites, text, and other shapes onto your game screen. It is a versatile and powerful tool that is essential for creating dynamic and interactive Pygame games.
  

By utilizing `blit()` along with coordinates and images we're able to manipulate the display to fit our game's needs and show the player their own hand as well as the discard pile and the card they need to play on. Fun!!
  
  
 # 💖 *Thank you!* 💖
 Though we only previewed a few parts of our project, it took these small portions in tandem with many other lines of code to finally have a working product, and we're very thankful for the chance to present our work.
 Through a lot of effort, and *a lot* of energy drinks... we were able to create our game. We hope it might seem as enjoyable to others as it was for us.
  This has been an amazing event, both as a fun way to connect with others and an incredible learning experience. Our entire team would like to thank all of the organizers & sponsors for the work they did to make HackKU 2023 happen.
  
