import math
import sys

def input():
    return sys.stdin.readline()[:-1]

A, B = list(map(int, input().split()))

print(math.lcm(A, B))