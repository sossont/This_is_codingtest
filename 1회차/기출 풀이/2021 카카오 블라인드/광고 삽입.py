# 공식 해설 참고했음
# 초로 바꾸는 아이디어는 좋았는데
# 뒤에 아이디어는 정말...신박하다
def solution(play_time, adv_time, logs):
    logs.sort()
    time = play_time.split(':')
    int_play_time = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])

    time = adv_time.split(':')
    int_adv_time = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
    print(int_adv_time, int_play_time)
    plays = [0] * (int_play_time + 1)

    for log in logs:
        log = log.split('-')
        time1 = log[0].split(':')  # 시작시간
        time2 = log[1].split(':')  # 종료시간
        play1 = int(time1[0]) * 3600 + int(time1[1]) * 60 + int(time1[2])  # 시작시간을 초로 환산
        play2 = int(time2[0]) * 3600 + int(time2[1]) * 60 + int(time2[2])  # 종료시간을 초로 환산
        plays[play1] += 1
        plays[play2] -= 1

    max_play = 0
    play_time = 0

    # 구간 개수
    for i in range(1, int_play_time):
        plays[i] += plays[i - 1]

    # 누적합으로 변경
    for i in range(1, int_play_time):
        plays[i] += plays[i - 1]

    max_time = plays[int_adv_time - 1]
    max_i = 0

    for i in range(int_adv_time, int_play_time + 1):
        now_time = plays[i] - plays[i - int_adv_time]
        if max_time < now_time:
            max_time = now_time
            max_i = i + 1 - int_adv_time

    ## Seconds to HH:MM:SS
    hour = max_i // 3600
    max_i -= hour * 3600
    minute = max_i // 60
    max_i -= minute * 60
    second = max_i
    hour = str(hour)
    minute = str(minute)
    second = str(second)
    if len(hour) == 1:
        hour = "0" + hour

    if len(minute) == 1:
        minute = "0" + minute

    if len(second) == 1:
        second = "0" + second

    answer = hour + ":" + minute + ":" + second
    return answer


"""
def solution(play_time, adv_time, logs):
    logs.sort()
    time = play_time.split(':')
    int_play_time = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])

    time = adv_time.split(':')
    adv_time = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
    if (int_play_time == adv_time):
        return "00:00:00"
    plays = []
    for log in logs:
        log = log.split('-')
        time1 = log[0].split(':')
        time2 = log[1].split(':')
        play1 = int(time1[0]) * 3600 + int(time1[1]) * 60 + int(time1[2])
        play2 = int(time2[0]) * 3600 + int(time2[1]) * 60 + int(time2[2])
        plays.append([play1, play2])

    max_time = 0
    max_idx = -1

    for i in range(len(plays)):
        start_time = plays[i][0]  # 시작 시간 기준 잡기
        total = 0
        for play in plays:

            if play[0] < start_time:
                if play[1] <= start_time:  # case 1
                    continue

                # case 2
                if play[1] <= start_time + adv_time:
                    total += play[1] - start_time
                    continue

                # case 6
                if play[1] > start_time + adv_time:
                    total += adv_time
                    continue

            elif play[0] >= start_time:
                # case 5
                if play[0] >= start_time + adv_time:
                    continue

                    # case 3
                if play[1] < start_time + adv_time:
                    total += play[1] - play[0]
                    continue

                # case 4
                if play[1] >= start_time + adv_time:
                    total += start_time + adv_time - play[0]
                    continue
        if max_time < total:
            max_time = total
            max_idx = i

    tt = plays[max_idx][0]

    if tt + adv_time > int_play_time:
        tt = int_play_time - adv_time
    hour = int(tt / 3600)
    tt -= hour * 3600
    minute = int(tt / 60)
    tt -= minute * 60
    seconds = tt
    hour = str(hour)
    minute = str(minute)
    seconds = str(seconds)
    if len(str(hour)) == 1:
        hour = "0" + str(hour)

    if len(str(minute)) == 1:
        minute = "0" + str(minute)

    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)

    answer = hour + ":" + minute + ":" + seconds
    return answer
"""
