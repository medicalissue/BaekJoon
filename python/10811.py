N, M = list(map(int, input().split()))

box = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = list(map(int, input().split()))
    i -= 1
    j -= 1
    all = i + j
    tempBox = list(box)
    for k in range(j - i + 1):
        box[all - i - k] = tempBox[all - j + k]

print(*box)