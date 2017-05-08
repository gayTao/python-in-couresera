# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global cards,exposed,state,previous_click,turn
    turn = 0
    state = 0
    previous_click = []
    cards = range(8)
    cards.extend(cards)
    random.shuffle(cards)
    exposed=[]
    i = 0
    while i < 16 :
        #value is invisible
        exposed.append(False) 
        i = i + 1
    
# define event handlers
def mouseclick(pos):
    global exposed,state,previous_click,turn
    position = list(pos)
    expose_change = position[0] / 50
    previous_click.append(expose_change)
    if len(previous_click) > 3 :
        previous_click.pop(0)
    if state == 0:
        state = 1
        exposed[expose_change] = True
    elif not exposed[expose_change] :        
        exposed[expose_change] = True
        if state == 1 :
            state = 2
            turn = turn + 1
        elif state == 2 and cards[previous_click[0]] != cards[previous_click[1]] :  
            exposed[previous_click[0]] = False
            exposed[previous_click[1]] = False
            state = 1
            
        elif state == 2 and cards[previous_click[0]] == cards[previous_click[1]] :  
            state = 1
            
    label.set_text("Turns = "+str(turn))
    
# cards are logically 50x100 pixels in size   
def draw(canvas):
    for card_index in range(len(cards)):
        card_pos = 50 * card_index
        canvas.draw_text(str(cards[card_index]), (card_pos,100), 100,'Red')
        if not exposed[card_index] :
                canvas.draw_polygon([(card_pos+25,0), (card_pos+25, 0),(card_pos+25,100),(card_pos+25, 100)],50, 'Green')

    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
