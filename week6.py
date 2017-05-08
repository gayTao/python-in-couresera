# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], 

CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hands_list = []	# create Hand object

    def __str__(self):
        rank_str = ""
        for i in range(len(self.hands_list)):
            rank_str += self.hands_list[i].suit+self.hands_list[i].rank+" "
        return rank_str	# return a string representation of a hand

    def add_card(self, card):
        self.hands_list.append(card) 	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        A_exist = False
        for hand in self.hands_list :
            value += VALUES.get(hand.rank)
            if hand.rank == 'A':
                A_exist = True
        if value <= 11 and A_exist:
            value +=10
        return value    
   
    def draw(self, canvas, pos):
        for i in range(len(self.hands_list)):
            pos[0] +=72
            self.hands_list[i].draw(canvas,pos)
            
# define deck class 
class Deck:
    def __init__(self):
        self.deck_list = []	# create a Deck object
        for suit in SUITS :
            for rank in RANKS :
                self.deck_list.append(Card(suit,rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck_list)# use random.shuffle()

    def deal_card(self):
        return self.deck_list.pop()	# deal a card object from the deck
    
    def __str__(self):
        deck_str = " "
        for i in range(len(self.deck_list)):
            deck_str += self.deck_list[i].suit+self.deck_list[i].rank+" "
        return "Deck contains "+deck_str	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player,deck
    deck = Deck()
    deck.shuffle()
    dealer_got = deck.deal_card()
    player_got = deck.deal_card()
    dealer = Hand()
    dealer.add_card(dealer_got)
    outcome = "dealer "+dealer_got.__str__()
    player = Hand()
    player.add_card(player_got)
    outcome = "player "+player_got.__str__()	
    in_play = True

def hit():
    global player,score,in_play
    player_got = deck.deal_card()
    player.add_card(player_got)
    outcome = "player hit"+player_got.__str__()
    if player.get_value() >= 21 :
        outcome = "You have busted"
        score -= 1
        in_play = False
        
def stand():
    global outcome, in_play, dealer, player, score
    if player.get_value() >21 :
        outcome = "the player has busted"
    while(dealer.get_value()<17):
        dealer_got = deck.deal_card()
        dealer.add_card(dealer_got)
    if dealer.get_value() >21 :
        outcome = "You wins"
        score += 1
        in_play = False
        return
    if dealer.get_value() >= player.get_value() :
        outcome = "You have lost"
        score -= 1
        in_play = False
    else :
        outcome = "You wins"
        score += 1
        in_play = False		
    
# draw handler    
def draw(canvas):
    canvas.draw_text(outcome, (400, 30), 30, 'black')
    canvas.draw_text("SCORE:"+str(score), (400, 80), 30, 'black')
    dealer.draw(canvas,[0,200])
    player.draw(canvas,[-72,400])
#draw the back of the card if still in play
    if in_play :
        card_loc = (CARD_CENTER[0],CARD_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_SIZE,[CARD_CENTER[0], 200 + CARD_CENTER[1]], CARD_SIZE)
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric