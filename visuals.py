import tkinter as tk
from card import Card
import sys
sys.dont_write_bytecode = True

root = tk.Tk()

canvas = tk.Canvas(root, width=1000, height=800)
canvas.pack()

# Create a card
card = Card('heart', 'king', canvas, 50, 50, 100, 150, 'red')


# Should be last
root.mainloop()