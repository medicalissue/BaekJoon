import sys
import math

def input():
    return sys.stdin.readline()[:-1]

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

M, N = list(map(int, input().split()))
ans = set()

for i in range(M, N + 1):
    if isPrime(i):
        ans.add(i)

print(*sorted(list(ans)), sep = "\n")