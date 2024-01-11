import sys
sys.setrecursionlimit(100000)

T = int(input())
isThereBaeChu = list()

def deleteBaeChu(y, x, MaxY, MaxX):
    isThereBaeChu[y][x] = False
    if y != 0 and isThereBaeChu[y - 1][x]:
        deleteBaeChu(y - 1, x, MaxY, MaxX)
    if x != MaxX - 1 and isThereBaeChu[y][x + 1]:
        deleteBaeChu(y, x + 1, MaxY, MaxX)
    if y != MaxY - 1 and isThereBaeChu[y + 1][x]:
        deleteBaeChu(y + 1, x, MaxY, MaxX)
    if x != 0 and isThereBaeChu[y][x - 1]:
        deleteBaeChu(y, x - 1, MaxY, MaxX)


for _ in range(T):
    m, n, k = list(map(int, input().split()))
    isThereBaeChu = [[False for j in range(m)] for i in range(n)]
    howManyGroup = 0
    for _ in range(k):
        x, y = list(map(int, input().split()))
        isThereBaeChu[y][x] = True
    for i in range(n):
        for j in range(m):
            if isThereBaeChu[i][j]:
                howManyGroup += 1
                deleteBaeChu(i, j, n, m)
    del isThereBaeChu
    print(howManyGroup)
