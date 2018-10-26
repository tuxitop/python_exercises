#! /usr/bin/python

# Filename:    5_movie_watcher_farzad.py
# Description: Solution to <Series 1 - Problem 5>
# Author:      Ali Mousavi <ali.mousavi@gmail.com>
# Instructor:  Mr. Ali Rezaee
# Date:        2018/10/24
import sys


def titlecase_list(titles):
    """ takes a list of strings and returns a list with all the strings
        titlecased.

    Keyword arguments:
    titles -- a list of strings

    returns a list
    """
    return [title.title() for title in titles]


def input_movies_list():
    """ takes the names of movie titles from user.

    returns None or list
    """
    # try 3 times to get a valid number
    for idx in range(3):
        try:
            # count = int(input("How many movie names do you want to provide? "))
            count = int(input())
            if count <= 0:
                raise ValueError
        except ValueError:
            print("You have to enter a \"positive integer\"", file=sys.stderr)
        else:
            break
    else:
        print("You failed to enter a positive integer", file=sys.stderr)
        return None
    # SUFFIXES = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']
    movie_titles = []
    idx = 1
    while idx <= count:
        # name = input(
        #     'Enter the {0}{1} title: '.format(idx, SUFFIXES[idx % 10])
        # )
        name = input()
        movie_titles.append(name)
        if name:
            idx += 1
    return movie_titles


if __name__ == '__main__':
    titles = input_movies_list()
    if not titles:
        sys.exit(1)
    titlecase_titles = titlecase_list(titles)
    for title in titlecase_titles:
        print(title)
