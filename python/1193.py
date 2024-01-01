from copy import copy

loc = int(input())
n = copy(loc)
i = 1

while n > 0:
    n -= i
    i += 1

loc -= int(((i - 1) * (i - 2)) / 2)

if i % 2 == 0:
    print("{0}/{1}".format(str(i - loc), str(loc)))
else:
    print("{0}/{1}".format(str(loc), str(i - loc)))