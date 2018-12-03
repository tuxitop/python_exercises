(n, x, k) = map(int, input().split())
channels = []
for i in range(n):
    channels.append(input())
print(channels[((x + k - 1) % n)])
