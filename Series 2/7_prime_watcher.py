# Filename:    7_prime_watcher.py
# Description: Solution to <Series 2 - Problem 7>
# Author:      Ali Mousavi <ali.mousavi@gmail.com>
# Instructor:  Mr. Ali Rezaee
# Date:        2018/11/11
from math import sqrt
start = int(input())
end = int(input())

primes = []
for num in range(start+1, end):
    primes.append(num)
    if num > 3:
        for idx in range(2, int(sqrt(num) + 1)):
            if not num % idx:
                primes.pop()
                break

print(','.join((str(p) for p in primes)))
