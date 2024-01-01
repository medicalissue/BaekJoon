import sys
input = sys.stdin.readline

N = int(input())
member = list()
for _ in range(N):
    age, name = input().split()
    age = int(age)
    member.append([age, name])
member.sort(key=lambda x:x[0])

for i in range(N):
    print(member[i][0], member[i][1])