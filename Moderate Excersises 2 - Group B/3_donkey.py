a, b, l = (int(i) for i in input().split(' '))
seconds = 0
turn_a = 1
while (l):
    if turn_a:
        seconds += a
        turn_a = 0
    else:
        seconds += b
        turn_a = 1
    l -= 1
print(seconds)
