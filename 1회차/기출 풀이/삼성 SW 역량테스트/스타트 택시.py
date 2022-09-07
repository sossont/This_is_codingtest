import heapq

N,M,answer = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

ds_y, ds_x = map(int,input().split())   # 운전 시작하는 행열 번호

target = []
for _ in range(M):
    target.append(list(map(int,input().split())))

def check(x,y):
    if 0<=x<N and 0<=y<N:
        return True

    return False

# 최단 거리 구하기

def dikjstra(x,y):
    global graph
    delta = [[-1,0],[1,0],[0,1],[0,-1]]
    q = []
    heapq.heappush(q, [0,x,y])
    distance = [[100] * N for _ in range(N)]
    distance[y][x] = 0
    while q:
        cost,x,y = heapq.heappop(q)
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            if not check(nx,ny):
                continue
            if graph[ny][nx] == 1:
                continue
            if distance[ny][nx] > cost + 1:
                distance[ny][nx] = cost + 1
                heapq.heappush(q, [cost+1, nx, ny])


    return distance

ds_x -= 1
ds_y -= 1


while True:
    if len(target) == 0:
        break
    start_dist = dikjstra(ds_x,ds_y)
    q = []

    for i in range(len(target)):
        sy,sx,dy,dx = target[i]
        heapq.heappush(q, [start_dist[sy-1][sx-1], sy-1, sx-1, dy-1, dx-1, i])
    # 최단거리 승객 고름
    start_fuel, sy, sx, dy, dx, idx = heapq.heappop(q)
    if start_fuel == 100:
        answer = -1
        break
    target = target[:idx] + target[idx+1:] #target에서 삭제
    # 승객한테 까지 가는 연료 : start_fuel
    end_dist = dikjstra(sx,sy)
    # 승객 목적지까지 가는 연료
    end_fuel = end_dist[dy][dx]
    if end_fuel == 100:
        answer = -1
        break
    # 연료가 바닥나는 경우
    if start_fuel + end_fuel > answer:
        answer = -1
        break

    # 연료 두배 충전
    answer += end_fuel - start_fuel
    ds_x = dx
    ds_y = dy


print(answer)