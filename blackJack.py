from deck import Deck_Generator
from pprint import pprint

deck_Gen = Deck_Generator(4)
deck = deck_Gen.deck

class basePlayer:
    cards = []
    def __init__(self):
        pass
    def addCard(self,card):
        self.cards.append(card)
    def hit(self):
        pass    
    def stay(self):
        pass
    def __str__(self):
        return "\n".join(self.cards)

class dealer(basePlayer):

    def __init__(self):
        super().__init__(self)

class Player(basePlayer):
    def __init__(self):
        pass

class BlackJack():
    pass

