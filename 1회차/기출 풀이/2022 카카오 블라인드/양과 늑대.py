answer = 1


def solution(info, edges):
    global answer
    adj = [[] for _ in range(len(info))]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    # 시작점은 양이 한개 있으니까
    for nxt in adj[0]:
        sheep_count = 1
        wolf_count = 0
        isvisited = [False] * len(info)
        info[0] = -1
        c_info = info[:]
        if info[nxt] == 1:
            if sheep_count > wolf_count + 1:
                c_info[nxt] = -1
                isvisited[nxt] = True
                dfs(c_info, adj, nxt, sheep_count, wolf_count + 1, isvisited)
        elif info[nxt] == 0:
            isvisited[nxt] = True
            c_info[nxt] = -1
            dfs(c_info, adj, nxt, sheep_count + 1, wolf_count, isvisited)

    return answer


def dfs(info, adj, now, scount, wcount, isvisited):
    global answer
    # 현재랑 연결된 지점 1~3개나옴
    for nxt in adj[now]:
        c_info = info[:]
        # 다음 지점에 양이 있으면
        if info[nxt] == 0:
            # 방문 여부 초기화
            c_isvisited = [False] * len(info)
            c_isvisited[nxt] = True
            c_info[nxt] = -1
            dfs(c_info, adj, nxt, scount + 1, wcount, c_isvisited)
        else:
            if isvisited[nxt]:
                continue

            c_isvisited = isvisited.copy()
            if info[nxt] == 1 and scount > wcount + 1:
                c_isvisited[nxt] = True
                c_info[nxt] = -1
                dfs(c_info, adj, nxt, scount, wcount + 1, c_isvisited)
            elif info[nxt] == -1:
                c_isvisited[nxt] = True
                dfs(c_info, adj, nxt, scount, wcount, c_isvisited)

    answer = max(answer, scount)
