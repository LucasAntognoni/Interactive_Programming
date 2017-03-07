# Mini-project #5 - Memory

import simplegui
import random

# Globals

cards = range(0, 8) * 2
exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
state = 0
turns = 0
card1 = 0
card2 = 0

# Helper function to initialize globals

def new_game():
   
    global state, turns

    random.shuffle(cards)
        
    state = 0
    turns = 0
    
    for i in range(len(cards)):
        exposed.insert(i, False)
        
    label.set_text("Turns = " + str(turns))
    
# Define event handlers

def mouseclick(pos):
   
    global state, turns, card1, card2
    
    index = pos[0] // 50
        
    if state == 0:
        if exposed[index] == False:
            card1 = index
            exposed[index] = True
            state = 1
        
    elif state == 1 and index != card1:
        
        turns += 1
        label.set_text("Turns = " + str(turns))
        
        if exposed[index] == False:
            card2 = index
            exposed[index] = True
            state = 2
            
    elif state == 2 and index != card2:
            
        if cards[card1] != cards[card2]:
            exposed[card1] = False
            exposed[card2] = False
        
        if exposed[index] == False:
            card1 = index
            exposed[index] = True
            state = 1
            
def draw(canvas):
    
    posc = 24.5
    posn = 0
    
    for i in range(len(cards)):
           
        canvas.draw_line((posc, 0), (posc, 100), 48, 'Green')
        posc += 50
            
        if exposed[i] is True:
            posn = (i * 50) + 5
            canvas.draw_line((posn + 19.6, 0), (posn + 19.6, 100), 48, 'Black')    
            canvas.draw_text(str(cards[i]), [posn, 75], 60, 'White')

# Create frame and add a button and labels

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# Register event handlers

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# Get things rolling

new_game()
frame.start()