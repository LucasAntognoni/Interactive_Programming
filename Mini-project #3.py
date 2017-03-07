# Mini-project 3 - Stopwatch: The Game

import simplegui

# Global variables

time = 0
x = 0
y = 0
running = False

# Function that formats the time to A:BC.D format

def format(t):
    
    A = (t // 600)
    
    B = (((t // 10) % 60) // 10)
    
    C = (((t // 10) % 60) % 10)
    
    D = (t % 10) 
    
    return str(A) + ":" + str(B) + str(C) + "." + str(D)

# Function that returns the "x/y" score string

def score():
    
    return str(x) + "/" + str(y)

# Buttons handlers

def start_button():
    
    global running 
    
    running = True
    
    timer.start()
    
def stop_button():
    
    global running 
    global x
    global y
    
    timer.stop()
    
    if running == True:
        
        if (time % 10) == 0:
            x += 1
            y += 1
            
        else:
            y += 1
        
        running = False
        
def reset_button():
    
    global time
    global x
    global y
    
    time = 0
    x = 0
    y = 0
    
# Timer handler

def timer_handler():
    
    global time
    
    time += 1
    
    print time

# Draw handler

def draw_handler(canvas):
    canvas.draw_text(format(time), [90, 110], 30, "White")
    canvas.draw_text(score(), [170, 50], 24, "Red")
        
# Create frame

frame = simplegui.create_frame("Stopwatch", 250 , 200)

# Register event handlers

frame.add_button('Start', start_button, 100)
frame.add_button('Stop', stop_button, 100)
frame.add_button('Reset', reset_button, 100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)

# Start frame
frame.start()
