stu = [i for i in range(1, 31)]

for _ in range(28):
    attendance = int(input())
    stu.remove(attendance)
    
print(min(stu))
print(max(stu))