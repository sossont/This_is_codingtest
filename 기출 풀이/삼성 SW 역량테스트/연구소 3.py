import heapq

N, M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))


virus = []
for y in range(N):
    for x in range(N):
        if graph[y][x] == 2:
            virus.append([y,x])
            graph[y][x] = 0

# 바이러스 위치를 이따가 -1로 만들 것.

def combination(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in combination(arr[i+1:], r-1):
                yield [arr[i]] + nxt


def check(xx,yy):
    global N
    return 0<=xx<N and 0<=yy<N

def bfs(xx,yy, distance):
    global graph
    delta = [[-1,0],[1,0],[0,-1],[0,1]]
    distance[yy][xx] = 0
    q = []
    heapq.heappush(q, [0,xx,yy])
    while q:
        cost, x, y =heapq.heappop(q)

        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            if not check(nx, ny):
                continue

            if graph[ny][nx] == 1:
                continue

            if distance[ny][nx] > cost + 1:
                distance[ny][nx] = cost + 1
                heapq.heappush(q, [cost+1, nx, ny])

INF = 987654321

min_dist = INF
for viruss in combination(virus, M):
    dist = [[INF] * N for _ in range(N)]
    for v in viruss:
        bfs(v[1], v[0],dist)

    print("-======-")
    for d in dist:
        print(d)
    max_dist = 0
    flag = False
    for v in virus:
        if dist[v[0]][v[1]] == INF:
            flag = True
            break

    if flag:
        continue

    for y in range(N):
        for x in range(N):
            if dist[y][x] == INF:
                dist[y][x] = -1
            max_dist = max(dist[y][x], max_dist)

    if max_dist != 0:
        min_dist = min(max_dist,min_dist)

if min_dist == INF:
    print("-1")
else:
    print(min_dist)

