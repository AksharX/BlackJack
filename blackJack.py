from deck import Deck_Generator
from pprint import pprint

deck_Gen = Deck_Generator(4)
deck = deck_Gen.deck

class Hand:
    hand = {
        1:{
            "Cards":[],
            "Hand Total":0
        }
    }
    def __init__(self):
        pass
    def addCard(self,card,handNum):
        if handNum not in self.hand:
            self.hand[handNum] = {
                "Cards":[card],
                "Hand_Total":self.calculateCardTotal([card]),
            }
        else:
            self.hand[handNum]["Cards"].append(card)
            self.hand[handNum]["Hand_Total"] = self.calculateCardTotal(self.hand[handNum]["Cards"])

            
    def calculateCardTotal(self,cards):
        total = 0
        Aces_Count = 0
        for c in cards:
            if len(c.value()) == 1:
                total += c.value(0)
            else:
                Aces_Count += 1
                total += c.value(1)
        if total > 21 and Aces_Count > 0:
            for x in range(Aces_Count):
                total -= 10
        


class BasePlayer:
    hand = []
    deck = None
    def __init__(self,__deck):
        self.deck = __deck
        hand = Hand()
    def addCard(self,card):
        self.cards.append(card)
    def hit(self):
        c = self.deck.deal_card()
        if c == None:
            self.deck.shuffle()
        self.cards.append(c)
    def stay(self):
        pass

    def __str__(self):
        return "\n".join(self.cards)

class Dealer(BasePlayer):

    def __init__(self):
        super().__init__(self)

class Player(BasePlayer):
    def __init__(self):
        pass


class commands():
    pass
    def execute(self):
        pass

# class hit_Command(commands):
#     basePlayer = None 
#     deck = None
#     def __init__(self,__basePlayer,__deck):
#         self.basePlayer = __basePlayer
#         self.deck = __deck
    
#     def execute(self):
#         c = deck.deal_card
        
#         if c == None:
#             deck.shuffle()
             
#         self.basePlayer.addCard(c)


    


