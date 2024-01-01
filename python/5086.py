whatIsIt = list()

while True:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    elif b % a == 0:
        whatIsIt.append("factor")
    elif a % b == 0:
        whatIsIt.append("multiple")
    else:
        whatIsIt.append("neither")

print(*whatIsIt, sep = "\n")