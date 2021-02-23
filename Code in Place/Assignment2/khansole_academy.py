"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""


import random as r


def main():
    counting = 0
    while counting != 3:

        random1 = r.randint(10, 99)
        random2 = r.randint(10, 99)
        sum = random1 + random2

        print(f'What is {random1} + {random2}? ')
        answer = int(input('Your answer is: '))

        if answer == sum:
            counting += 1
            print(f"Correct! You've gotten {counting} correct roll!")
        else:
            print(f"Incorrect! The expected answer was {sum}!")
            counting = 0
    print('Congratulations! You mastered addition. ')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
