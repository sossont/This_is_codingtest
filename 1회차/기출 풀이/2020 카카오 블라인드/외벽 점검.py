# 현재 84점 6,10,12,14 통과 못함

def solution(n, weak, dist):
    answer = 9
    weak_len = len(weak)

    for i in range(weak_len - 1):
        weak.append(weak[i] + n)

    dist.sort(reverse=True)
    cases = []  # 친구들이 선택되는 경우의 수들. 비트마스킹으로 모든 경우를 1과 0으로 파악.
    for i in range(1, len(dist) + 1):
        case = [1] * i
        cases.append(case)

    for case in cases:  # 케이스 별로 완전 탐색

        for next_idx in range(weak_len):  # 시작점을 0부터 n-1번까지로 둔다.
            count_weak = []  # 이거의 세트 길이랑 같으면 점검 완료

            for i in range(len(case)):
                distance = dist[i]  # 선정된 친구의 탐색 거리
                start = weak[next_idx]  # 탐색 시작 점

                for j in range(next_idx, len(weak)):  # 다음 녀석의 탐색 범위
                    cur = weak[j]
                    if start + distance < cur:  # 여기부터는 탐색 못하니 다음 놈에게 넘긴다.
                        next_idx = j
                        break
                    count_weak.append(cur)

            set_count = len(list(set(count_weak)))
            if set_count == weak_len:
                answer = min(answer, len(case))

    if answer == 9:
        return -1

    return answer


"""
반례 : 
n = 200
weak[] = [0, 10, 50, 80, 120, 160]
dist[] = [1, 10, 5, 40, 30]
return = 3

이런 반례는 어떻게 찾지..
"""

import sys

sys.setrecursionlimit(10000)


def solution(n, weak, dist):
    answer = 0
    original_weak = weak.copy()
    for i in range(len(weak) - 1):
        weak.append(weak[i] + n)
    dist.sort(reverse=True)

    # weak 지점 랜덤으로 선택해야 한다.
    # 어차피 큰 거리부터 배치하는게 맞으니까, 하나씩 팝하면서 weak idx 아무데나 배치하면 될듯!?
    distance = dist[0]  # 가장 큰 거리
    for i in range(len(original_weak)):
        check_list = []
        stop_idx = i
        while weak[stop_idx] <= weak[i] + distance:
            if (weak[stop_idx] - n) not in check_list and weak[stop_idx] + n not in check_list:
                check_list.append(weak[stop_idx])
            stop_idx += 1
            if stop_idx == len(weak):
                break
        check_list = set(check_list)
        if len(check_list) == len(original_weak):
            return 1
        answer = min(1000, recursion(n, dist, 1, weak, check_list.copy(), 1, len(original_weak)))
    return answer


def recursion(n, dist, dist_idx, weak, check_list, ans, weak_len):
    tmp_ans = 1000

    if dist_idx == len(dist):  # 못 끝냈음
        return 1000

    distance = dist[dist_idx]  # 이번에 잴 거리
    for i in range(weak_len):
        stop_idx = i
        copy_check = check_list.copy()
        while weak[stop_idx] <= weak[i] + distance:
            if (weak[stop_idx] - n) not in copy_check and weak[stop_idx] + n not in copy_check:
                copy_check.add(weak[stop_idx])
            stop_idx += 1

            if stop_idx == len(weak):
                break

        if len(copy_check) == weak_len:
            print(ans + 1)
            return ans + 1

        tmp_ans = min(n, tmp_ans, recursion(n, dist, dist_idx + 1, weak, copy_check, ans + 1, weak_len))

    return tmp_ans
