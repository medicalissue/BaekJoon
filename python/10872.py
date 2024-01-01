import sys
import math

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
print(math.factorial(N))