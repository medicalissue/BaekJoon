import sys

def input():
    return sys.stdin.readline()[:-1]

N = int(int(input()))
rainbowDance = {"ChongChong"}

for i in range(N):
    a, b = input().split()
    if a in rainbowDance or b in rainbowDance:
        rainbowDance.add(a)
        rainbowDance.add(b)

print(len(rainbowDance))