"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random as r


def main():
    for _ in range(0, 10):
        print(r.randint(0, 100))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
