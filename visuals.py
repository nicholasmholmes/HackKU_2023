import tkinter as tk
import os

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create a card
card = Card(canvas, 50, 50, 100, 150, 'red')


# Should be last
root.mainloop()