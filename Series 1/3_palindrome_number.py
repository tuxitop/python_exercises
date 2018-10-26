#! /usr/bin/python

# Filename:    2_palindrome_number.py
# Description: Solution to <Series 1 - Problem 3>
# Author:      Ali Mousavi <ali.mousavi@gmail.com>
# Instructor:  Mr. Ali Rezaee
# Date:        2018/10/22
import sys


def check_for_palindrome_number(number):
    """Checks if the number is palindrome

    keyword arguments:
    number -- the string representation of the number

    Retruns: string
    """
    # The following statement will raise ValueError if the value is not a
    # positive number.
    if int(number) < 0:
        raise ValueError
    if number == number[::-1]:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    # Try 3 times to recieve an integer.
    for idx in range(3):
        try:
            # number = input("Please enter a positive integer: ")
            number = input()
            print(check_for_palindrome_number(number))
        except ValueError:
            print("That is not a positive integer.", file=sys.stderr)
        else:
            break
    else:
        print("Do you even know what a positive \"integer\" means?",
              file=sys.stderr)
        sys.exit(1)
