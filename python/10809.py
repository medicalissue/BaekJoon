S = list(map(ord, input()))

alphabetList = [-1] * 26

for i in range(26):
    for j in range(len(S)):
        if 97 + i == S[j]:
            alphabetList[i] = j
            break

print(*alphabetList)