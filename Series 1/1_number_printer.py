#! /usr/bin/python

# Filename:    1_number_printer.py
# Description: Solution to <Series 1 - Problem 1>
# Author:      Ali Mousavi <ali.mousavi@gmail.com>
# Instructor:  Mr. Ali Rezaee
# Date:        2018/10/21


def number_printer(digits):
    """Prints each digit of the input n times where n is the digit itself.

    Keyword arguments:
    digits -- The number to print its digits.
    """
    for digit in list(digits):
        print(digit + ": " + digit * int(digit))


if __name__ == '__main__':
    digits = None
    while not digits:
        digits = input("Please enter an integer: ")
        # Checking if the provided value is an integer and not just a string.
        try:
            int(digits)
            number_printer(digits)
        except ValueError:
            print("That is not an integer")
            digits = None
