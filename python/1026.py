N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
s = 0

for _ in range(N):
    smallA = min(A)
    largeB = max(B)
    s += smallA * largeB
    A.remove(smallA)
    B.remove(largeB)

print(s)