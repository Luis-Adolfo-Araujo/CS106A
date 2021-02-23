"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    stones = 20
    while stones > -1:
        for player in range(1, 3):
            if stones == 0:
                print(f'Player {player} wins!')
                stones -= 1
                break
            print(f'There are {stones} stones left.')
            answer = int(input(f'Player {player} would you like to remove 1 or 2 stones?'))
            while answer > 2:
                answer = int(input('Enter 1 or 2: '))
            while answer < 1:
                answer = int(input('Enter 1 or 2: '))
            if stones == 1:
                while answer != 1:
                    answer = int(input('2 is not available : '))
            stones -= answer
        if stones == -1:
            break






# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
