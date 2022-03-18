## 당연히 시간초과 날것
# 이 코드는 5분컷,, 시간 초과 어떻게 해결할까?

def solution(food_times, k):
    time = 0
    idx = 0
    answer = 0
    dic = {}
    while True:
        if idx == len(food_times):  # 끝에 도달
            idx = 0
            continue

        if food_times[idx] == 0:
            if len(dic) == len(food_times):
                return -1
            idx += 1
            dic[idx] = 1
            continue

        if time == k:
            answer = idx + 1
            break

        food_times[idx] -= 1
        time += 1
        idx += 1

    return answer