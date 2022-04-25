# 초등학교 + 중학교 2시간 컷

import heapq

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


# 반시계 방향 90도 회전
def rotate(g):
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for yy in range(N):
        for xx in range(N):
            temp[N - 1 - xx][yy] = graph[yy][xx]

    return temp


delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def check(cy, cx):
    if 0 <= cx < N and 0 <= cy < N:
        return True

    return False


def remove_block(start_y, start_x, num):
    global delta
    global graph
    q = []
    visited = [[False] * N for _ in range(N)]
    q.append([start_y, start_x])
    visited[start_y][start_x] = True
    yxlist = [[start_y, start_x]]
    # BFS
    while q:
        cy, cx = q.pop(0)
        for d in delta:
            ny = cy + d[0]
            nx = cx + d[1]
            if not check(ny, nx):
                continue

            if graph[ny][nx] == -1 or visited[ny][nx]:
                continue

            if graph[ny][nx] == 0 or graph[ny][nx] == num:
                visited[ny][nx] = True
                yxlist.append([ny, nx])
                q.append([ny, nx])

    # 블록 지우기
    while yxlist:
        y, x = yxlist.pop()
        graph[y][x] = -2


def gravitiy():
    global graph

    init_y = N - 1
    for xx in range(N):
        cur_y = init_y
        for _ in range(N - 1):
            if graph[cur_y][xx] == -2:
                for i in range(1, cur_y + 1):
                    if graph[cur_y - i][xx] == -1:
                        break

                    if graph[cur_y - i][xx] != -2:
                        graph[cur_y - i][xx], graph[cur_y][xx] = graph[cur_y][xx], graph[cur_y - i][xx]
                        break
            cur_y -= 1


answer = 0

while True:
    blocks = [[] for _ in range(M + 1)]
    h = []
    block_visit = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            # 검은색 블록이거나, 무지개 블록이거나, 빈칸이거나
            if graph[y][x] == -1 or graph[y][x] == 0 or graph[y][x] == -2:
                continue

            if block_visit[y][x]:
                continue

            q = []
            isvisited = [[False] * N for _ in range(N)]
            block_num = graph[y][x]
            rainbow_count = 0  # 무지개 블록 개수
            block_count = 1  # 사라질 블록 개수
            q.append([y, x])
            isvisited[y][x] = True

            # BFS
            while q:
                cy, cx = q.pop(0)
                for d in delta:
                    ny = cy + d[0]
                    nx = cx + d[1]
                    if not check(ny, nx):
                        continue

                    if graph[ny][nx] == -1 or graph[ny][nx] == -2 or isvisited[ny][nx]:
                        continue

                    if graph[ny][nx] == 0 or graph[ny][nx] == block_num:
                        block_count += 1
                        isvisited[ny][nx] = True
                        if graph[ny][nx] == 0:
                            rainbow_count += 1
                        else:
                            block_visit[ny][nx] = True
                        q.append([ny, nx])
            heapq.heappush(h, [-block_count, -rainbow_count, -y, -x, graph[y][x]])

    if len(h) == 0:
        break
    score, _, y, x, block_num = heapq.heappop(h)
    score = -score
    y = -y
    x = -x

    if score <= 1:
        break
    # 제외할 블록 더하기
    answer += score * score
    remove_block(y, x, block_num)
    gravitiy()
    graph = rotate(graph)
    gravitiy()
print(answer)
