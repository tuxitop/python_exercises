nums = []
while True:
    nums.append(int(input()))
    if not nums[-1]:
        nums.pop()
        break

print(*nums[::-1], sep='\n')
