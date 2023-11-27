H , M = input().split()

H = int(H)
M = int(M)

realMin = H * 60 + M
alarm = realMin - 45

if alarm < 0:
    alarm += 1440

alarmMin = alarm % 60
alarmHour = int((alarm - alarmMin) / 60)

print(alarmHour, alarmMin)