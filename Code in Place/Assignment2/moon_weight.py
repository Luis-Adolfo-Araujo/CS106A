"""
File: moon_weight.py
--------------------
Calculates the Moonweight of an earthling based on its earth weight.
"""

# Pre = ask for the Earth weight
# Post = print the Moon weight
def main():
    weight = moon_weight(int(input('Enter a weight on earth: ')))
    print(f'{weight:.2f}')


# Takes the earth weight value and calculate the moon weight using the formula hereafter
def moon_weight(weight):
    weight = weight * (16.5 / 100)
    return weight


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
