import heapq

def solution(n, s, a, b, fares):
    INF = float('inf')
    adj = [[] for _ in range(n + 1)]
    for start, end, fee in fares:
        adj[start].append((end, fee))
        adj[end].append((start, fee))

    distances = [[]]
    # 다익스트라
    for start in range(1, n + 1):
        q = []
        distance = [INF] * (n + 1)
        distance[start] = 0
        heapq.heappush(q, [0, start])
        while q:
            cost, now = heapq.heappop(q)
            for nxt, fee in adj[now]:
                if distance[nxt] > cost + fee:
                    distance[nxt] = cost + fee
                    heapq.heappush(q, [cost + fee, nxt])

        distances.append(distance)

    answer = INF
    for i in range(1, n + 1):
        co = distances[s][i]
        a_house = distances[i][a]
        b_house = distances[i][b]

        if answer > co + a_house + b_house:
            answer = co + a_house + b_house

    return answer

