import sys

def input():
    return sys.stdin.readline().rstrip()

def recursion(s, l, r, calls):
    if l >= r:
        return 1, calls
    elif s[l] != s[r]:
        return 0, calls
    else:
        return recursion(s, l + 1, r - 1, calls + 1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 1)

T = int(input())

for _ in range(T):
    word = input()
    print(*isPalindrome(word))
