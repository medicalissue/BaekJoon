import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
haveWord = set()
count = 0

for _ in range(N):
    haveWord.add(input())

for i in range(M):
    if input() in haveWord:
        count += 1

print(count)