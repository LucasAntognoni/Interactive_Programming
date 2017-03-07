# Mini-project #6 - Blackjack

import simplegui
import random

# Load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# Global variables
in_play = True
outcome = ""
score = 0
end = 0

# Cards globals
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# Classes
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
        
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                         [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
class Hand:
    
    def __init__(self):
        
        self.cards = []	

    def __str__(self):
        
        string = ""
        
        for	c in self.cards:
            
            string += str(c) + ' '
            
        return "Hand contains " + string
    
    def add_card(self, card):
        
        self.cards.append(card)	

    def get_value(self):
        
        value = 0
        
        for c in self.cards:
            value += VALUES.get(c.get_rank())
        
        for c in self.cards:
            
            if c.get_rank() == 'A':
            
                if (value + 10) <= 21:
                    value += 10
        
        return value		
   
    def draw(self, canvas, pos):
        
        for c in self.cards:
            
            c.draw(canvas, pos); 
            
            pos[0] += 100
     
    def new_hand(self):
        
        self.cards = []
    
class Deck:
    
    def __init__(self):
        
        self.cards = []
        
        for s in SUITS:
            
            for r in RANKS:
                
                self.cards.append(Card(s, r))
        
        random.shuffle(self.cards)
        
    def shuffle(self):
        
        random.shuffle(self.cards)

    def deal_card(self):
        
        return self.cards.pop()
    
    def __str__(self):
        
        string = ""
        
        for c in self.cards:
            
            string += str(c) + ' '

        return "Deck contains " + string
    
    def new_deck(self):
        
        self.cards = []
        
        for s in SUITS:
            
            for r in RANKS:
                
                self.cards.append(Card(s, r))
        
        random.shuffle(self.cards)
    
# Handlers    
def deal():
    
    global outcome, in_play, end, score, DECK, PLAYER, DEALER
    
    if len(DEALER.cards) == 2 and end == 0:
        score -= 1
        DECK.new_deck()
        PLAYER.new_hand()
        DEALER.new_hand()
        end = 0
        in_play = True
        
    elif end == 1:
        
        DECK.new_deck()
        PLAYER.new_hand()
        DEALER.new_hand()
        end = 0
        in_play = True
    
    PLAYER.add_card(DECK.deal_card())
    PLAYER.add_card(DECK.deal_card())
    
    DEALER.add_card(DECK.deal_card())
    DEALER.add_card(DECK.deal_card())
    
    outcome = "Hit or Stand?"

def hit():
    
    global score, in_play, outcome, end
    
    if end == 0:
    
        if PLAYER.get_value() <= 21:

            PLAYER.add_card(DECK.deal_card())

            if PLAYER.get_value() > 21:

                in_play = False
                end = 1
                score -=1
                outcome = "Dealer wins! New deal?"

        else:
            outcome = "Dealer wins! New deal?"
            end = 1
                         
def stand():
    
    global score, outcome, in_play, end
    
    in_play = False
    
    if PLAYER.get_value() > 21:
        
        outcome = "Dealer wins! New deal?"
        
    else:
        
        if end == 0:
        
            while DEALER.get_value() <= 17:

                DEALER.add_card(DECK.deal_card())            

            if DEALER.get_value() > 21:

                outcome = "You win! New deal?"
                score += 1
                end = 1

            else:

                if PLAYER.get_value() > DEALER.get_value():

                    outcome = "You win! New deal?"
                    score += 1
                    end = 1

                else:

                    outcome = "Dealer wins! New deal?"
                    score -= 1
                    end = 1

def draw(canvas):

    canvas.draw_text('Blackjack', (30, 80), 48, 'Orange')
    canvas.draw_text("Score: " + str(score), (350, 150), 36, 'Black')
    canvas.draw_text(outcome, (270, 420), 24, 'Yellow')
    
    canvas.draw_text('Dealer', (40, 200), 36, 'Black')
    DEALER.draw(canvas, [40, 250])
    
    if in_play == True:
        
        card_back_loc = (CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0] * 0, 
                         CARD_BACK_CENTER[1] + CARD_BACK_SIZE[1] * 0)
        
        canvas.draw_image(card_back, card_back_loc, CARD_BACK_SIZE, 
                         [40 + CARD_BACK_CENTER[0], 250 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    
    canvas.draw_text('Player', (40, 420), 36, 'Black')
    PLAYER.draw(canvas, [40, 470])

# Frame initialization
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# Create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# Initialize globals
PLAYER = Hand()
DEALER = Hand()
DECK = Deck()

# Run it!
deal()
frame.start()