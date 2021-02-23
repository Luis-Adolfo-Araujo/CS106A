from karel.stanfordkarel import *
'''This program should be able to make Karel climb a mountain and bring her down after that'''

def main():
    midpoint()

def midpoint():
    edges()
    decrease()

def edges():
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()

def decrease():
    if beepers_present():
        pick_beeper()
        turn_around()
        if front_is_clear():
            move()
            put_beeper()
            move()
            if no_beepers_present():
                put_beeper()
            move()
            decrease()
    else:
        while front_is_clear():
            if no_beepers_present():
                move()
            decrease()

def turn_around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
