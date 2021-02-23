"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

from time import sleep

def main():
    for countdown in range(10, 0, -1):
        print(countdown)
        sleep(1)
    print('Liftoff!')

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
