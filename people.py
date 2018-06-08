from deck import Deck_Generator
from pprint import pprint
from tabulate import tabulate

class Hand:
    hand = {}
    
    def __init__(self):
        pass
    
    def getCard(self,hand_Number,position):
        return self.hand[hand_Number]["Cards"][position]
    
    def addCard(self,card,handNum):
        if handNum not in self.hand:
            self.hand[handNum] = {
                "Cards":[card],
                "Hand_Total":self.calculateCardTotal([card]),
                "Split": self.splitPossible([card])
            }
        else:
            self.hand[handNum]["Cards"].append(card)
            self.hand[handNum]["Hand_Total"] = self.calculateCardTotal(self.hand[handNum]["Cards"])
            self.hand[handNum]["Split"] = self.splitPossible(self.hand[handNum]["Cards"])
            
    
    def __repr__(self):
        handList = []
        for _ , h in self.hand.items():
            cList = [str(c) for c in h["Cards"]]
            vList = [str(h["Hand_Total"])]
            cards = "\n".join(cList + vList)
            
            handList.append([cards])
        return tabulate(handList)
    def splitPossible(self,cards):
        pass

    def calculateCardTotal(self,cards):
        print("Running Calculation")
        total = 0
        Aces_Count = 0
        for c in cards:
            if c.value is not 14:
                total += c.value()
            else:
                Aces_Count += 1
                total += c.value()
        if total > 21 and Aces_Count > 0:
            for _ in range(Aces_Count):
                total -= 10
        return total

class BasePlayer:
    hand = None
    deck = None
    def __init__(self,__deck):
        self.deck = __deck
        self.hand = Hand()
    
    def hit(self,handNum):
        c = self.deck.deal_card()
        
        if c == None:
            self.deck.shuffle()
        
        self.hand.addCard(c,handNum)


    def stay(self):
        pass

    def handleCommand(self,command,handNum):
        if command in {"h","H"}:
            self.hit(handNum)
        elif command in {"s", "S"}:
            self.stay()
        else:
            pass

    def revealCards(self):
        return self.hand

    def __repr__(self):
        return str(self.hand)

class Dealer(BasePlayer):

    def __init__(self,__deck):
        super().__init__(__deck)

    def showingCard(self):
        return self.hand.getCard(1,1)


class Player(BasePlayer):
    auto = None
    __rules__ = {}

    def __init__(self,__deck,__auto = False):
        super().__init__(__deck)
        self.auto = __auto

    def handleCommand(self,command,handNum):
        super().handleCommand(command,handNum)
        if command in {"sp","SP"}:
            self.split(handNum)
        elif command in {"d","D"}:
            self.doubleDown(handNum)

    def doubleDown(self,handNum):
        pass

    def split(self,handNum):
        pass
    
    def automaticPlay(self,dealerCard):
        pass

        

