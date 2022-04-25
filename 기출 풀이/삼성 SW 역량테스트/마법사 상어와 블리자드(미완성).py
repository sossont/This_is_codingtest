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
