label = input()
y = label.count('Y')
r = label.count('R')
if y + r == 5 or r >= 3 or (r >= 2 and y >= 2):
    print('nakhor lite')
else:
    print('rahat baash')
