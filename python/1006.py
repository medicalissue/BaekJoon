import copy
import sys

sys.setrecursionlimit(1000000)

def input():
    return sys.stdin.readline().rstrip()


T = int(input())

def beside(loc, N):
    circle = [list(range(1, N + 1)), list(range(N + 1, N * 2 + 1))]
    if loc <= N:
        return list({circle[1][loc - 1], circle[0][loc % N], circle[0][loc - 2]})
    else:
        return list({circle[0][loc - 1 - N], circle[1][(loc - N) % N], circle[1][loc - N - 2]})

def checkpair(loc, circleEnemy, W, cnt):
    bes = beside(whereToCheck, N)
    if bes:
        for bs in bes:
            if circleEnemy[loc] + circleEnemy[bs] <= W and circleEnemy[bs] != 0:
                tmpList = copy.deepcopy(circleEnemy)
                tmpList[loc] = 0
                # print(tmpList[1:8])
                # print(tmpList[8:15])
                # print(cnt)
                return checkpair(bs, tmpList, W, cnt + 1)
        return cnt
    else:
        return cnt


for _ in range(T):
    N, W = list(map(int, input().split()))
    circleEnemy = [0]
    for _ in range(2):
        circleEnemy += list(map(int, input().split()))
    for i in range(N * 2):
        if len(set(circleEnemy)) == 1:
            print(i)
            break
        whereToCheck = circleEnemy.index(max(circleEnemy))
        leftSoldiers = W - circleEnemy[whereToCheck]
        # print(circleEnemy[whereToCheck])
        circleEnemy[whereToCheck] = 0
        nextLoc = list()
        for bs in beside(whereToCheck, N):
            if circleEnemy[bs] == 0 or circleEnemy[bs] > leftSoldiers:
                continue
            else:
                nextLoc.append(bs)

        # print(i)
        # print(circleEnemy[1:8])
        # print(circleEnemy[8:15])
        for nl in nextLoc:
            if checkpair(nl, circleEnemy, W, 1) % 2 == 0:
                circleEnemy[nl] = 0
                break

        # print(i)
        # # print(circleEnemy[1:8])
        # # print(circleEnemy[8:15])
