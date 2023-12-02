card = int(input())
howMany = int(input())
s = 0

for i in range(howMany):
    pr = list(map(int, input().split()))
    s += pr[0] * pr[1]

if s == card:
    print("Yes")
else:
    print("No")
    