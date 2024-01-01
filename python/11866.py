import sys
from collections import deque

def input():
    return sys.stdin.readline()[:-1]

N, K = list(map(int, input().split()))
circle = list(range(1, N + 1))
JosepList = list()

while True:
    JosepList.append(circle.pop((K % len(circle)) - 1))
    if len(circle) == 0:
        break
    for _ in range((K % (len(circle) + 1)) - 1):
        circle = deque(circle)
        circle.append(circle.popleft())
    circle = list(circle)

print("<" + str(JosepList)[1:-1] + ">")