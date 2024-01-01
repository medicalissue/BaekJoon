history = [-1] * 10
diff = 0

for i in range(10):
    mod = int(input()) % 42
    for j in range(10):
        if mod == history[j]:
            break
        else:
            if j == 9:
                history[i] = mod
                diff += 1
            else:
                continue

print(diff)
