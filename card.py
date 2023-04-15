class Card:
    def __init__(self, suit, rank, canvas, x, y, width, height, color):
        self._suit = suit
        self._rank = rank
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x+width, y+height, fill=color)
        self.canvas.tag_bind(self.id, '<ButtonPress-1>', self.start_drag)
        self.canvas.tag_bind(self.id, '<ButtonRelease-1>', self.stop_drag)
        self.canvas.tag_bind(self.id, '<B1-Motion>', self.on_drag)
        self.dragging = False
        self.start_x = 0
        self.start_y = 0
        self.width = width
        self.height = height

    def getSuit(self):
        return self._suit

    def getValue(self):
        return self._rank

    def __lt__(self, other):
        return (self._rank < other._rank)

    def __gt__(self, other):
        return (self._rank > other._rank)

    def __le__(self, other):
        return (self._rank <= other._rank)

    def __ge__(self, other):
        return (self._rank >= other._rank)

    def __eq__(self, other):
        return (self._rank == other._rank)

    def __ne__(self, other):
        return (self._rank != other._rank)

    def __str__(self):
        return f"{self._rank} of {self._suit}"
    
    def start_drag(self, event):
        self.dragging = True
        self.start_x = event.x
        self.start_y = event.y

    def stop_drag(self, event):
        self.dragging = False

    def on_drag(self, event):
        if self.dragging:
           dx = event.x - self.start_x
           dy = event.y - self.start_y
           self.canvas.move(self.id, dx, dy)
           self.start_x = event.x
           self.start_y = event.y

