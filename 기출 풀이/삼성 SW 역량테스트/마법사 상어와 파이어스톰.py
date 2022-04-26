from collections import deque

N, Q = map(int, input().split())
n = pow(2, N)  # 2^N

ices = []
for _ in range(n):
    inp = list(map(int, input().split()))
    ices.append(inp)

level = list(map(int, input().split()))

# ---- 입력 끝 ----
graph = ices
temp = [[0] * n for _ in range(n)]


# temp[x][(길이 - 1) - y]
# 90 도 회전
def rotate(start_x, start_y, d):
    global temp
    global graph
    for cy in range(d):
        for cx in range(d):
            temp[start_y + cx][start_x + (d - 1) - cy] = graph[start_y + cy][start_x + cx]

    for cy in range(d):
        for cx in range(d):
            graph[start_y + cx][start_x + (d - 1) - cy] = temp[start_y + cx][start_x + (d - 1) - cy]


def check(kx, ky):
    if 0 <= kx < n and 0 <= ky < n:
        return True
    return False


delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

q = Q

while q > 0:
    l = level[Q - q]
    q -= 1
    expl = pow(2, l)  # 격자 한 변의 길이
    max_y = n // expl  # 격자가 한 변에 차는 갯수
    init_y = 0

    # 격자로 나눠서 돌리기
    if l != 0:
        for yy in range(max_y):
            # init_y, init_x : 격자 별 시작 좌표(왼쪽 위)
            init_x = 0
            while init_x < n:
                rotate(init_x, init_y, expl)
                init_x += expl
            init_y += expl

    delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    will_destroy = []
    for y in range(n):
        for x in range(n):
            ice_count = 0
            for d in delta:
                ny = y + d[0]
                nx = x + d[1]
                if not check(nx, ny):
                    continue

                if graph[ny][nx] != 0:
                    ice_count += 1

            if ice_count < 3:
                will_destroy.append([y, x])

    # 얼음 양 줄어든다.
    while will_destroy:
        wy, wx = will_destroy.pop()
        if graph[wy][wx] > 0:
            graph[wy][wx] -= 1

isvisited = [[False] * n for _ in range(n)]
answer = 0

# 남아있는 얼음의 합

for y in range(n):
    for x in range(n):
        answer += graph[y][x]

max_block = 0
for y in range(n):
    for x in range(n):
        if isvisited[y][x]:
            continue

        if graph[y][x] == 0:
            continue

        queue = deque([])
        queue.append([y, x])
        block = 1
        while queue:
            cy, cx = queue.popleft()
            isvisited[cy][cx] = True
            for d in delta:
                ny = cy + d[0]
                nx = cx + d[1]
                if not check(nx, ny):
                    continue

                if not isvisited[ny][nx] and graph[ny][nx] != 0:
                    block += 1
                    isvisited[ny][nx] = True
                    queue.append([ny, nx])

        max_block = max(max_block, block)

print(answer)
print(max_block)