def solution(n, t, m, timetable):
    crews = []
    for time in timetable:
        hour = int(time[:2])
        minute = int(time[3:])
        crews.append(hour * 60 + minute)

    answer = 0
    crews.sort()
    on = []
    bus_start = 60 * 9  # 09:00 버스 출발
    for _ in range(n):
        count = 0
        for idx in range(len(on), len(crews)):
            if crews[idx] <= bus_start:
                count += 1
                on.append(crews[idx])

            if count == m:
                break

        if count != m:
            answer = bus_start
        bus_start += t  # 다음 버스가 나온다

    if len(on) == 0:
        answer = max(answer, bus_start - t)
    else:
        answer = max(answer, on[-1] - 1)

    hour = str(answer // 60)
    minute = str(answer - int(hour) * 60)

    if len(hour) == 1:
        hour = "0" + hour

    if len(minute) == 1:
        minute = "0" + minute

    ans = hour + ":" + minute
    return ans