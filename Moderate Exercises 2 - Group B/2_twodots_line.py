dims = [int(i) for i in input().split(' ')]
if (dims[1] == dims[3]):
    print('Horizontal')
elif (dims[0] == dims[2]):
    print('Vertical')
else:
    print('Try again')
