import sys
sys.setrecursionlimit(1000000)

N, M = list(map(int, input().split()))
map = [list() for _ in range(M)]
w = 0
b = 0

def dfs(x, y, wb):
    if x == -1 or x == N or y == -1 or y == M or map[y][x] != wb:
        return 0
    map[y][x] = "*"
    return 1 + dfs(x + 1, y, wb) + dfs(x, y + 1, wb) + dfs(x - 1, y, wb) + dfs(x, y - 1, wb)


for i in range(M):
    map[i] = list(input())

for y in range(M):
    for x in range(N):
        if map[y][x] == "*":
            continue
        elif map[y][x] == "W":
            w += pow(dfs(x, y, map[y][x]), 2)
        elif map[y][x] == "B":
            b += pow(dfs(x, y, map[y][x]), 2)

print(w, b)