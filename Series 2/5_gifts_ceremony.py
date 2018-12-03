# Filename:    5_gifts_ceremony.py
# Description: Solution to <Series 2 - Problem 5>
# Author:      Ali Mousavi <ali.mousavi@gmail.com>
# Instructor:  Mr. Ali Rezaee
# Date:        2018/11/11

guests = [input() for i in range(int(input()))]
# guests = ['dave', 'laura', 'owen', 'vick', 'amr']
incomes = [0 for i in guests]
# incomes = [0, 0, 0, 0, 0]

gifts = {}
for idx in guests:
    guest = input()
    amount, count = [int(n) for n in input().split()]
    gifts[guest] = (amount, [])
    for idx2 in range(count):
        gifts[guest][1].append(input())
# gifts = {
#     'dave': (200, ['laura', 'owen', 'vick']),
#     'owen': (500, ['dave']),
#     'amr': (150, ['vick', 'owen']),
#     'laura': (0, ['amr', 'vick']),
#     'vick': (0, [])
# }

for guest, gift in gifts.items():
    if len(gift[1]):
        incomes[guests.index(guest)] -= gift[0] - gift[0] % len(gift[1])
        for reciever in gift[1]:
            incomes[guests.index(reciever)] += gift[0] // len(gift[1])

print('\n'.join(['{} {}'.format(g, incomes[guests.index(g)]) for g in guests]))
