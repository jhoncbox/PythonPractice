import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

# Class Definitions
# Step 2: Create a Card Class
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

# Step 3: Create a Deck Class
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "the decs has : " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
# ------------------------------------
#testing 
test_deck = Deck()
# print(test_deck)
# # shufling the deck
test_deck.shuffle()
# print(test_deck)
# # ------------------------------------

# Step 4: Create a Hand Class
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        # the card passed in is from
        # the Deck.deal() ---> single_card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
        # track for aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        # THEN CHANGE MY ACE TO BE A 1 INSTEAD OF 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1 

# --------------------------------
# PLAYER
# test_player = Hand()
# # Deal one card from the deck
# pulled_card = test_deck.deal()
# print(pulled_card)
# # adding the card to the player's hand
# test_player.add_card(pulled_card)
# print(test_player.value)
# # adding another card
# test_player.add_card(test_deck.deal())
# print(test_player.value)
# --------------------------------
# Step 5: Create a Chips Class
class Chips:
    def __init__(self,total=100):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

# Function Defintions#
# Step 6: Write a function for taking bets
def take_bet(chips):    
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            ("sorry please provide a number")
        else:
            if chips.bet > chips.total:
                print("sorry you dont have enough chips, you have {}".format(chips.total))
            else:
                break

# Step 7: Write a function for taking hits
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# Step 8: Write a function prompting the Player to Hit or Stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input("Hit or Stand, enter h or s: ")
        if x == 'h':
            hit(deck,hand)
        elif x == 's':
            print("player stands, Dealer's turn")
            playing = False
        else:
            print("sorry i did not understand, please enter h or s")
            continue
        break

# Step 9: Write functions to display cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

# Step 10: Write functions to handle end of game scenarios
def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()
    
def push(player,dealer):
    print("dealer and player tie, PUSH")


while True:
    # Print an opening statement
    print("WELCOME TO JHON'S CASINO")
    # Create & shuffle the deck, deal two cards to each player
    deck  = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total 
    print("\n Player Total chips are: {}".format(player_chips.total))
    # Ask to play again
    new_game = input("would you like to play again? y/n: ")
    if new_game[0] == 'y':
        playing = True
        continue
    else:
        print("thank you for playing")
        break