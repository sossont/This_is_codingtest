import math

# 주차요금 계산 함수
def calculate(fees, min):
    # 기본 요금만 나오는 경우
    if fees[0] >= min:
        return fees[1]
    else:
        over_time = min - fees[0]
        return fees[1] + fees[3] * math.ceil(over_time / fees[2])

def solution(fees, records):
    dic = {}
    cars = []
    for record in records:
        time, num, state = record.split(' ')
        hour = int(time[:2])
        min = int(time[3:])
        t = 60 * hour + min
        num = int(num)
        if num not in dic:
            cars.append(num)
            dic[num] = [t]
        else:
            dic[num].append(t)

    answer = []
    cars.sort()
    for num in cars:
        total_time = 0
        if len(dic[num]) % 2 == 1:
            dic[num].append(23 * 60 + 59)
        for idx in range(len(dic[num]) // 2):
            total_time += (dic[num][2*idx+1] - dic[num][2*idx])

        answer.append(calculate(fees, total_time))
    return answer