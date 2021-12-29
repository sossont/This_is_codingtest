# 다익스트라 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())

# 노드와 노드 사이에 거
graph = [[] for i in range(n+1)]

# 방문 체크 리스트
visited = [False] * (n+1)

# 최단 거리 테이블을 모두 무한으로 초기화.
distance = [INF] * (n+1)

for _ in range(m):
    # graph[a][0] = b. graph[a][1] = c. a에서 b로 가는 비용이 c.
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print(graph)


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        # 방문하지 않은 노드들 중에 가장 거리가 짧은 노드.
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return i

def dijkstra(start):
    distance[start] = 0
    visited[start] = True   # 방문했으니까~

    for i in graph[start]:  # a에서 b까지 거리가 c니까!
        distance[i[0]] = i[1]

    for i in range(n-1):
        now = get_smallest_node()   # 가장 거리가 짧은 노드 부터 방문한다.
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            if  cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한으로출력.
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])