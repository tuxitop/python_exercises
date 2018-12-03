caps = False
output = ''
for i in range(int(input())):
    key = input()
    if key == 'CAPS':
        caps = ~caps
    elif caps:
        output += key.upper()
    else:
        output += key
print(output)
