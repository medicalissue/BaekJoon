N, M = list(map(int, input().split()))

box = [0] * N

for step in range(M):
    i, j, k = list(map(int, input().split()))
    for boxNum in range(j - i + 1):
        box[i + boxNum - 1] = k

print(*box)