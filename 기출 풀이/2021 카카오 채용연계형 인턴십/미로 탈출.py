answer = 987654321
adj = [[] for _ in range(2000)]
isvisited = [[0 for _ in range(2000)] for _ in range(2000)]

def solution(n, start, end, roads, traps):
    graph = [[0 for _ in range(2000)] for _ in range(2000)]
    global answer
    for road in roads:
        s = road[0]
        e= road[1]
        cost = road[2]
        if graph[s][e] != 0:
            graph[s][e] = min(graph[s][e],cost)
        else:
            graph[s][e] = cost  # Cost는 방향으로 기록
        adj[s].append(e)    # 인접한 걸 기록
        adj[e].append(s)
    DFS(start,end,traps, 0, graph)
    return answer


def DFS(now, end, traps, costs, now_graph):
    global answer
    print("DFS!")
    if now == end:
        answer = min(answer,costs)
        return

    for nxt in adj[now]: # 인접한 노드들.
        if now_graph[now][nxt] == 0:    # 이 방향 선이 존재하지 않음.
            continue

        if isvisited[now][nxt] == 1:    # 무한 루프 방지
            continue

        print(now, nxt, costs)
        cost = now_graph[now][nxt]
        isvisited[now][nxt] = 1
        graph = now_graph.copy()
        if nxt in traps:    # 다음 노드가  트랩이면
            # 다음 노드랑 연결되어 있는 녀석들 방향 바꿔준다.
            for node in adj[nxt]:
                tmp = now_graph[node][nxt]
                now_graph[node][nxt] = now_graph[nxt][node]
                now_graph[nxt][node] = tmp
            DFS(nxt, end, traps, costs + cost, now_graph)
        else:
            DFS(nxt, end, traps, costs + cost, graph)

        isvisited[now][nxt] = 0
