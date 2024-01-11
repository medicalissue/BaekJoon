from collections import deque

N = int(input())
numlist = list(map(int, input().split()))
S = int(input())
important = sorted(numlist, reverse = True)
stack = deque()

i = 0
while i < N:
    if important[i] in numlist and numlist.index(important[i]) <= S:
        S -= numlist.index(important[i])
        stack.append(numlist.pop(numlist.index(important[i])))
        i = -1
    i += 1

print(*(list(stack) + numlist))