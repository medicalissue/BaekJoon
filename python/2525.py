H , M = input().split()
COOK = input()

H = int(H)
M = int(M)
COOK = int(COOK)

realMin = H * 60 + M
alarm = realMin + COOK

if alarm >= 1440:
    alarm -= 1440

alarmMin = alarm % 60
alarmHour = int((alarm - alarmMin) / 60)

print(alarmHour, alarmMin)