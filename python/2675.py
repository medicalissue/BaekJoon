T = int(input())

ans = ""
for i in range(T):
    rep, word = input().split()
    rep = int(rep)
    for j in range(len(word)):
        for k in range(rep):
            ans += word[j]
    ans += " "

for i in range(T):
    print(ans.split(" ")[i])