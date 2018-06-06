from deck import Deck_Generator
from pprint import pprint
from tabulate import tabulate


class Hand:
    hand = {}
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
    
    def __str__(self):
        handList = []
        for h in self.hand:
            handList.append("\n".join(str(c) for c in h["Cards"]))
        return tabulate(handList)
            
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
    hand = None
    deck = None
    hit_Command = None
    def __init__(self,__deck,__commands):
        self.deck = __deck
        self.hand = Hand()
        self.hit_Command = __commands["Hit"]
    
    def hit(self,handNum):
        self.hit_Command.execute(Hand,handNum)

    def stay(self):
        pass

    def __str__(self):
        return str(self.hand)

class Dealer(BasePlayer):

    def __init__(self,__deck,__commands):
        super().__init__(__deck,__commands)

class Player(BasePlayer):
    auto = None
    def __init__(self,__deck,__commands):
        super().__init__(__deck,__commands)
    

class commands():
    pass

class hit_Command(commands):
    basePlayer = None 
    deck = None
    def __init__(self,__deck):
        self.deck = __deck
    
    def execute(self,hand,handNum):
        
        c = self.deck.deal_card()
        
        if c == None:
            self.deck.shuffle()
        
        hand.addCard(c,handNum)

class BlackJack:
    players = []
    dealer = None
    deck = None

    def __init__(self):
        pass
    def CreateDeck(self,num_Decks):
        deckGen= Deck_Generator(num_Decks)
        self.deck = deckGen.deck


    def addPlayers(auto = false)
        
        if auto == False:
            hit = hit_Command(self.deck)
            self.dealer = Dealer(self.deck,hit)

            for i in range(num_Players):
                self.players.append(Player(self.deck,hit))
    

    def playGame(self,rounds=1):

        #Initial Setup - Hand Everybody two Cards!
        for i in range(rounds):
            everyOne = self.players + [self.dealer]
            for people in everyOne * 2:
                people.hit(1)

            for people in self.players:
                = input("Hit or Stay or Double")


                    

            

