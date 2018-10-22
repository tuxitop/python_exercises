#! /usr/bin/python

# Filename:    2_powers_of_two.py
# Description: Solution to <Series 1 - Problem 2>
# Author:      Ali Mousavi <ali.mousavi@gmail.com>
# Instructor:  Mr. Ali Rezaee
# Date:        2018/10/22
import sys


def powers_of_two(number):
    """Returns the nearest power of two, greater than <number>

    keyword arguments:
    number -- the provided number

    Retruns: number
    """
    # The following line will raise ValueError if the value is not a number.
    number = int(number)
    power = 0
    while True:
        if 2 ** power > number:
            return 2 ** power
        power += 1


if __name__ == '__main__':
    # Try 3 times to recieve an integer.
    for idx in range(3):
        try:
            number = input("Please enter an integer: ")
            print(powers_of_two(number))
        except ValueError:
            print("That is not an integer.")
        else:
            break
    else:
        print("Do you even know what an \"integer\" means?")
        sys.exit(1)
