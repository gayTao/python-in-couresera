import simplegui
import random

rangeflag = 0
times = 7

def new_game():
    global secret_number,rangeflag,times
    rangeflag=int(rangeflag)
    if rangeflag == 0:
        secret_number=random.randrange(0,100)
        times = 7
        print "New Game,the rangle of input is 0~100,the remaining times of guess is 7"
    else:
        secret_number=random.randrange(0,1000)
        times = 10
        print "New Game,the rangle of input is 0~1000,the remaining times of guess is 10"

def range100():
    global rangeflag
    rangeflag = 0
    new_game()
    
def range1000():
    global rangeflag
    rangeflag = 1
    new_game()
    
def input_guess(guess):
    global times
    guess=int(guess)
    times = times-1
    if times == 0 :
        if secret_number != guess :
            print "Sorry,you've run out of times,the real number is ",secret_number
            new_game()
            return
    print "Guess was",guess
    print "the remaining times of guess is ",times
    if secret_number > guess :
        print "Higher"
    elif secret_number < guess :
        print "Lower"
    else :
        print "Correct"
        new_game()

frame = simplegui.create_frame("Guess the number", 300, 200)
frame.add_button("Range is [0,1000)", range1000)
frame.add_button("Range is [0,100)", range100)
frame.add_input("input your guess", input_guess, 100)
frame.start()
new_game()

