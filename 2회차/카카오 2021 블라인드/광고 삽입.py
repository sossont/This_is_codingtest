def solution(play_time, adv_time, logs):
    max_hour = int(play_time[:2]) * 60 * 60
    max_min = int(play_time[3:5]) * 60
    max_sec = int(play_time[6:8])

    end_hour = int(adv_time[:2]) * 60 * 60
    end_min = int(adv_time[3:5]) * 60
    end_sec = int(adv_time[6:8])

    MAX_TIME = max_hour + max_min + max_sec
    END_TIME = end_hour + end_min + end_sec

    arr = [0] * (MAX_TIME+1)
    for log in logs:
        start_hour = int(log[:2]) * 60 * 60
        start_min = int(log[3:5]) * 60
        start_second = int(log[6:8])
        end_hour = int(log[9:11]) * 60 * 60
        end_min = int(log[12:14]) * 60
        end_second = int(log[15:])

        start_time = start_hour + start_min + start_second
        end_time = end_hour + end_min + end_second
        arr[start_time] += 1
        arr[end_time] -= 1

    for i in range(1,MAX_TIME+1):
        arr[i] += arr[i-1]

    for i in range(1, MAX_TIME+1):
        arr[i] += arr[i - 1]

    answer = 0
    answer_time = 0
    for i in range(MAX_TIME - END_TIME):
        people = arr[END_TIME + i] - arr[i]
        if people > answer:
            answer = people
            answer_time = i

    if answer_time == 0:
        answer = "00:00:00"
    else:
        answer_time += 1
        hour = answer_time // 3600
        minute = (answer_time - hour*3600) // 60
        second = answer_time - hour * 3600 - minute * 60

        string = ""
        if hour < 10:
            string += "0"
        string += str(hour) + ":"
        if minute < 10:
            string += "0"
        string += str(minute) + ":"
        if second < 10:
            string += "0"
        string += str(second)
        answer = string

    return answer