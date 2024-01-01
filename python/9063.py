import sys

input = sys.stdin.readline

N = int(input())
up = 0
down = 0
left = 0
right = 0
for i in range(N):
    x, y = list(map(int, input().split()))
    if i == 0:
        up = y
        down = y
        left = x
        right = x
        continue
    up = max(up, y)
    down = min(down, y)
    left = min(left , x)
    right = max(right, x)

print((up - down) * (right - left))