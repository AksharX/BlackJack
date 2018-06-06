import random
import pprint
import math 


class Card:
    __suit = None
    __value = None
    
    def __init__(self,suit,value):
        self.__suit = suit
        self.__value = value

    def __str__(self):
        if self.__value == 11:
            return "Jack of " + self.__suit 
        elif self.__value == 12:
            return "Queen of " + self.__suit
        elif self.__value == 13:
            return "King of " + self.__suit
        elif self.__value == 1:
            return "Ace of " + self.__suit
        else:
            return str(self.__value) + " of " + self.__suit
        
    def value(self):
        if self.__value == 14:
            return (1,11)
        elif self.__value > 10:
            return (10)
        else:
            return (self.__value)
    
class Deck:
    __deck = []
    __discard_Pile = []
    def __init__(self,cards):
        self.__deck = cards
    
    def shuffle(self):
        self.__deck = self.__deck + self.__discard_Pile
        self.__discard_Pile = []
        for i in range(len(self.__deck)):
            new_i = random.randrange(0,len(self.__deck))
            temp = self.__deck[new_i]
            self.__deck[new_i] = self.__deck[i]
            self.__deck[i] = temp        

    def deal_card(self):
        c = self.__deck.pop()
        self.__discard_Pile.append(c) 
        return c
        

    def __str__(self):
        deck_Print = ""
        for c in self.__deck:
            deck_Print = deck_Print  + str(c) + "\n"
        return deck_Print
    def __len__(self):
        return len(self.__deck)   

    def __iter__(self):
        return self.__deck

class Deck_Generator:
    __suits = ("Hearts","Diamonds","Spades","Clubs")
    __values = tuple(x for x in range(1,14))
    __card_List = []
    deck = None

    def __init__(self,numDecks):
        
        for suit in self.__suits:
            for value in self.__values:
                c = Card(suit,value)
                self.__card_List.append(c)
        
        self.deck = Deck(self.__card_List * numDecks)
        

class TestRandomAccurary:
    cardsDic = {}
    def __init__(self,deck,NumTests):
        
        for x in range(NumTests):
            c = str(deck.deal_card())
            if c in self.cardsDic:
                self.cardsDic[c]["Num_Appeared"] += 1
                self.cardsDic[c]["Pecentage"] = round(self.cardsDic[c]["Num_Appeared"]/NumTests,2)
            else:
                self.cardsDic[c] = {
                "Num_Appeared":1,
                "Pecentage":1/NumTests
                }
            deck.shuffle()
        pprint.pprint(self.cardsDic)
        print(len(self.cardsDic))
    
          
            
