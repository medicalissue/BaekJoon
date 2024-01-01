import sys
from collections import deque

def input():
    return sys.stdin.readline()[:-1]

deck = deque()
N = int(input())

for _ in range(N):
    todo = input().split()
    if todo[0] == "push":
        deck.append(int(todo[1]))
    elif todo[0] == "pop":
        if deck:
            print(deck.popleft())
        else:
            print("-1")
    elif todo[0] == "size":
        print(len(deck))
    elif todo[0] == "empty":
        if deck:
            print("0")
        else:
            print("1")
    elif todo[0] == "front":
        if deck:
            print(deck[0])
        else:
            print("-1")
    elif todo[0] == "back":
        if deck:
            print(deck[len(deck) - 1])
        else:
            print("-1")