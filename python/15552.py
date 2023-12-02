import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    pl = list(map(int, sys.stdin.readline().rstrip().split()))
    print(sum(pl))