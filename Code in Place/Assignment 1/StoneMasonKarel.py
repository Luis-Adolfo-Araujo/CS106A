from karel.stanfordkarel import *

"""
This program solve the problem of repairing columns of a building after a earthquake.
"""

def main():
    turn_left()
    fill_column()
    moving_east()
    fill_column2()
    moving_east()
    blocked_column()
    turn_left()
    fill_column()
    moving_east()
    fill_column2()


def fill_column():  # Fills the beepers column facing north
        while front_is_clear():
            interact_beepers()
        if front_is_blocked():
            interact_beepers()
            turn_around()


def turn_around():  # Makes Karel turn around
    turn_left()
    turn_left()
    turn_left()


def interact_beepers():  # determine Karel's interaction with beepers put beepers
    while front_is_clear():
        if no_beepers_present():  # put beepers if there aren't in the corner
            put_beeper()
            move()
        elif beepers_present():  # just move if there are beepers
            move()
    if front_is_blocked():
        if no_beepers_present():
            put_beeper()


def moving_east():  # Makes Karel move to the other columns
    x = facing_east()
    for x in range(4):
        move()


def fill_column2():  # Makes Karel fill up the columns while facing south
    fill_up_column()
    turn_around()
    while front_is_clear():
        interact_beepers()
    while front_is_blocked():
        interact_beepers()
        turn_left()


def fill_up_column():  # Makes karel fill the top side of the column if it reaches the column in the middle
    if left_is_clear():
        turn_left()
        fill_column()  # Makes Karel turn around and fill the column in the bottom


def blocked_column():  # Makes Karel put a beeper and move on if there is a column with one corner only
    if left_is_blocked() and right_is_blocked():
        put_beeper()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
