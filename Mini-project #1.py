# Mini-project 1 - Rock-paper-scissors-lizard-Spock

import random

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# Convert name to a number
def name_to_number(name):
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    else:
        return 4

# Convert number to a name 
def number_to_name(number):
        
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else:
        return "scissors"

# Game function    
def rpsls(player_choice): 
    
    print 

    # Print the player's choice
    print "Player chooses", player_choice
    
    # Convert the player_choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # Compute random guess for computer_number using random.randrange()
    computer_number = random.randrange(0, 5)
    
    # Convert computer_number to computer_choice using the function number_to_name()
    computer_choice = number_to_name(computer_number)
    
    # Print the computer's choice
    print "Computer chooses", computer_choice
    
    # Compute difference of computer_number and player_number modulo five
    result = (computer_number - player_number) % 5
    
    # Conditionals based on the variable result
    if (result == 3) or (result == 4):
        print "Player wins!"
    elif (result == 1) or (result == 2):
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    
# TEST

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")