# 이제는 27분 컷..
import heapq

INF = 987654321
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

shark_x, shark_y = 0,0
shark_size = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_x,shark_y = j,i
            graph[i][j] = 0
            break

def check(x,y):
    return 0<=x<N and 0<=y<N

def dijkstra(sx,sy):
    q = []
    global N
    global graph
    distance = [[INF] * N for _ in range(N)]
    distance[sy][sx] = 0
    heapq.heappush(q, [0,sy,sx])
    delta = [[-1,0],[1,0],[0,1],[0,-1]]
    while q:
        cost, y, x = heapq.heappop(q)
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            if not check(nx,ny):
                continue

            if distance[ny][nx] > cost + 1 and shark_size >= graph[ny][nx]:
                distance[ny][nx] = cost+1
                heapq.heappush(q, [cost+1,ny,nx])

    # 그러면 x,y 기준으로 거리가 나올 것
    ret = []
    for y in range(N):
        for x in range(N):
            if graph[y][x] != 0 and graph[y][x] < shark_size:
                heapq.heappush(ret,[distance[y][x], y, x])

    return ret

answer = 0
eat_count = 0
while True:
    arr = dijkstra(shark_x, shark_y)
    if len(arr) == 0:   # 잡아먹을 물고기가 없는 경우
        break
    # 잡아먹은 경우
    dist,gy,gx = heapq.heappop(arr)
    if dist == INF:
        break
    # 그 좌표 물고기 없애주고
    graph[gy][gx] = 0

    # 상어를 그좌표로 옮겨주고
    shark_x, shark_y = gx, gy
    # 먹은 개수 카운트 늘려주고, 사이즈 체크한다.
    eat_count += 1
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

    answer += dist

print(answer)
### =========
from collections import deque

# 가장 큰 관건 -> 경로 찾는 것
# 단순 BFS 돌리는 건 쉬운데, 어떻게 가장 가까운 경로를 계속 찾을 것이며, 탈출 조건은 어떻게?

N = int(input())
space = []
baby_shark = (0, 0)
for y in range(N):
    inp = list(map(int, input().split()))
    space.append(inp)
    for x in range(len(inp)):
        if inp[x] == 9:
            baby_shark = [y, x]
            space[y][x] = 0

# 위, 왼쪽, 오른쪽, 아래 순서대로 탐색.  [x,y]
delta = [[0, -1], [-1, 0], [1, 0], [0, 1]]


def check(x, y):  # (x,y) 가 범위 내에 있다면
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


shark_level = 2
shark_eat = 0
q = deque()
fishes = []
answer = 0
q.append([0, baby_shark[0], baby_shark[1]])
isvisited = [[False for _ in range(N)] for _ in range(N)]  # 방문 여부 체크
min_distance = 0

while q:
    if len(fishes) != 0 and q[0][0] != min_distance:  # 최단 거리로 갈 수 있는 물고기 발견!
        fishes.sort()
        dist, fish_y, fish_x = fishes[0]
        answer += dist  # 거리 더한다.

        shark_eat += 1

        if shark_eat == shark_level:
            shark_level += 1
            shark_eat = 0
        # 초기화
        space[fish_y][fish_x] = 0
        baby_shark = [fish_y, fish_x]
        isvisited = [[False for _ in range(N)] for _ in range(N)]

        q.clear()
        fishes.clear()
        q.append([0, fish_y, fish_x])

    q = deque(sorted(q))
    dis, y, x = q.popleft()
    isvisited[y][x] = True
    for d in delta:
        ny = y + d[1]
        nx = x + d[0]
        if not check(nx, ny):  # 맵 안에 안들어오면
            continue

        if shark_level < space[ny][nx]:  # 자신보다 큰 물고기를 지나갈 수 없다.
            continue

        if isvisited[ny][nx]:
            continue

        if space[ny][nx] < shark_level and space[ny][nx] != 0:
            min_distance = dis
            fishes.append([dis + 1, ny, nx])

        q.append([dis + 1, ny, nx])
        isvisited[ny][nx] = True

print(answer)

"""
fishes = []
shark_level = 2
shark_eat = 0
min_dist = 500
near_y = 0
near_x = 0
answer = 0
# 자신보다 큰 물고기를 지나갈 수 없다는 조건을 빼먹었네..
def check_fishes():
    fishes.clear()
    for y in range(N):
        for x in range(N):
            if space[y][x] != 0 and space[y][x] != 9:
                dist = abs(baby_shark[0] - y) + abs(baby_shark[1] - x)  # 이동 거리
                heapq.heappush(fishes, [dist, space[y][x], y, x])  # (거리,크기, y, x)순서


check_fishes()

while True:
    if len(fishes) == 0:
        print("min dist : ", min_dist)
        if min_dist == 500:  # 먹을수 있는 물고기가 없다면
            print(space)
            break  # 끝!
        else:
            shark_eat += 1
            answer += min_dist
            print("shark level : ", shark_level)
            print("near_y : ", near_y)
            print("near_x : ", near_x)
            space[near_y][near_x] = 0
            baby_shark = [near_y, near_x]
            check_fishes()  # 다시 fishes 배열 초기화
            min_dist = 500

            if shark_eat == shark_level:  # 레벨업 조건 만족
                shark_level += 1
                shark_eat = 0
            continue

    distance, level, fish_y, fish_x = heapq.heappop(fishes)  # 제일 가까운 물고기 꺼낸다.
    if shark_level <= level:  # 못 먹는 물고기임
        continue
    # 먹을 수 있는 물고기라면

    if min_dist > distance:  # 처음 최소 거리를 만났다.
        min_dist = distance
        near_y = fish_y
        near_x = fish_x
    elif min_dist == distance:
        if near_y > fish_y:  # 가장 위에 있는 물고기라면
            near_y = fish_y
            near_x = fish_x
        elif near_y == fish_y and near_x > fish_x:  # 가장 왼쪽에 있는 물고기 라면
            near_x = fish_x
    else:  # 최소 거리인 물고기가 정해졌다.
        print("min dist : ", min_dist)
        if min_dist == 500:  # 먹을수 있는 물고기가 없다면
            print(space)
            break  # 끝!
        else:
            shark_eat += 1
            answer += min_dist
            print("shark level : ", shark_level)
            print("near_y : ", near_y)
            print("near_x : ", near_x)
            space[near_y][near_x] = 0
            baby_shark = [near_y, near_x]
            check_fishes()  # 다시 fishes 배열 초기화
            min_dist = 500

            if shark_eat == shark_level:  # 레벨업 조건 만족
                shark_level += 1
                shark_eat = 0
            continue

print(answer)

"""
