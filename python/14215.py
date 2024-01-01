length = list(map(int, input().split()))

if sum(length) - max(length) <= max(length):
    print((sum(length) - max(length)) * 2 - 1)
else:
    print(sum(length))