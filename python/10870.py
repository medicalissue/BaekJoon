import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lastFibo = 0
curFibo = 1

for _ in range(N - 1):
    curFibo , lastFibo = lastFibo + curFibo, curFibo

if N == 0:
    print(0)
else:
    print(curFibo)