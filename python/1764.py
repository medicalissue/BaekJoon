import sys
def input():
    return sys.stdin.readline()[:-1]

N, M = list(map(int, input().split()))
noHear = [""] * N
noSee = [""] * M
for i in range(N):
    noHear[i] = input()
for i in range(M):
    noSee[i] = input()
noSee = set(noSee)
ans = ["*"] * N
for i in range(N):
    if noHear[i] in noSee:  
        ans[i] = noHear[i]

ans = sorted(list(set(ans)))[1:]
print(len(ans))
print(*ans, sep="\n")