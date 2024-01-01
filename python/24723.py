import sys

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
print(2 ** N)