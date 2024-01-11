import datetime as dt


def timetosec(string):
    return int((dt.datetime.strptime(string, "%H:%M:%S") - dt.datetime(1900, 1, 1)).total_seconds())

def howmuchstacked(l1, l2):
    s1, e1 = l1
    s2, e2 = l2

    overlap_start = max(s1, s2)
    overlap_end = min(e1, e2)

    if overlap_start <= overlap_end:
        return overlap_end - overlap_start + 1
    else:
        return 0

N = int(input())
watchingTime = [[0, 0] for _ in range(N)]
for i in range(N):
    watchingTime[i] = list(map(timetosec, input().split(" - ")))
    if watchingTime[i][0] > watchingTime[i][1]:
        watchingTime[i][1] += int(dt.timedelta(days=1).total_seconds())
Q = int(input())

for _ in range(Q):
    targetTime = list(map(timetosec, input().split(" - ")))
    if targetTime[0] > targetTime[1]:
        targetTime[1] += int(dt.timedelta(days=1).total_seconds())
    cnt = 0
    for i in range(N):
        cnt += howmuchstacked(targetTime, watchingTime[i])
    print(cnt / (targetTime[1] - targetTime[0] + 1))
