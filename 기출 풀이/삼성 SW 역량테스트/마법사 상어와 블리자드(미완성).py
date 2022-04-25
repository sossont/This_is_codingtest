# 정답 코드
# 직렬화 생각을 어케하냐,,하,,
from collections import deque

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # y,x 4가지 방향 순서

N, M = map(int, input().split())

inp = []
for _ in range(N):
    inp.append(list(map(int, input().split())))

magics = []
for _ in range(M):
    magics.append(map(int, input().split()))


# 2차원 배열을 1차원 배열로 바꿔보자.


def add_move():
    cur_y = (N + 1) // 2 - 1
    cur_x = (N + 1) // 2 - 1
    move_list = []
    for n in range(3, N + 1):
        if n % 2 == 0:
            continue
        cur_x -= 1
        move_list.append([cur_y, cur_x])  # 왼

        # 아래 * N-2
        for _ in range(n - 2):
            cur_y += 1
            move_list.append([cur_y, cur_x])

        # 오 * N-1
        for _ in range(n - 1):
            cur_x += 1
            move_list.append([cur_y, cur_x])

        # 위 * N-1
        for _ in range(n - 1):
            cur_y -= 1
            move_list.append([cur_y, cur_x])

        # 왼 * N-1
        for _ in range(n - 1):
            cur_x -= 1
            move_list.append([cur_y, cur_x])

    return move_list


moves = add_move()
blocks = []
# 1차원 배열로 바꿈
graph = [[0] * N for _ in range(N)]

# graph : 해당 좌표의 배열 번호
# blocks : 번호 담겨있는걸 일차원 배열로 나열한 것
# moves : 해당 배열 번호의 좌표

for num in range(len(moves)):
    y_pos, x_pos = moves[num]
    if inp[y_pos][x_pos] == 0:
        blocks.append(-1)
    else:
        blocks.append(inp[y_pos][x_pos])
    graph[y_pos][x_pos] = num

# ---- 세팅 끝 ----

destroy = [0, 0, 0, 0]


# 1. 상어가 마법 시전

def magic(di, si):
    global delta
    global blocks
    global graph
    global destroy
    cur_y = (N + 1) // 2 - 1  # 상어 y,x 좌표
    cur_x = (N + 1) // 2 - 1
    for ds in range(1, si + 1):
        ny = cur_y + delta[di - 1][0] * ds
        nx = cur_x + delta[di - 1][1] * ds
        bubble_num = graph[ny][nx]
        # -1 : 구슬 삭제
        if bubble_num >= len(blocks):
            continue
        blocks[bubble_num] = -1


# 2. 구슬이 빈칸 채워서 이동
def move():
    global blocks
    temp = []
    for b in blocks:
        if b == -1:
            continue
        temp.append(b)
    blocks = temp


# 3. 구슬 폭발 후 재배열
def explode():
    global blocks
    global destroy
    count = 0
    bef = 0
    block_num = 0
    flag = False
    for b in range(len(blocks)):
        if blocks[b] == blocks[bef]:  # 이전 블록과 연속되면
            block_num = blocks[b]
            count += 1
        else:
            if count >= 4:
                flag = True
                for n in range(bef, b):
                    blocks[n] = -1
                destroy[block_num] += count
            count = 1
            bef = b
            block_num = blocks[b]

    if count >= 4:
        flag = True
        for n in range(bef, len(blocks)):
            blocks[n] = -1
        destroy[block_num] += count

    return flag


# 4. 구슬 변화
def trans():
    global blocks
    q = deque()
    count = 0
    bef = 0
    block_num = 0
    for i in range(len(blocks)):
        if blocks[i] == blocks[bef]:
            block_num = blocks[i]
            count += 1
        else:
            q.append([count, block_num])
            count = 1
            bef = i
            block_num = blocks[i]

    q.append([count, block_num])

    tmp = []
    while q:
        a, b = q.popleft()
        if a != 0:
            tmp.append(a)
        if len(tmp) == N * N - 1:
            break

        if b != 0:
            tmp.append(b)
        if len(tmp) == N * N - 1:
            break

    blocks = tmp


for d, s in magics:
    magic(d, s)
    move()
    while explode():
        move()
    trans()

answer = destroy[1] + 2 * destroy[2] + 3 * destroy[3]
print(answer)

### 틀린 코드
from collections import deque

# N은 항상 홀수. y,x
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

magics = []
for _ in range(M):
    di, si = map(int, input().split())
    magics.append([di, si])


