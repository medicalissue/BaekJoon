import sys
input = sys.stdin.readline

N = int(input())
haveCard = set(map(int, input().split()))
M = int(input())
targetCard = list(map(int, input().split()))
ans = [0] * M

for i in range(M):
    if targetCard[i] in haveCard:
        ans[i] = 1

print(*ans)