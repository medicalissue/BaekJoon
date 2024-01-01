import sys
import math

def input():
    return sys.stdin.readline()[:-1]

T = int(input())
ans = list()

for _ in range(T):
    n, m = list(map(int, input().split()))
    ans.append(int(math.factorial(m) / (math.factorial(m - n) * math.factorial(n))))

print(*ans, sep = "\n")