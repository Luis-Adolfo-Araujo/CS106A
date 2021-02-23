"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so.
"""
from random import randint


def main():
    q = str(input('Ask a yes or no question: ')).strip()
    if q != "":
        print(responses())
    else:
        print('No questions found.')


def responses():

    r = randint(0, 5)

    if r == 0:
        return 'It is certain.'

    elif r == 1:
        return 'My answer is no.'

    elif r == 2:
        return 'My sources say no.'

    elif r == 3:
        return 'You may rely on it.'

    elif r == 4:
        return "Don't count on it"


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
