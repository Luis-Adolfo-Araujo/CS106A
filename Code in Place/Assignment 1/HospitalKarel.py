from karel.stanfordkarel import *


"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""


'''a program to implement 3 Hospitals Building around a pile of supplies '''
def main():  # Makes Karel build 3 hospitals to help in critical times
    for _ in range(3):
        build_hospital()


def subida():  #  Karel builds up the hospital's 1st wall
    if beepers_present():
        turn_left()
        move()
        put_beeper()
        move()
        put_beeper()
        turn_right()


def descida():  # Karel builds the hospital's 2nd wall
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_left()


def turn_right():  # makes Karel turn right
    for _ in range(3):
        turn_left()


def build_hospital():  # simply build the hospitals, one at a time
    while front_is_clear():
        while no_beepers_present():
            move()
        subida()
        move()
        descida()
        if front_is_clear():
            move()


# There is no need to edit code beyond this point
if _name_ == "_main_":
    run_karel_program()
