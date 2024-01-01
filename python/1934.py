import math
import sys

def input():
    return sys.stdin.readline()[:-1]

testCase = int(input())
ans = [0] * testCase
for i in range(testCase):
    a, b = list(map(int, input().split()))
    ans[i] = math.lcm(a, b)

print(*ans, sep = "\n")