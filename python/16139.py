import sys

def input():
    return sys.stdin.readline().rstrip()

def apb(ch):
    return ord(ch) - 97

S = input()
q = int(input())
stackedAscii = [[0 for j in range(26)] for i in range(len(S))]
stackedAscii[0][apb(S[0])] += 1
for i in range(1, len(S)):
    stackedAscii[i] = stackedAscii[i - 1].copy()
    stackedAscii[i][apb(S[i])] += 1

for _ in range(q):
    alpha, l, r = list(input().split())
    alpha = apb(alpha)
    l = int(l)
    r = int(r)

    if l != 0:
        print(stackedAscii[r][alpha] - stackedAscii[l - 1][alpha])
    else:
        print(stackedAscii[r][alpha])