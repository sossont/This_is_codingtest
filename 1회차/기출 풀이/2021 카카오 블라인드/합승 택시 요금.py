# 30분 컷!

import heapq


def solution(n, s, a, b, fares):
    INF = 987654321
    graph = [[] for _ in range(201)]
    for fare in fares:
        c, d, f = fare
        graph[c].append((f, d))  # (c - d 양방향 그래프)
        graph[d].append((f, c))

    distances = [[]]
    # 다익스트라
    for start in range(1, n + 1):
        q = []
        heapq.heappush(q, [0, start])
        distance = [INF] * (n + 1)
        distance[start] = 0
        while q:
            cost, now = heapq.heappop(q)
            for adj in graph[now]:
                dist, nxt = adj
                if distance[nxt] > cost + dist:
                    distance[nxt] = cost + dist
                    heapq.heappush(q, [cost + dist, nxt])
        distances.append(distance)
    answer = INF

    for i in range(1, n + 1):
        hap = distances[s][i]
        a_cost = distances[i][a]
        b_cost = distances[i][b]
        total = hap + a_cost + b_cost
        answer = min(total, answer)

    return answer
