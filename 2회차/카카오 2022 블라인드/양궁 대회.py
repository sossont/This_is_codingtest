score = 0  # 우승 점수
answer_arr = []  # 그 경우의 배열


def solution(n, info):
    global answer_arr
    arr = [0] * 11
    dfs(n, info, arr, 0)
    if len(answer_arr) == 0:
        return [-1]
    return answer_arr


# n : 남은 화살 개수, arr : 라이언 과녁 점수, idx : 현재 탐색 중인 원소 번호
def dfs(n, info, arr, idx):
    global score, answer_arr

    # 화살을 다 썼으므로 점수 계산
    if n == 0:
        apeach = 0
        ryan = 0
        for i in range(11):
            if info[i] == 0 and arr[i] == 0:
                continue

            if info[i] < arr[i]:
                ryan += (10 - i)
            else:
                apeach += (10 - i)
        if apeach >= ryan:
            return
        else:
            value = ryan - apeach
            if score < value:
                score = value
                answer_arr = arr
            elif score == value:
                for k in range(11):
                    if answer_arr[10 - k] == arr[10 - k]:
                        continue
                    elif answer_arr[10 - k] < arr[10 - k]:
                        answer_arr = arr
                        return
                    else:
                        return

    if idx == 11:
        return

    for shot in range(n + 1):
        copy_arr = arr[:]
        copy_arr[idx] = shot
        dfs(n - shot, info, copy_arr, idx + 1)