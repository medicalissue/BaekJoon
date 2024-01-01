import sys
import math

def input():
    return sys.stdin.readline()[:-1]

N, K = list(map(int, input().split()))
print(int(math.factorial(N) / (math.factorial(N - K) * math.factorial(K))))