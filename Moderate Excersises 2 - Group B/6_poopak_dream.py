a, b, x = (int(i) for i in input().split(' '))
count = 0
for i in range(1, x + 1):
    for j in range(1, x + 1):
        if (a % i == 0) and (b % j == 0) and (i + j <= x):
            count += 1

print(count)
