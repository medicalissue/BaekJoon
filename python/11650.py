import sys
input = sys.stdin.readline

N = int(input())
coord = list()
for i in range(N):
    coord.append(list(map(int, input().split())))
coord.sort()

for i in range(N):
    print(*coord[i])