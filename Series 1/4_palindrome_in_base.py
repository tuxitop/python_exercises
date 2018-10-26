#! /usr/bin/python

# Filename:    4_palindrome_in_base.py
# Description: Solution to <Series 1 - Problem 4>
# Author:      Ali Mousavi <ali.mousavi@gmail.com>
# Instructor:  Mr. Ali Rezaee
# Date:        2018/10/23
import sys


def convert_bases(number, initial_base=10, converted_base=10):
    """Converts a number from the initial_base to any specified base

    number -- the number to convert
    base -- base of number
    converted_base --the base to convert the number to.

    returns string
    """
    # Check if everything is alright
    if (initial_base > 10 or initial_base < 2):
        raise ValueError("initial base should be between 2 and 10")
    if (converted_base > 10 or converted_base < 2):
        raise ValueError("Converted base should be between 2 and 10")
    if (number < 0):
        raise ValueError("Number should be a positive integer")

    # Convert to base 10
    base_10 = number
    if initial_base != 10:
        base_10 = 0
        for idx, digit in enumerate(str(number)[::-1]):
            # Check if the number is really in the specified base
            if (int(digit) >= initial_base):
                raise ValueError("The number is not in base " +
                                 str(initial_base))
            # convert the number
            base_10 += int(digit) * initial_base ** idx

    # Convert to the required base
    if converted_base == 10 or base_10 == 0:
        return str(base_10)

    reversed_converted_str = ""
    while base_10:
        reversed_converted_str += str(base_10 % converted_base)
        base_10 = int(base_10 / converted_base)
    return reversed_converted_str[::-1]


def check_for_palindrome(number):
    """Checks if the number is palindrome

    keyword arguments:
    number -- the string representation of the provided number

    Retruns: string
    """
    # The following statement will raise ValueError if the value is not a
    # positive number.
    if number == number[::-1]:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    # Try 3 times to recieve the required information.
    for idx in range(3):
        try:
            # number = input("Please enter a positive integer: ")
            # base = input("Please enter the base of the integer " +
            #              "(2 <= basae <= 10): ")
            # palindrome_base = input("Please enter the base in which you " +
            #                         "think the number is palindrome " +
            #                         " (2 <= base <= 10): ")
            number = input()
            base = input()
            palindrome_base = input()
            palindromic_number = convert_bases(int(number),
                                               int(base),
                                               int(palindrome_base))
            print(check_for_palindrome(palindromic_number))
        except ValueError as e:
            print("Error: " + str(e), file=sys.stderr)
        else:
            break
    else:
        print("Do you even know what a \"positive integer\" means?",
              file=sys.stderr)
        sys.exit(1)
