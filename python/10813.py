N, M = list(map(int, input().split()))

box = [0] * N

for init in range(N):
    box[init] = init + 1

for rep in range(M):
    i, j = list( map(int, input().split()))
    box[i - 1], box[j - 1] = box[j - 1], box[i - 1]

print(*box)