import math
import sys

def input():
    return sys.stdin.readline()[:-1]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = [math.lcm(a[1], b[1])] * 2
ans[0] = int((ans[1] / a[1]) * a[0] + (ans[1] / b[1]) * b[0])
ansGcd = math.gcd(ans[0], ans[1])
ans[0] = int(ans[0] / ansGcd)
ans[1] = int(ans[1] / ansGcd)

print(*ans)