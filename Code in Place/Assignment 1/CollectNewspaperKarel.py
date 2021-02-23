from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

# Runs the program. Karel is supposed to go pick the newspaper up and go back home
def main():
    collect_newspaper()

#Makes Karel turn right
def turn_right():  
    for _ in range(3):
        turn_left()

# Makes Karel turn around
def turn_around():
    for _ in range(2):
        turn_left()

#Process to collect the newspaper
def collect_Newspaper():
    go_for_newspapper()
    go_back_home()

#Karel goes after the newspaper
def go_for_newspaper(): 
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()

# After get the newspaper picked up, Karel goes back home
def go_back_home():  
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