def add_move():
    cur_y = (N + 1) // 2 - 1
    cur_x = (N + 1) // 2 - 1
    move_list = []
    for n in range(3, N + 1):
        if n % 2 == 0:
            continue
        cur_x -= 1
        move_list.append([cur_y, cur_x])  # 왼

        # 아래 * N-2
        for _ in range(n - 2):
            cur_y += 1
            move_list.append([cur_y, cur_x])

        # 오 * N-1
        for _ in range(n - 1):
            cur_x += 1
            move_list.append([cur_y, cur_x])

        # 위 * N-1
        for _ in range(n - 1):
            cur_y -= 1
            move_list.append([cur_y, cur_x])

        # 왼 * N-1
        for _ in range(n - 1):
            cur_x -= 1
            move_list.append([cur_y, cur_x])

    return move_list


block_num = add_move()  # 칸의 번호가 적혀있는 것
bubble_count = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            bubble_count += 1


# -- 빈칸으로 구슬 이동하는 함수 --
def move():
    global block_num
    global graph
    count = 0
    for num in range(0, len(block_num) - count):
        num_y, num_x = block_num[num]
        count = 0
        if graph[num_y][num_x] == 0:
            count += 1
            while True:
                if num + count >= len(block_num):
                    break
                next_y, next_x = block_num[num + count]

        if (num + count) >= len(block_num):
            break
        next_y, next_x = block_num[num + count]
        graph[num_y][num_x], graph[next_y][next_x] = graph[next_y][next_x], graph[num_y][num_x]

    print("=======")
    for g in graph:
        print(g)


def check():
    global block_num
    global graph
    global bubble_count
    global destroy
    will_remove = deque()

    while True:
        count = 1
        bef_num = graph[block_num[0][0]][block_num[0][1]]
        for num in range(1, bubble_count):
            num_y, num_x = block_num[num]
            # 같은 구슬 개수 세기
            if graph[num_y][num_x] != 0 and graph[num_y][num_x] == bef_num:
                count += 1
            else:
                # 같은 블록의 개수가 4개 이상이면
                if count >= 4:
                    will_remove.append([num - count, num - 1])  # 같은 번호 구간 기록
                count = 1
                bef_num = graph[num_y][num_x]

        if count >= 4:  # 마지막 구간 까지 기록
            will_remove.append([len(block_num) - count, len(block_num) - 1])  # 같은 번호 구간 기록

        # 만약 더이상 폭발할 구슬이 없으면 탈출
        if len(will_remove) == 0:
            break

        while will_remove:
            rev = will_remove.popleft()
            start, end = rev
            # 블록 번호 구간 쭉 터트리기
            for k in range(start, end + 1):
                ky, kx = block_num[k]

                destroy[graph[ky][kx]] += 1
                graph[ky][kx] = 0
                bubble_count -= 1

        move()


def trans():
    global block_num
    global graph
    global bubble_count
    group = deque()
    bef_num = graph[block_num[0][0]][block_num[0][1]]
    count = 1
    for k in range(1, bubble_count):
        cur_y, cur_x = block_num[k]
        if graph[cur_y][cur_x] == bef_num:
            count += 1
        else:
            group.append([count, bef_num])
            bef_num = graph[cur_y][cur_x]
            count = 1
    group.append([count, bef_num])
    # --- A,B 생성 ---

    # 순서대로 넣기
    block_count = 0
    bubble_count = 0
    while group:
        a, b = group.popleft()
        graph[block_num[block_count][0]][block_num[block_count][1]] = a
        bubble_count += 1
        block_count += 1
        if block_count == len(block_num):
            break

        graph[block_num[block_count][0]][block_num[block_count][1]] = b
        block_count += 1
        bubble_count += 1
        if block_count == len(block_num):
            break


destroy = [0, 0, 0, 0]
for di, si in magics:
    # 1. 상어가 구슬 폭발 시킨다.
    init_y = (N + 1) // 2 - 1  # 상어 좌표
    init_x = (N + 1) // 2 - 1

    for i in range(1, si + 1):
        ny = init_y + d[di - 1][0] * i
        nx = init_x + d[di - 1][1] * i
        if 0 > ny or 0 > nx or ny >= N or nx >= N:
            break
        graph[ny][nx] = 0  # 구슬 터트린다.
        bubble_count -= 1  # 구슬 갯수
    move()
    check()
    trans()

answer = destroy[1] + 2 * destroy[2] + 3 * destroy[3]
print(answer)
