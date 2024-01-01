import sys
from collections import deque

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
deck = deque(range(1, N + 1))

while len(deck) != 1:
    deck.popleft()
    deck.append(deck.popleft())

print(deck[0])