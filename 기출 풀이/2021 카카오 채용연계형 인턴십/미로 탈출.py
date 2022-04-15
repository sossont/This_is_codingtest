# 결국엔 구글링해서 풀었다
# 결국 트랩 경우 따져서 비트 마스킹 하는 게 핵심

import heapq

INF = 987654321


def isReverse(cur_pos, nxt_pos, cur_state, trap_dic):
    nxt_trap_on = False
    cur_trap_on = False

    # 현재 노드가 트랩일 때, 현재 노드가 활성화 되어 있는지 확인한다. 활성화 되어있으면 True로 바뀔 것.
    if cur_pos in trap_dic:
        cur_trap_on = (cur_state & (1 << trap_dic[cur_pos])) > 0

    # 다음 노드가 트랩일 때, 다음 트랩이 활성화 되어 있는지 확인한다. 활성화 되어있으면 True로 바뀔 것.
    if nxt_pos in trap_dic:
        nxt_trap_on = (cur_state & (1 << trap_dic[nxt_pos])) > 0

    # 1.만약 하나만 활성화 되어 있으면 역방향
    # 2.둘 다 활성화 안되어 있으면 순방향
    # 3.둘 다 활성화 되어 있어도 순방향
    # 고로 1번의 경우는 True를 반환, 2,3번은 False를 반환한다.
    return nxt_trap_on != cur_trap_on


# 트랩일 경우 트랩 활성화 토글 시켜주는 함수
def getNextState(nxt, cur_state, trap_dic):
    if nxt in trap_dic:
        return cur_state ^ (1 << trap_dic[nxt])  # 트랩 마스킹 해준다.

    return cur_state


def solution(n, start, end, roads, traps):
    answer = INF
    graph = [[] for _ in range(n + 1)]
    # False : 활성화 안된 상태, 그대로 사용
    # True : 활성화 된 상태, 뒤집어서 사용
    for road in roads:
        p, q, s = road
        graph[p].append([q, s, False])  # 순방향
        graph[q].append([p, s, True])  # 역방향

    trap_dic = {}  # 트랩 개수별로 마킹하기
    for i in range(len(traps)):
        trap_dic[traps[i]] = i

    distance = [[INF] * (n + 1) for _ in range(2 ** len(traps))]  # 거리 저장해 놓을 곳
    q = []
    # 현재까지 거리, 현재 위치, 현재 트랩 상태
    heapq.heappush(q, [0, start, 0])
    distance[0][start] = 0

    while q:
        cur_cost, cur_pos, cur_state = heapq.heappop(q)
        if cur_pos == end:  # 종점 도달
            answer = min(answer, cur_cost)
            continue

        # 똑같은 상태일 때, 더 적은 비용으로 오는 방법이 있다.
        if cur_cost > distance[cur_state][cur_pos]:
            continue

        for nxt_pos, nxt_cost, is_reverse in graph[cur_pos]:
            # 방향이 안맞으면 탐색하지 않는다. 갈 수 없음
            if is_reverse != isReverse(cur_pos, nxt_pos, cur_state, trap_dic):
                continue

            nxt_state = getNextState(nxt_pos, cur_state, trap_dic)
            nxt_sum = nxt_cost + cur_cost

            # 같은 상태인데 더 적은 비용으로 갈 수 있으면 가지 않는다.
            if nxt_sum >= distance[nxt_state][nxt_pos]:
                continue

            distance[nxt_state][nxt_pos] = nxt_sum
            heapq.heappush(q, [nxt_sum, nxt_pos, nxt_state])

    return answer


# -----------
answer = 987654321
adj = [[] for _ in range(2000)]
isvisited = [[0 for _ in range(2000)] for _ in range(2000)]


def solution(n, start, end, roads, traps):
    graph = [[0 for _ in range(2000)] for _ in range(2000)]
    global answer
    for road in roads:
        s = road[0]
        e = road[1]
        cost = road[2]
        if graph[s][e] != 0:
            graph[s][e] = min(graph[s][e], cost)
        else:
            graph[s][e] = cost  # Cost는 방향으로 기록
        adj[s].append(e)  # 인접한 걸 기록
        adj[e].append(s)
    DFS(start, end, traps, 0, graph)
    return answer


def DFS(now, end, traps, costs, now_graph):
    global answer
    print("DFS!")
    if now == end:
        answer = min(answer, costs)
        return

    for nxt in adj[now]:  # 인접한 노드들.
        if now_graph[now][nxt] == 0:  # 이 방향 선이 존재하지 않음.
            continue

        if isvisited[now][nxt] == 1:  # 무한 루프 방지
            continue

        print(now, nxt, costs)
        cost = now_graph[now][nxt]
        isvisited[now][nxt] = 1
        graph = now_graph.copy()
        if nxt in traps:  # 다음 노드가  트랩이면
            # 다음 노드랑 연결되어 있는 녀석들 방향 바꿔준다.
            for node in adj[nxt]:
                tmp = now_graph[node][nxt]
                now_graph[node][nxt] = now_graph[nxt][node]
                now_graph[nxt][node] = tmp
            DFS(nxt, end, traps, costs + cost, now_graph)
        else:
            DFS(nxt, end, traps, costs + cost, graph)

        isvisited[now][nxt] = 0


# -----------------

import copy

answer = 987654321


def solution(n, start, end, roads, traps):
    graph = [[-1] * (n + 1) for _ in range(n + 1)]
    adj = [[] for _ in range(n + 1)]  # trap 노드 연결되어있는거 다 뒤집게
    direct = [[0] * (n + 1) for _ in range(n + 1)]
    # direct[a][b] 가 0이면 a->b 로 가는 방향
    # direct[a][b] 가 1이면 b->a 로 가는 방향
    for road in roads:
        p, q, s = road
        adj[p].append(q)
        adj[q].append(p)
        graph[p][q] = s
        graph[q][p] = s
        direct[p][q] = 0
        direct[q][p] = 1

    dfs(start, end, graph, adj, direct, traps, 0, [])
    return answer


def dfs(now, end, graph, adj, direct, traps, cost, visit_trap):
    global answer

    if now == end:  # 끝 도달
        answer = min(answer, cost)
        return

    for nxt in adj[now]:  # 현재 노드로 부터 인접한 노드들
        if nxt in visit_trap:  # 한번 방문한 트랩은 두번 방문하지 않는다.
            continue
        costs = cost + graph[now][nxt]
        if direct[now][nxt] == 0:  # 다음 방향으로 갈수 있다
            if nxt in traps:  # 다음 노드가 트랩인 경우

                direct_copy = copy.deepcopy(direct)
                v_trap = visit_trap.copy()
                if now in traps:
                    v_trap.append(nxt)
                for adj_trap in adj[nxt]:  # 트랩에 인접한 간선들 다 방향 바꿔준다
                    if direct_copy[nxt][adj_trap] == 0:
                        direct_copy[nxt][adj_trap] = 1
                        direct_copy[adj_trap][nxt] = 0
                    else:
                        direct_copy[nxt][adj_trap] = 0
                        direct_copy[adj_trap][nxt] = 1
                dfs(nxt, end, graph, adj, direct_copy, traps, costs, v_trap)
            else:
                dfs(nxt, end, graph, adj, direct, traps, costs, visit_trap)


r = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
t = [2, 3]
solution(4, 1, 4, r, t)
