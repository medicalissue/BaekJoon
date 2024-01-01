a1, a2 = list(map(int, input().split()))
c = int(input())
n0 = int(input())

if c - a1 < 0:
    print("0")
elif a2 > (c - a1) * n0:
    print("0")
else:
    print("1")