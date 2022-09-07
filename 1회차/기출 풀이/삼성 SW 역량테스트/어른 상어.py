# 1의 번호를 가진 상어는 모두를 쫓아낼 수 있다.

# 1. 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
# 2. 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 그 칸에 냄새를 뿌린다.
# 냄새는 상어가 k번 이동하면 사라진다.

# 상어 이동방향 결정 방법
#
# 1. 아무 냄새가 없는 칸
# 2. 그런 칸이 없으면 자신의 냄새가 있는 칸
# 여러 칸인 경우 : 특정한 우선순위를 따른다. 상어마다 다르고, 같은 상어도 방향마다 다르다.


N, M, K = map(int, input().split())
graph = []
sharks = [[] for _ in range(M)]
for _ in range(N):
    graph.append(list(map(int, input().split())))

shark_graph = [[[] for _ in range(N)] for _ in range(N)]

for ky in range(N):
    for kx in range(N):
        if graph[ky][kx] != 0:
            shark_graph[ky][kx].append(graph[ky][kx])

shark_dir = list(map(int, input().split()))
smell = [[0] * N for _ in range(N)]

for s in range(M):
    sharks[s].append([])
    for _ in range(4):
        inp2 = list(map(int, input().split()))
        sharks[s].append(inp2)

smell_count = [[0] * N for _ in range(N)]

for y in range(N):
    for x in range(N):
        # 상어가 없으면
        if not shark_graph[y][x]:
            continue
        # 현재 좌표에 냄새부터 뿌린다.
        smell[y][x] = shark_graph[y][x][0]
        smell_count[y][x] = K

# sharks : 0~3번 상어의 방향 우선순위. 1~4 : 위 아 왼 오 향할 때 우선순위
# graph 에는 상어 번호가 1~4번으로 나타나있음을 주의!!!!!!


def check(now_x, now_y):
    if 0 <= now_x < N and 0 <= now_y < N:
        return True
    return False

def move():
    global N
    global shark_graph
    global shark_dir
    global smell
    global smell_count
    global K
    delta = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]  # 위 아래 왼쪽 오른쪽 (y,x)
    tmp = [[[] for _ in range(N)] for _ in range(N)]

    for y in range(N):
        for x in range(N):
            # 상어가 없으면
            if not shark_graph[y][x]:
                continue

            shark_num = shark_graph[y][x].pop() - 1
            # 상어의 현재 방향
            now_dir = shark_dir[shark_num]

            # 움직였으면 True로 바꿔줘야 한다.
            is_move = False
            # 우선순위로 확인
            for direct in sharks[shark_num][now_dir]:
                ny = y + delta[direct][0]
                nx = x + delta[direct][1]

                if not check(nx, ny):
                    continue

                # 냄새가 없는 칸으로 움직이는 경우
                if smell_count[ny][nx] <= 0:
                    tmp[ny][nx].append(shark_num + 1)
                    shark_dir[shark_num] = direct
                    is_move = True
                    break

            # 움직였으면 다음 상어 확인
            if is_move:
                continue

            # 빈 칸이 없으면, 자신의 냄새가 있는 칸으로 방향을 잡는다.
            for direct in sharks[shark_num][now_dir]:
                ny = y + delta[direct][0]
                nx = x + delta[direct][1]
                if not check(nx, ny):
                    continue

                # 자신의 냄새가 있는 칸인 경우
                if shark_num + 1 == smell[ny][nx]:
                    tmp[ny][nx].append(shark_num + 1)
                    shark_dir[shark_num] = direct
                    break


    # 모든 상어 이동 끝. 냄새 없애고 냄새 뿌린다.
    for yy in range(N):
        for xx in range(N):
            if smell_count[yy][xx] > 0:
                smell_count[yy][xx] -= 1
                if smell_count[yy][xx] == 0:
                    smell[yy][xx] = 0

            if len(tmp[yy][xx]) == 1:
                smell[yy][xx] = tmp[yy][xx][0]
                smell_count[yy][xx] = K
                continue

            if not tmp[yy][xx]:
                continue

            min_shark = M + 1
            while tmp[yy][xx]:
                now_num = tmp[yy][xx].pop()
                min_shark = min(now_num, min_shark)

            # 가장 작은 상어 한마리만 살아 남는다.
            tmp[yy][xx].append(min_shark)
            smell[yy][xx] = tmp[yy][xx][0]
            smell_count[yy][xx] = K

    shark_graph = tmp


answer = 0

while True:
    move()
    answer += 1
    if answer > 1000:
        answer = -1
        break

    count = 0
    for ky in range(N):
        for kx in range(N):
            if shark_graph[ky][kx]:
                count += 1

    if count == 1:
        break


print(answer)
