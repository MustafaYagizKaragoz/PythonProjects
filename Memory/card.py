class Card:

    def __init__(self, symbol):
        self.is_open = False
        self.symbol = symbol
    
    def reveal(self):
        self.is_open = True
    
    def hide(self):
        self.is_open = False
    
    def __str__(self) -> str:
        return self.symbol if self.is_open else "X"
    
    
