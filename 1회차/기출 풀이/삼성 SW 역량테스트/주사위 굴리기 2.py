from collections import deque

# (1,1) -> (N,M)
# N이 세로, M이 가로
N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


# 지도 입력 끝
# 0~N-1 , 0~M-1

# 맵 안에 들어오는지
def check(nextx, nexty):
    if 0 <= nextx < M and 0 <= nexty < N:
        return True

    return False


# 4 * 3 주사위
cube = [[0] * 3 for _ in range(4)]
cube[0][1] = 2
cube[1][0], cube[1][1], cube[1][2] = 4, 1, 3
cube[2][1] = 5
cube[3][1] = 6


# 주사위 움직이기

def move_right(c):
    case1, case2, case3, case4 = c[1][0], c[1][1], c[1][2], c[3][1]
    c[1][1] = case1
    c[1][2] = case2
    c[3][1] = case3
    c[1][0] = case4


def move_left(c):
    case1, case2, case3, case4 = c[1][0], c[1][1], c[1][2], c[3][1]
    c[1][0] = case2
    c[1][1] = case3
    c[3][1] = case1
    c[1][2] = case4


def move_up(c):
    case1, case2, case3, case4 = c[0][1], c[1][1], c[2][1], c[3][1]
    c[0][1] = case2
    c[1][1] = case3
    c[2][1] = case4
    c[3][1] = case1


def move_down(c):
    case1, case2, case3, case4 = c[0][1], c[1][1], c[2][1], c[3][1]
    c[1][1], c[2][1], c[3][1] = case1, case2, case3
    c[0][1] = case4


# 아랫면 좌표 : c[3][1]

direction = 0  # 0 : 동 1 : 남 2 : 서 3 : 븍


# 1. 이동방향으로 한 칸 굴러간다.
def change_dir(y, x):
    global direction
    ny = y + delta[direction][0]
    nx = x + delta[direction][1]
    if not check(nx, ny):  # 해당 방향에 칸이 없으면 반대 방향으로 바꾼다.
        direction += 2

    if direction >= 4:
        direction -= 4
    elif direction < 0:
        direction += 4


def move(direct):
    global cube
    global cube_y
    global cube_x
    if direct == 0:
        move_right(cube)
        cube_x += 1
    elif direct == 1:
        move_down(cube)
        cube_y += 1
    elif direct == 2:
        move_left(cube)
        cube_x -= 1
    elif direct == 3:
        move_up(cube)
        cube_y -= 1


delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # y,x 이동


# 2. 점수 획득
def calc(x, y, b):
    isvisited = [[False] * M for _ in range(N)]
    q = deque()
    q.append([y, x])
    count = 1
    while q:
        now_y, now_x = q.popleft()
        isvisited[now_y][now_x] = True
        for i in range(4):
            ny = now_y + delta[i][0]
            nx = now_x + delta[i][1]
            if not check(nx, ny):  # 칸을 벗어나면
                continue

            if isvisited[ny][nx]:
                continue

            if graph[ny][nx] == b:
                q.append([ny, nx])
                isvisited[ny][nx] = True
                count += 1

    return count * b


answer = 0
cube_y = 0
cube_x = 0

for _ in range(K):
    change_dir(cube_y, cube_x)
    move(direction)
    B = graph[cube_y][cube_x]
    answer += calc(cube_x, cube_y, B)
    if cube[3][1] > B:
        direction += 1
    elif cube[3][1] < B:
        direction -= 1

    if direction >= 4:
        direction -= 4
    elif direction < 0:
        direction += 4

print(answer)
