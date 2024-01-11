import sys
import copy
sys.setrecursionlimit(1000000)

N, M = list(map(int, input().split()))
edges = [dict() for _ in range(N + 1)]
copiedEdges = list()
priceList = list()
def dfs(now, togo):
    global priceList, copiedEdges
    if now == togo:
        return True
    possibleRoad = list(copiedEdges[now].keys())
    for i in range(len(possibleRoad)):
        priceList.append(copiedEdges[now][possibleRoad[i]])
        del copiedEdges[now][possibleRoad[i]]
        del copiedEdges[possibleRoad[i]][now]
        if dfs(possibleRoad[i], togo):
            return True
        else:
            priceList.pop()

for _ in range(N - 1):
    start, end, price = list(map(int, input().split()))
    edges[start][end] = price
    edges[end][start] = price

for _ in range(M):
    start, end = list(map(int, input().split()))
    priceList = list()
    copiedEdges = copy.deepcopy(edges)
    dfs(start, end)
    print(sum(priceList))