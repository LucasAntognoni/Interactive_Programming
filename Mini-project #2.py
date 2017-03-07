# Mini-project 2 - Guess the number!

import math
import random
import simplegui

# Global Variables

secret_number = 0
guesses = 0
game_range = 100

# New game function
def new_game(flag):
    
    global secret_number
    global guesses
    
    # If it's the first game or 
    # the player won/lost a game
    # the global variables are set
    
    if flag == True:
        
        if game_range == 100:
            secret_number =  random.randrange(0, 100)   
        
        elif game_range == 1000:
            secret_number =  random.randrange(0, 1000)    	 
        
        # For debugging
        else:
            print "Error" 
        
        # Calculates the number of
        # guesses based on the range
        
        guesses = int(math.ceil(math.log(game_range, 2)))
    
    # If the player pressed the 
    # buttons range [0, 100)/[0, 1000),
    # the function just prints "New game" message
    
    print "New game. Range is [0," + str(game_range) + ")"
    print "Number of remaining guesses is ", guesses, "\n"

# Sets the game to range [0, 100)
# returning a new game
def range100():

    global secret_number
    global guesses
    global game_range
    
    secret_number = random.randrange(0, 100)
    guesses = 7
    game_range = 100
    
    return new_game(False)
 
# Sets the game to range [0, 1000)
# returning a new game    
def range1000():
    
    global secret_number
    global guesses
    global game_range
    
    secret_number = random.randrange(0, 1000)
    guesses = 10
    game_range = 1000
    
    return new_game(False)

# Handles the player inputs
def input_guess(guess):
    
    global guesses
    
    # String to int
    n = int(guess)
    
    print "Guess was", n
        
    if n > secret_number:
        print "Lower!"
        guesses -= 1
        print "Number of remaining guesses is ", guesses, "\n"
            
    elif n < secret_number:
        print "Higher!"
        guesses -= 1
        print "Number of remaining guesses is ", guesses, "\n"
        
    else:
        print "Correct!\n"
        new_game(True)
               
    if guesses == 0:
        print "Out of guesses! The number was", secret_number, "\n"
        new_game(True)
    
# Creates the game window
frame = simplegui.create_frame('Guess the number', 200, 200)

# Adds the buttons and text input to the window
frame.add_button('Range [0, 100)', range100, 120)
frame.add_button('Range [0, 1000)', range1000, 120)
frame.add_input('Make a guess!', input_guess, 120)

# Starts the frame
frame.start()

# Create a new game
new_game(True)


