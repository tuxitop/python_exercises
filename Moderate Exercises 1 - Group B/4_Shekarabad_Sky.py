count = 0
for i in range(int(input().split()[0])):
    count += input().count('*')

print(count)
