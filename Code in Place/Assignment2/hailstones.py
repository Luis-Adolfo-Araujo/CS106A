"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""

from time import sleep


def main():
    verify_number()


def verify_number():
    number = int(input('Enter a number: '))
    steps = 0

    while number != 1:
        steps += 1
        even = number % 2 == 0
        if even == True:
            half_even = number / 2
            print(f'{number} is even, so I take half: {half_even}')
            sleep(2)
            if half_even != 1:
                number = int(half_even)
            elif half_even == 1:
                break

        elif even == False:
            odd_expression = ((3 * number) + 1)
            print(f'{number} is odd, so I make 3n + 1: {odd_expression}')
            sleep(2)
            if odd_expression != 1:
                number = int(odd_expression)
            elif odd_expression == 1:
                break
    print(f'The process took {steps} steps to reach 1')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
