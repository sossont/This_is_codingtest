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

