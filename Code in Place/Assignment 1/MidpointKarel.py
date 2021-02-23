from karel.stanfordkarel import * 

'''program where Karel is supposed to paint the corner in the middle
of the street on the given maps (1x1, 2x2, 5x5, 8x8, 9x9)'''

def main():
    midpoint()

def midpoint():
    edges()
    decrease()
    paint()
    check()

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
            if no_beepers_present():
                put_beeper()
            move()
            decrease()
    else:
        while front_is_clear():
            if no_beepers_present():
                move()
            decrease()

def paint():
    if facing_east():
        move_back()
    else:
        if facing_west():
            turn_around()

    while front_is_clear():
        paint_corner(RED)
        move()
        paint_corner(BLUE)
        if front_is_clear():
            move()

def check():
    turn_around()
    paint_corner(BLANK)
    move()
    if corner_color_is(BLUE):
        odd()
    else:
        if corner_color_is(RED):
            even()

def odd():
    while front_is_clear():
        paint_corner(BLANK)
        move()
    paint_corner(BLANK)
    turn_around()
    while no_beepers_present():
        move()


def even():
    while front_is_clear():
        paint_corner(BLANK)
        move()
    paint_corner(BLANK)
    turn_around()
    while no_beepers_present():
        move()
    move()
    put_beeper()

def move_back():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def turn_around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
