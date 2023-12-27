
# Online Python - IDE, Editor, Compiler, Interpreter
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

ColorCards = [str(n) for n in range(1, 10)] + list("RSD")



class UnoDeck:
    
     ranks = ["0"] + [str(n) for n in ColorCards for _ in range(2)] 
     wildcards = [w for w in ["plusFour","default"] for _ in range(4)]
     suits = 'red blue green yellow'.split()
     
     def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
            for rank in self.ranks] + [Card(rank,"WildCard") for rank in self.wildcards]
            
     def __len__(self):
        return len(self._cards)
        
     def __getitem__(self, position):
        return self._cards[position]
        
deck = UnoDeck()

print(len(deck))
