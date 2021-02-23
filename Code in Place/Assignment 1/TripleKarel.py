from karel.stanfordkarel import *

"""
Program to make Karel paint 3 building's walls
"""
def main(): # Runs the program
    paint_block_1()  # Karel paints the block 1
    paint_block_2_3()  # Karel paints the block 2 and 3

def turn_right():  # Makes Karel turn Right
    for _ in range(3):
        turn_left()

def paint():  # Makes Karel paint the walls
    while left_is_blocked():
        paint_corner(ORANGE)
        move()

def paint_to_left():  # Makes Kares paint the walls after turn left
    for _ in range(2):
        turn_left()
        move()
        paint()

def paint_block_1():  # Makes Karel paint the whole block 1
    for _ in range(2):
        paint()
        turn_left()
        move()
    paint()

def paint_block_2_3():  # Makes Karel paint the whole block 2 and 3
    for _ in range(2):
        turn_right()
        paint()
        paint_to_left()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
