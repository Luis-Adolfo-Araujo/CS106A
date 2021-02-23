from karel.stanfordkarel import *


"""
This program Makes Karel jump some walls while she put beepers around it
"""

# Runs the whole code
def main():  
    run_prog()

# Function to work while Karel is going to jump a wall
def subida():  
    turn_left()
    while facing_north():
        while right_is_blocked():
            interact_beeper()
            move()
        interact_beeper()
        turn_right()
        move()
        interact_beeper()
        turn_right()

# Function to work while karel is going down to the 1st street
def descida():  
    while front_is_clear():
        interact_beeper()
        move()
        if front_is_blocked():
            interact_beeper()
            turn_left()
            break

# Function to put beepers in case there aren't in the indicated corner
def interact_beeper():
    if no_beepers_present():
        put_beeper()

# Function to make karel turns right
def turn_right():  
    for _ in range(3):
        turn_left()

# This function makes karel move one corner while it is in between wall separated by a corner
def east():  
    while facing_east() and front_is_clear():
        move()


def run_prog():
    for _ in range(5):
        subida()
        descida()
        east()
    subida()
    descida()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
