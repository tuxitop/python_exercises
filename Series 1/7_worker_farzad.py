#! /usr/bin/python

# Filename:    7_worker_farzad.py
# Description: Solution to <Series 1 - Problem 7>
# Author:      Ali Mousavi <ali.mousavi@gmail.com>
# Instructor:  Mr. Ali Rezaee
# Date:        2018/10/26
import sys


def calculate_maximum_sum(target_list):
    """Takes a list and returns the largest sum of its subarrays

    Keyword arguments:
    target_list -- the list to check its subarrays

    returns an integer
    """
    subarrays = []
    for length in range(1, len(target_list) + 1):
        for idx in range(len(target_list) + 1 - length):
            subarrays.append(target_list[idx:idx + length])

    maximum_sum = float("-inf")  # assign -infinity to maximum
    for subarray in subarrays:
        sum = 0
        for elem in subarray:
            sum += elem

        if sum > maximum_sum:
            maximum_sum = sum

    return maximum_sum


def input_list_of_numbers():
    """Takes data from the user and returns a list of numbers

    returns a list of numbers.
    """
    # try 3 times to get the length of the list from the users
    for idx in range(3):
        try:
            # length = int(input(
            #     "Please enter the length of the list: ")
            # )
            length = int(input())
            if length <= 0:
                raise ValueError
        except ValueError:
            print('You need to provide a positive integer.',
                  file=sys.stderr)
        else:
            break
    else:
        print('You did not enter a valid length.', file=sys.stderr)
        raise ValueError

    # try 3 times to get the list values from the users
    for idx in range(3):
        try:
            # list_str = input(
            #     "Please enter the elements (seperate with space): "
            # )
            list_str = input()
            result = [int(elem) for elem in list_str.split()]
            if len(result) != length:
                print("Size of the entered list didn't match the length.",
                      file=sys.stderr)
                raise ValueError
        except ValueError:
            print('You did not enter valid values,', file=sys.stderr)
        else:
            break
    else:
        print("You seem not to be able to provide valid values for the list.")
        raise ValueError

    return result


if __name__ == '__main__':
    try:
        profits_each_day = input_list_of_numbers()
    except ValueError:
        sys.exit(1)

    maximum_profit = calculate_maximum_sum(profits_each_day)
    if (maximum_profit > 0):
        print(maximum_profit)
    else:
        print(0)
