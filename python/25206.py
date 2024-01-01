majorPointDic = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0":	3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
multiSum = 0
hakJeomSum = 0

while True:
    try:
        allInform = input().split()
        if allInform[2] == "P":
            continue
        majorCredit = float(allInform[1])
        engToFloatGrade = majorPointDic[allInform[2]]
        multiSum += majorCredit * engToFloatGrade
        hakJeomSum += majorCredit
    except:
        break

print(multiSum / hakJeomSum)