# Filename:    8_climbing_steps.py
# Description: Solution to <Series 2 - Problem 8>
# Author:      Ali Mousavi <ali.mousavi@gmail.com>
# Instructor:  Mr. Ali Rezaee
# Date:        2018/11/11

steps = int(input())


def count_all(remain):
    if remain < 0:
        return 0
    if remain == 0:
        return 1

    return (count_all(remain - 1) +
            count_all(remain - 2) +
            count_all(remain - 5))


print(count_all(steps))
