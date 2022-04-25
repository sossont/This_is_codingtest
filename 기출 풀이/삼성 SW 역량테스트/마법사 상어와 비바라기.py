# (r,c) r행 c열 -> (y,x)
# 왼쪽 위 (0,0) 오른쪽 아래 (N-1,N-1)
# 1번 행과 N번 행 연결, N번 열과 1번 열 연결

# 1. 비바라기 시전 :
# (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다

# 2. 구름의 이동 명령
# 모든 구름이 방향으로 이동한다.

# 3. 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.

# 4. 구름이 모두 사라진다.

# 5. 2에서 물이 증가한 칸에 물복사버그마법 시전

# 6. 구름이 사라졌던 칸 제외 바구니에 물 양이 2이상인 칸에 구름 생성

# 35분에 첫번째 완성, 근데 왜틀릴까

N, M = map(int, input().split())
graph = []

# [y,x]. 1부터 순서대로
delta = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

for _ in range(N):
    inp = list(map(int, input().split()))
    graph.append(inp)

move_op = []
for _ in range(M):
    inp = list(map(int, input().split()))
    move_op.append(inp)


# 처음에 생긴 구름

# --- 입력 끝 ---

# 모든 구름이 d 방향으로 s칸 이동
def move(d, s, inc_cloud):
    global cloud
    move_y = delta[d][0] * s
    move_x = delta[d][1] * s
    inc = []
    while cloud:
        y, x = cloud.pop()
        ny = (y + move_y) % N
        nx = (x + move_x) % N  # 이동한 구름의 y,x 좌표
        graph[ny][nx] += 1
        inc.append([ny, nx])  # 새로 이동한 구름의 좌표
        inc_cloud[ny][nx] = 1

    cloud = inc


# 경계 넘어가는 지 확인
def check(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True

    return False


# 물복사 버그 마법
def magic():
    global cloud
    d = [[-1, -1], [-1, 1], [1, -1], [1, 1]]  # 대각선 경우의 수 4가지
    for cur_y, cur_x in cloud:
        for dy, dx in d:
            ny = cur_y + dy
            nx = cur_x + dx
            if not check(nx, ny):
                continue

            if graph[ny][nx] > 0:
                graph[cur_y][cur_x] += 1


# 구름 생성
def create(old_cloud):
    new_cloud = []
    for yy in range(N):
        for xx in range(N):
            if graph[yy][xx] >= 2 and old_cloud[yy][xx] == 0:
                new_cloud.append([yy, xx])
                graph[yy][xx] -= 2

    return new_cloud


cloud = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]

for m in range(M):
    cloud2 = [[0] * N for _ in range(N)]
    di, si = move_op[m]
    di -= 1
    move(di, si, cloud2)
    magic()
    cloud = create(cloud2)

answer = 0
for i in range(N):
    for j in range(N):
        answer += graph[i][j]

print(answer)
