a, b, c = (int(i) for i in input().split(' '))
if a and b and c and a + b + c == 180:
    print('Yes')
else:
    print('No')
