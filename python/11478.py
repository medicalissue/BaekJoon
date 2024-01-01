import sys
def input():
    return sys.stdin.readline()[:-1]

S = input()
diffStr = set()

for i in range(len(S)):
    for j in range(len(S) - i):
        diffStr.add(S[j:j + i + 1])
        
print(len(diffStr))