class CPU:
    def __init__(self):
        self.hand = []

    def play_card(self, index):
        value = self.hand[index]
        self.hand.remove(index)
        return value
    
    def __str__(self):
        return f"Hand: {self.hand}"

    def __repr__(self):
        return f"Hand: {self.hand}"
