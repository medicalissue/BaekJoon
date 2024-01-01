T = int(input())

ans = [""] * T

for i in range(T):
    voca = input()
    ans[i] += voca[0]
    ans[i] += voca[len(voca) - 1]

for i in range(T):
    print(ans[i])