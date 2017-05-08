import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PADDLE_LEN = 40
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0 / 60.0,  5.0 / 60.0]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2 
paddle1_vel = 0
paddle2_vel = 0

def spawn_ball(direction):
    global ball_pos, ball_vel 
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == "LEFT" :
        vel[0] = -random.randrange(120, 240)/60
    elif direction == "RIGHT" :
        vel[0] = random.randrange(120, 240)/60
    vel[1] = -random.randrange(60, 180)/60
    
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel 
    global score1, score2 
    score1 = 0
    score2 = 0
    spawn_ball("LEFT")
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
   
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
    if ball_pos[1] >= HEIGHT-BALL_RADIUS:
        vel[1] = - vel[1]              
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    if paddle1_pos < PADDLE_LEN :
        paddle1_pos =PADDLE_LEN
    elif paddle1_pos > HEIGHT-PADDLE_LEN :
        paddle1_pos = HEIGHT-PADDLE_LEN
    if paddle2_pos < PADDLE_LEN :
        paddle2_pos =PADDLE_LEN
    elif paddle2_pos > HEIGHT-PADDLE_LEN :
        paddle2_pos = HEIGHT-PADDLE_LEN
    # draw paddles
    canvas.draw_line([0, paddle1_pos-PADDLE_LEN],[0, paddle1_pos+PADDLE_LEN], 2*PAD_WIDTH, "White")
    canvas.draw_line([WIDTH , paddle2_pos-PADDLE_LEN],[WIDTH, paddle2_pos+PADDLE_LEN], 2*PAD_WIDTH, "White")
    # determine whether paddle and ball collide    
    if ball_pos[0] <= BALL_RADIUS :
        if ball_pos[1] >= paddle1_pos-PADDLE_LEN and ball_pos[1]<=paddle1_pos+PADDLE_LEN :
            vel[0] = - vel[0]
            vel[0] += vel[0]/10
        else :
            spawn_ball("RIGHT")
            score2 += 1
    if ball_pos[0] >= WIDTH-BALL_RADIUS :
        if ball_pos[1] >= paddle1_pos-PADDLE_LEN and ball_pos[1]<=paddle1_pos+PADDLE_LEN :
            vel[0] = - vel[0]
            vel[0] += vel[0]/10
        else :
            spawn_ball("LEFT")
            score1 += 1
    # draw scores
    canvas.draw_text(str(score1), (20, 40), 40, 'White')
    canvas.draw_text(str(score2), (360, 40), 40, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 4
    elif key ==  simplegui.KEY_MAP["up"] :
        paddle2_vel = -4
    if chr(key) == 'W' :
        paddle1_vel = -4
    elif chr(key) == 'S' :
        paddle1_vel = 4
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 60)

# start frame
new_game()
frame.start()
