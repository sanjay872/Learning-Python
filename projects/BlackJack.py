import random

class Card: # creating cards by suit and rank eg: 7 0f hearts ; 7 is rank and heart is suit
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self): #gets triggered if print statement is used on this class object
        return f"{self.rank['rank']} of {self.suit}"

class Deck: #Deck for playing the game
    def __init__(self):
        self.cards=[]
        self.suits=["hearts","spades","clubs","diamonds"]
        # A has 11 as rank point; k,Q and J has 10 points; other cards points based on their numbers
        self.ranks = [
                {"rank": "A", "value": 11},
                {"rank": "2", "value": 2},
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "J", "value": 10},
                {"rank": "Q", "value": 10},
                {"rank": "K", "value": 10},
            ]

    def createCards(self): #create the deck
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit,rank))

    def shuffle(self): #shuffle the cards
        random.shuffle(self.cards)

    def deal(self,number=1): #get card from the deck
        cards_dealt=[]
        if len(self.cards)>0:
            for i in range(number):
                cards_dealt.append(self.cards.pop())
        return cards_dealt

class Hand: #Players hand
    def __init__(self,dealer=False):
        self.cards=[]
        self.value=0
        self.dealer=dealer
    
    def add_card(self,card_list): # adding cards to player hand
        self.cards.extend(card_list)
    
    def calculate_card_value(self):
        self.value=0
        has_ace=False

        for card in self.cards: # seeing all the cards in hand
            self.value+=int(card.rank["value"]) #adding the value
            if card.rank["rank"]=='A': #checking if player has ace card 
                has_ace=True
        
        if has_ace and self.value > 21: # has ace card and total card value > 21 deduct 10 points
            self.value-=10
    
    def get_value(self): # returns current value of cards in hand
        self.calculate_card_value() # calculate value
        return self.value

    def is_blackjack(self): # check if we hit blackjack
        return True if self.value == 21 else False
    
    def display(self,show_all_dealer_cards=False): #to display
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''') #its dealer or you 
        for index,card in enumerate(self.cards): # show the cards
            if index==0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print('Hidden')
            else: # the card will be show if its players card
                print(card)
        if not self.dealer:
            print("Value: ",self.get_value()) # value of cards player holds
        print()

class Game:
    def play(self):
        game_number=0
        games_to_play=0
        while games_to_play<=0:
            try:
                games_to_play=int(input("How many games do u want to play?"))
            except:
                print("U must enter a number!")
        while game_number<games_to_play:
            game_number+=1
            
            #making the deck
            deck=Deck()
            deck.createCards()
            deck.shuffle()

            #start the game
            player_hand=Hand()
            dealer_hand=Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())
            
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.checkForWinner(player_hand,dealer_hand):
                continue
            
            choice=""
            while player_hand.get_value() < 21 and choice not in ["s","stand"]: 
                choice=input("Please choice 'Hit' or 'Stand':").lower()
                print()
                while choice not in ["h","hit","s","stand"]:
                    choice=input("Please enter 'Hit' or 'Stand' (or H/S)").lower()
                    print()
                if choice in ["hit","h"]:
                    player_hand.add_card(deck.deal())
                    player_hand.display()
            
            if self.checkForWinner(player_hand,dealer_hand):
                continue

            player_hand_value=player_hand.get_value()
            dealer_hand_value=dealer_hand.get_value()

            if dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand_value=dealer_hand.get_value()
            
            dealer_hand.display(show_all_dealer_cards=True)

            if self.checkForWinner(player_hand,dealer_hand):
                continue

        print("Final Results")
        print("Your hand:", player_hand_value)
        print("Dealer's hand:",dealer_hand_value)

        self.checkForWinner(player_hand,dealer_hand,True)
        print("\nThanks for playing!")

    def checkForWinner(self,player_hand,dealer_hand,game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You lose!!")
                return True
            elif dealer_hand.get_value() > 21:
                print("You win!")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Tie!")
                return True
            elif player_hand.is_blackjack():
                print("You have a blackjack, u win!!")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer got blackjack,he wins!")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")
            elif player_hand.get_value() < dealer_hand.get_value():
                print("Dealer win!")
            else:
                print("Tie!")
            return True
        return False

game=Game()
game.play()