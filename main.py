def solution(n, t, m, timetable):
    table = []
    for time in timetable:
        hour = int(time[:2])
        minute = int(time[-2:])
        t = hour*100 + minute
        table.append(t)

    answer = ''
    print(table)
    return answer

solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])