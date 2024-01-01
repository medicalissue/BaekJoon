import sys
input = sys.stdin.readline

n = int(input())
memberState = dict()

for _ in range(n):
    name, EntOrLv = input().split()
    if EntOrLv == "enter":
        memberState[name] = True
    else:
        memberState[name] = False

ans = [k for k, v in memberState.items() if v]
ans.sort(reverse = True)
print(*ans)