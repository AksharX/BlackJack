from deck import Deck_Generator
from people import Dealer, Player




class BlackJack:
    players = []
    dealer = None
    deck = None

    def __init__(self,num_Decks):
        deckGen= Deck_Generator(num_Decks)
        self.deck = deckGen.deck
        self.deck.shuffle()
        self.dealer = Dealer(self.deck)

    def addPlayers(self,num_Players,auto = False):
        
        if auto == False:            
            for _ in range(num_Players):
                self.players.append(Player(self.deck))


    def playGame(self,rounds=1):

        #Initial Setup - Hand Everybody two Cards!
        for _ in range(rounds):
            everyOne = self.players + [self.dealer]
            for people in everyOne:
                people.hit(1)

            dealer_Show_Card = self.dealer.showingCard()
            print("Dealer Face Up Card: " + str(dealer_Show_Card)) 
            
            for player in self.players:
                if player.auto == False:
                    
                    print("Your Hand is:\n" + str(player.hand))
                    command = input("Hit or Stay or Double  or Automatic Play: ")
                    assert command in {"H","h","S",'s',"D","d","A",'a'}           

                    if command in ("H","h"):
                        player.hit(1)

                    print("Your Hand is:\n" + str(player.hand))  

                else:
                    #Implement Automatic Play
                    pass 




                    

            

