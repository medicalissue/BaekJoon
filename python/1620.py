import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
doGam = [""] * N
doGamDict = dict()
ans = [""] * M

for i in range(N):
    doGam[i] = input()[:-1]
    doGamDict[doGam[i]] = i + 1


for i in range(M):
    prob = input()[:-1]
    if prob.isdigit():
        ans[i] = doGam[int(prob) - 1]
    else:
        ans[i] = doGamDict[prob]

print(*ans)