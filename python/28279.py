import sys
from collections import deque

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
deck = deque()

for _ in range(N):
    todo = list(map(int, input().split()))
    if todo[0] == 1:
        deck.appendleft(todo[1])
    elif todo[0] == 2:
        deck.append(todo[1])
    elif todo[0] == 3:
        if deck:
            print(deck.popleft())
        else:
            print("-1")
    elif todo[0] == 4:
        if deck:
            print(deck.pop())
        else:
            print("-1")
    elif todo[0] == 5:
        print(len(deck))
    elif todo[0] == 6:
        if deck:
            print("0")
        else:
            print("1")
    elif todo[0] == 7:
        if deck:
            print(deck[0])
        else:
            print("-1")
    elif todo[0] == 8:
        if deck:
            print(deck[len(deck) - 1])
        else:
            print("-1")