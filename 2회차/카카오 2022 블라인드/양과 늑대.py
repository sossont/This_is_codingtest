answer = 0

def solution(info, edges):
    adj = [[] for _ in range(18)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    isvisited = [False] * 18
    info[0] = -1
    dfs(info, 0, 1, 0, adj, isvisited)
    return answer


def dfs(info, now, sheep, wolf, adj, isvisited):
    global answer
    for nxt in adj[now]:
        tmp_info = info[:]
        visited = isvisited[:]
        visited[now] = True
        if tmp_info[nxt] == 0:
            tmp_info[nxt] = -1
            visited = [False] * 18
            dfs(tmp_info, nxt, sheep + 1, wolf, adj, visited)
        elif tmp_info[nxt] == 1 and sheep > wolf + 1:
            tmp_info[nxt] = -1
            dfs(tmp_info, nxt, sheep, wolf + 1, adj, visited)
        elif tmp_info[nxt] == -1 and not visited[nxt]:
            dfs(tmp_info, nxt, sheep, wolf, adj, visited)

    if answer < sheep:
        answer = sheep