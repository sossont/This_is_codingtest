def solution(fees, records):
    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    normal_time, normal_fee, plus_time, plus_fee = fees
    answer = []
    # 차량번호는 0000~9999이므로 차량번호당 입차, 출차 시간 기록
    arr = [[] for _ in range(10000)]
    car_list = []
    for rec in records:
        time, car_num, inout = rec.split(' ')
        minutes = int(time[0:2]) * 60 + int(time[3:5])
        if int(car_num) not in car_list:
            car_list.append(int(car_num))
        arr[int(car_num)].append(minutes)

    car_list.sort()
    for car in car_list:
        fee = normal_fee  # 기본 요금
        car_time = 0
        if len(arr[car]) % 2 == 1:  # 마지막에 입차하고 끝남
            last_in = arr[car].pop()
            max_time = 23 * 60 + 59
            car_time += max_time - last_in

        for idx in range(len(arr[car]) // 2):
            in_time = arr[car][2 * idx]
            out_time = arr[car][2 * idx + 1]
            car_time += (out_time - in_time)

        if car_time > normal_time:
            extra_time = (car_time - normal_time) / plus_time
            # 올림
            if extra_time > int(extra_time):
                extra_time = int(extra_time) + 1
            fee += extra_time * plus_fee
        answer.append(fee)

    return answer