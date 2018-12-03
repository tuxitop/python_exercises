backseat = []
for i in range(4):
    name, pos = input().split(' ')
    if pos == 'R':
        backseat.append(name)
    elif pos == 'L':
        backseat.insert(0, name)
print(backseat[1])
