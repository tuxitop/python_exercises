#! /usr/bin/python

# Filename:    1_number_printer.py
# Description: Solution to <Series 1 - Problem 1>
# Author:      Ali Mousavi <ali.mousavi@gmail.com>
# Instructor:  Mr. Ali Rezaee
# Date:        2018/10/21
import sys


def number_printer(digits):
    """Prints each digit of the input n times where n is the digit itself.

    Keyword arguments:
    digits -- The number to print its digits.
    """
    int(digits)   # This line will raise ValueError if digits is not an integer
    for digit in list(digits):
        print(digit + ": " + digit * int(digit))


if __name__ == '__main__':
    # Try 3 times to recieve a positive integer.
    for idx in range(3):
        try:
            # digits = input("Please enter a positive integer: ")
            digits = input()
            number_printer(digits)
        except ValueError:
            print("That is not a positive integer", file=sys.stderr)
        else:
            break
    else:
        print("Do you even know what a \"positive integer\" means?",
              file=sys.stderr)
        sys.exit(1)
