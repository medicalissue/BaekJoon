class strangeWord():
    firstWord = str()
    lastWord = str()
    wordDict = dict()
    wordLen = int()

    def __init__(self):
        self.firstWord = str()
        self.lastWord = str()
        self.wordDict = dict()
        self.wordLen = int()

    def initsetting(self, string):
        word = list(string)
        self.wordLen = len(word)
        if len(word) == 1:
            self.firstWord = word[0]
            self.lastWord = word.pop()
        else:
            self.firstWord = word.pop(0)
            self.lastWord = word.pop()
        for _ in range(len(word)):
            temp = word.pop()
            if temp in self.wordDict:
                self.wordDict[temp] += 1
            else:
                self.wordDict[temp] = 1

    def getfirstword(self):
        return self.firstWord

    def getlastword(self):
        return self.lastWord

    def getdict(self):
        return self.wordDict

    def getlen(self):
        return self.wordLen

N = int(input())
dictionary = [strangeWord() for _ in range(N)]
for i in range(N):
    dictionary[i].initsetting(input())

M = int(input())
for _ in range(M):
    target = input().split()
    ans = 1
    for i in range(len(target)):
        cnt = 0
        targetWord = strangeWord()
        targetWord.initsetting(target[i])
        for i in range(N):
            if targetWord.getfirstword() == dictionary[i].getfirstword() and targetWord.getlastword() == dictionary[i].getlastword() and targetWord.getdict() == dictionary[i].getdict() and targetWord.getlen() == dictionary[i].getlen():
                cnt += 1
        ans *= cnt
    print(ans)