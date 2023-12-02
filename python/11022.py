import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    ans = "Case #" + str(i + 1) + ": "
    pl = list(map(int, sys.stdin.readline().rstrip().split()))
    ans += str(pl[0]) + " + " + str(pl[1]) + " = " + str(sum(pl))
    print(ans)
