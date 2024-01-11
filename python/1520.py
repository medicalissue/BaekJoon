import sys
sys.setrecursionlimit(1000000)

def input():
    return sys.stdin.readline().rstrip()

M, N = list(map(int, input().split()))
stairmap = [[0 for _ in range(N)] for _ in range(M)]
checkVisited = [[False for _ in range(N)] for _ in range(M)]
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
cnt = 0

def dfs(x, y):
    if x == N - 1 and y == M - 1:
        global cnt
        cnt += 1
        return
    checkVisited[y][x] = True
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if N > new_x >= 0 and M > new_y >= 0 and checkVisited[new_y][new_x] == False and stairmap[new_y][new_x] < stairmap[y][x]:
            dfs(new_x, new_y)
            checkVisited[new_y][new_x] = False

for i in range(M):
    stairmap[i] = list(map(int, input().split()))

dfs(0, 0)

print(cnt)