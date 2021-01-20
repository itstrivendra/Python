import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank+  " of " + self.suit

class Deck():
    
    def __init__(self):
        self.deck = [] #Starting with empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

#Testing(*)
#test_deck = Deck()
#test_deck.shuffle()
#print(test_deck) 


class Hand:
    def __init__(self):
        self.cards = [] #Starting with Empty list likewise Deck class
        self.value = 0 #Starting with value 0
        self.aces = 0 # Attribute to keep track of Aces
    
    def add_card(self,card):
         #Card passed in
        # from Deck.deal to singleCard(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
        
        #Track Aces
        if card.rank == 'Ace':
            self.aces += 1
                    
    def adjust_for_ace(self):
        #If total value is less than 21 and I still have an ace
        #then change ace to be 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        

test_deck = Deck()
test_deck.shuffle()

#Player
test_player = Hand()
# Deal 1 card from deck(suit,rank)
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

test_player.add_card(test_deck.deal())
test_player.value

class Chips:
    
    def __init__(self,total=100):
        self.total = total #Default Value
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -=self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet ? \n"))
        except:
            print("Sorry please provide an integer value")
        else:
            if chips.bet > chips.total:
                print("You don't have enough chips ! You have".format(chips.total))
            else:
                break

def hit(deck,hand):
    
    #single_card = deck.deal()
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input('Hit or Stand ? Enter h or s \n ')
        
        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif x[0].lower() == 's':
            print("Player stands, Dealer's turn ")
            playing = False
            
        else:
            print("Enter s or h only")
            continue

def show_some(player,dealer):
    print('Dealers Hand')
    print('One card hidden')
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND:')
    for card in player.cards:
        print(card)
        
def show_all(player,dealer):
    print('DEALER HAND:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYER HAND :')
    for card in player.cards:
        print(card)

def player_busts(player,dealer,chips):
    print("Bust Player")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("Player WINS")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print("DEALER BUSTS, Player WINS")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer Wins")
    chips.lose_bet()
    
def push(player,dealer):
    print('Dealer and Player Tie ! PUSH')


while True:
    print("WELCOME TO BLACKJACK")
    #Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    player_chips = Chips() #Default value is 100
    
    #Prompt the Player for their bet
    take_bet(player_chips)
    
    #Show cards(but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:
        #Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        #Show cards(Keep one hidden)
        show_some(player_hand,dealer_hand)
        
        #If player's hand exceeds 21
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
            
    # If Player hasn't busted, Play dealer's hand until reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < player_handand.value:
            hit(deck,dealer_hand)
            
        #Show all cards
        show_all(player_hand,dealer_hand)
        
        #Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
            
    #Inform Player of their total chips
    print('\n Player total chips are at: {}'.format(player_chips.total))
    #Ask to play again
    new_game = input("Want to play again ? y/n ")
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for Playing !')
        
        break