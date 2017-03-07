# Mini-project 4 - Pong

import simplegui
import random

# Initialize globals - pos and vel encode vertical info for paddles

WIDTH = 600
HEIGHT = 400 

LEFT = False
RIGHT = True

BALL_RADIUS = 20
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

PAD_WIDTH = 8
HALF_PAD_WIDTH = PAD_WIDTH / 2

PAD_HEIGHT = 80
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

paddle1_pos = HEIGHT / 2
paddle1_vel = 0
score1 = 0

paddle2_pos = HEIGHT / 2
paddle2_vel = 0
score2 = 0

# Initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    
    global ball_pos, ball_vel 
    
    ball_pos[0] = WIDTH / 2
    ball_pos[1] = HEIGHT / 2
    
    if direction == RIGHT:
        ball_vel[0] = random.randrange(120, 240) / 60
        ball_vel[1] = -(random.randrange(60, 180)) / 60
        
    elif direction == LEFT:
        ball_vel[0] = -random.randrange(120, 240) / 60
        ball_vel[1] = -(random.randrange(60, 180)) / 60
    
# Define event handlers

def new_game():
    
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  
    global score1, score2  
    
    paddle1_pos = HEIGHT / 2
    paddle1_vel = 0
    score1 = 0
    
    paddle2_pos = HEIGHT / 2
    paddle2_vel = 0
    score2 = 0
    
    spawn_ball(True)

def draw(canvas):
    
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
     
    # Draw mid line and gutters
    
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # Update ball
    
    if (ball_pos[1] - BALL_RADIUS) <= 0:
        
        ball_vel[1] = -(ball_vel[1])
    
    elif (ball_pos[1] + BALL_RADIUS) >= HEIGHT:
    
        ball_vel[1] = -(ball_vel[1])
                
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # Draw ball
    
    canvas.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 12, 'White', 'White')
    
    # Update paddle's vertical position, keep paddle on the screen
    
    if (paddle1_pos + HALF_PAD_HEIGHT + paddle1_vel) <= HEIGHT and (paddle1_pos - HALF_PAD_HEIGHT + paddle1_vel) >= 0:
        
        paddle1_pos += paddle1_vel
    
    if (paddle2_pos + HALF_PAD_HEIGHT + paddle2_vel) <= HEIGHT and (paddle2_pos - HALF_PAD_HEIGHT + paddle2_vel) >= 0:
        
        paddle2_pos += paddle2_vel
    
    # Draw paddles
    
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT], [0,paddle1_pos + HALF_PAD_HEIGHT]], 16, 'White', 'White')
    canvas.draw_polygon([[WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], 16, 'White', 'White')
    
    # Determine whether paddle and ball collide    
    
    if (ball_pos[0] - BALL_RADIUS) <= PAD_WIDTH:
        
        if ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT):
            
            ball_vel[0] = -(ball_vel[0])
            ball_vel[0] += (ball_vel[0] * 0.1)
        
        else:
            score1 += 1
            spawn_ball(True)
        
    elif (ball_pos[0] + BALL_RADIUS) >= (WIDTH - PAD_WIDTH):
        
        if ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT):
            
            ball_vel[0] = -(ball_vel[0])
            ball_vel[0] += (ball_vel[0] * 0.1)
            
        else:	            
            score2 += 1
            spawn_ball(False)
 

    # Draw scores
    
    canvas.draw_text(str(score1), (WIDTH / 3, 70), 50, 'White')
    canvas.draw_text(str(score2), (WIDTH - 230, 70), 50, 'White')
        
def keydown(key):
    
    global paddle1_vel, paddle2_vel
    
        
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -5
        
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 5       
    
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -5
        
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5        
        
def keyup(key):
    
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
        
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
        
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0 

# Create frame

frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 120)

# Start frame

new_game()
frame.start()
