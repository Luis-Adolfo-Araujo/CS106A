from karel.stanfordkarel import *

'''This program should be able to make Karel climb a mountain and bring her down after that'''

# pre: KArel is facing east at the bottom of the mountain wishing to climb it
# post: Karel is facing east afte she climbed the mountain
def main():
    ascend_mountain()
    descend_mountain()

# Pre: Karel will be facing east with her front blocked by a wall
# Post: Karel will be at the top of the mountain with the flag established
def ascend_mountain():
    while front_is_blocked():
        climb_blocks()
    put_beeper()


# Pre: Karel will be supposed to climb the "rocks" one at a time
def climb_blocks():
    step_up()

# Pre: Karel will be at the top of the mountain with the flag established facing east
# Post: Karel will at the bottom of the mountain after climbed it facing east
def descend_mountain():
    while front_is_clear():
        if front_is_blocked():
            turn_left()
            break
        step_down()

# Makes Karel turn right
def turn_right():
    for _ in range(3):
        turn_left()

# Pre: Karel will be supposed step up the "rocks" one at a time
def step_up():
    turn_left()
    move()
    turn_right()
    move()

# Pre: Karel will be supposed step down the "rocks" one at a time
def step_down():
    move()
    turn_right()
    move()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
