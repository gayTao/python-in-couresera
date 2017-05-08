import simplegui
import random

# Global state
state="stop"
position = [50, 50]
width = 500
height = 500
interval = 100
time = 0
successful_stops = 0
total_stops = 0

#helper function
def format(t):
    D = t%10
    C = (t%100 - D)/10
    E = t/100
    if E <= 5:
        B = E
        A = 0
    else:
        B=E%6
        A=E/6
    return str(A)+":" +str(B)+str(C)+"."+str(D)

# Handler for timer
def tick():
    global time
    if state == "start" :
        time = time + 1
    elif state == "reset" :
        time = 0


# Handler to draw on canvas
def draw_handler(canvas):
    canvas.draw_text(format(time), position, 36, "Red")
    canvas.draw_text(str(total_stops), [5,20], 10, "Red")
    canvas.draw_text(str(successful_stops), [5,30], 10, "Red")
    
def start_button_handler():
    global state
    state="start"

def stop_button_handler():
    global state,total_stops,successful_stops
    state="stop"    
    total_stops=total_stops+1
    if time%10 == 0 :
        successful_stops = successful_stops + 1
    
def reset_button_handler():
    global state,successful_stops,total_stops
    state="reset"
    successful_stops = 0
    total_stops = 0
    
# Create a frame 
frame = simplegui.create_frame("Stopwatch", width, height)

# Register event handlers
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_button_handler)
frame.add_button("Stop", stop_button_handler)
frame.add_button("Reset", reset_button_handler)

# Start the frame animation
frame.start()
timer.start()
###################################################
# Test code for the format function
# Note that function should always return a string with 
# six characters


print format(0)
print format(7)
print format(17)
print format(60)
print format(63)
print format(214)
print format(599)
print format(600)
print format(602)
print format(667)
print format(1325)
print format(4567)
print format(5999)

###################################################
# Output from test

#0:00.0
#0:00.7
#0:01.7
#0:06.0
#0:06.3
#0:21.4
#0:59.9
#1:00.0
#1:00.2
#1:06.7
#2:12.5
#7:36.7
#9:59.9

