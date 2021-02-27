#개선된 다익스트라 알고리즘

import heapq
import sys

input = sys.stdin.readline()
INF = int(1e9)

n, m = map(int,input().split())
start = int(input())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 큐에 추가하는 것 : (거리, 노드)
    heapq.heappush(q,(0,start))
    distance[start] = 0

    # 큐가 빌 때까지 반복.
    while q:
        dist, now = heapq.heappop()

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])