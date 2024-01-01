import sys
def input():
    return sys.stdin.readline()[:-1]
input()
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A - B) + len(B - A))