import heapq
from itertools import permutations
from copy import deepcopy

# 1. 출발점 지정
# 2. 거기서 카드 두 지점 둘다 가는 방법 구하고
# 3. 둘 다 경우를 따진다. 그리고 1번 무한 반복
# 4. 다 지우면 값 비교


# 맵 안에 들어오는지 확인
def check(y, x):
    if 0 <= y < 4 and 0 <= x < 4:
        return True

    return False


# 맵 넣고 (y,x) -> (r,c)에 출발점 넣으면 r,c부터 dest_y, dest_x까지 거리
def bfs(board, r, c, dest_y, dest_x):
    q = []
    INF = 987654321
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 움직일 수 있는 경우의 수
    distance = [[INF] * 4 for _ in range(4)]
    heapq.heappush(q, [0, r, c])
    while q:
        cost, y, x = heapq.heappop(q)
        if distance[y][x] <= cost:
            continue

        distance[y][x] = cost
        for d in direction:  # 그냥 상, 하, 좌, 우 움직이는 경우
            ny = y + d[0]
            nx = x + d[1]
            if not check(ny, nx):  # 맵 밖을 벗어나면
                continue

            if distance[ny][nx] > cost + 1:
                heapq.heappush(q, [cost + 1, ny, nx])

        for d in direction:  # Ctrl로 움직이는 경우
            flag = False
            ny = y
            nx = x
            while True:

                if not check(ny + d[0], nx + d[1]):
                    break

                ny = ny + d[0]
                nx = nx + d[1]
                flag = True

                if board[ny][nx] != 0:
                    break

            if not flag:
                continue

            if distance[ny][nx] > cost + 1:
                heapq.heappush(q, [cost + 1, ny, nx])
    return distance[dest_y][dest_x]


card_pos = [[] for _ in range(7)]
answer = 987654321


def calc(board, start_y, start_x, idx, order, cost):
    global answer

    if cost >= answer:  # 이거 넣으니까 14, 15, 16, 22, 23, 25 간신히 통과
        return

    if idx == len(order):  # 종료 조건.
        answer = min(answer, cost)
        return

    card_num = order[idx]
    pos1_y, pos1_x = card_pos[card_num][0]
    pos2_y, pos2_x = card_pos[card_num][1]

    dist2 = bfs(board, start_y, start_x, pos1_y, pos1_x) + bfs(board, pos1_y, pos1_x, pos2_y, pos2_x)

    dist1 = bfs(board, start_y, start_x, pos2_y, pos2_x) + bfs(board, pos2_y, pos2_x, pos1_y, pos1_x)

    copy_board = deepcopy(board) # 이거 위에서 이쪽으로 옮기니까 시간 초과 해결
    copy_board[pos1_y][pos1_x] = 0  # 없앤다.
    copy_board[pos2_y][pos2_x] = 0

    calc(copy_board, pos1_y, pos1_x, idx + 1, order, cost + dist1 + 2)
    calc(copy_board, pos2_y, pos2_x, idx + 1, order, cost + dist2 + 2)


def solution(board, r, c):
    card_list = []
    global answer

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_list.append(board[i][j])
                card_pos[board[i][j]].append((i, j))

    card_list = set(card_list)
    card_order = list(permutations(card_list, len(card_list)))  # 카드 제거하는 순서

    # 1. 출발점 지정
    # 2. 거기서 카드 두 지점 둘다 가는 방법 구하고
    # 3. 둘 다 경우를 따진다. 그리고 1번 무한 반복
    # 4. 다 지우면 값 비교

    for order in card_order:
        start_y, start_x = r, c  # 출발점
        card_num = order[0]
        pos1_y, pos1_x = card_pos[card_num][0]
        pos2_y, pos2_x = card_pos[card_num][1]

        # 거리 구하기
        dist2 = bfs(board, start_y, start_x, pos1_y, pos1_x) + bfs(board, pos1_y, pos1_x, pos2_y, pos2_x)
        dist1 = bfs(board, start_y, start_x, pos2_y, pos2_x) + bfs(board, pos2_y, pos2_x, pos1_y, pos1_x)

        copy_board = deepcopy(board) # 이거 위에서 이쪽으로 옮기니까 시간 초과 해결
        copy_board[pos1_y][pos1_x] = 0  # 없앤다.
        copy_board[pos2_y][pos2_x] = 0

        calc(copy_board, pos1_y, pos1_x, 1, order, dist1 + 2)
        calc(copy_board, pos2_y, pos2_x, 1, order, dist2 + 2)

    return answer


# --------


# 지정한 지점에서 출발
# 이동하는 방식은 1. 어떤 방향으로 한 칸 이동  2.방향에 있는 카드까지 가거나 마지막 칸 까지 가는 것
# 앞면이 보이게 카드를 뒤집었으면, 그 카드를 먼저 찾아야 한다.

# 1. 시작 지점에서 두 가지 방식으로 출발한다.
# 2. 카드를 발견했을 때 내가 타겟이 없다면 뒤집는다.
# 3. 타겟이 있다면 매칭될 경우 없애 준다.
# 모든 카드가 없어질 떄까지 이 과정을 반복한다.

## Key Point : 움직이는 방식과, 탈출 조건
## 그리고 모든 경우를 탐색할 때, 어떻게 시간을 줄여줄 것인가?
## isvisited 함수의 사용 여부


import copy

# (y,x) 다. 오른쪽, 위, 왼쪽, 아래 순서
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def check(y, x):
    if 0 <= y < 4 and 0 <= x < 4:
        return True

    return False


answer = 987654321


def solution(board, r, c):
    global answer
    total = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                total += board[i][j]
    target = board[r][c]
    board[r][c] = 0
    cost = 0
    if target != 0:  # 뒤집어야 하니까
        total = total - target
        cost = 1

    isvisited = [[False] * 4 for _ in range(4)]
    isvisited[r][c] = True
    for i in range(4):
        dfs(board, i, cost, r, c, target, copy.deepcopy(isvisited), total)
        ctrl(board, i, cost, r, c, target, copy.deepcopy(isvisited), total)
    return answer


# 그냥 가는 경우
def dfs(board, direction, cost, y, x, target, isvisited, total):
    global answer
    # 탐색이 끝난 경우
    isvisited[y][x] = True
    if total == 0:
        print(answer)

        answer = min(answer, cost)
        return

    ny = y + d[direction][0]
    nx = x + d[direction][1]

    # 맵 안에 안 들어오면 탐색할 가치가 없다.
    if not check(ny, nx):
        return

    if isvisited[ny][nx]:  # 방문했던 곳이면 방문하지 않는다.
        return

    # Target이 0 인경우
    if target == 0:
        if board[ny][nx] != 0:  # 만약 보드에 카드가 있으면 뒤집어서 타겟으로 설정.
            target = board[ny][nx]
            copy_board = copy.deepcopy(board)
            copy_board[ny][nx] = 0
            isvisit = [[False] * 4 for _ in range(4)]
            for i in range(4):
                dfs(copy_board, i, cost + 2, ny, nx, target, isvisit, total - target)
                ctrl(copy_board, i, cost + 2, ny, nx, target, isvisit, total - target)
        else:  # 보드에 카드가 없는 경우
            for i in range(4):
                dfs(board, i, cost + 1, ny, nx, target, isvisited, total)
                ctrl(board, i, cost + 1, ny, nx, target, isvisited, total)
    else:  # Target이 존재하는 경우
        if board[ny][nx] == target:  # 타겟이랑 같은 카드면 뒤집어서 없앤다.
            copy_board = copy.deepcopy(board)
            copy_board[ny][nx] = 0
            isvisit = [[False] * 4 for _ in range(4)]

            for i in range(4):
                dfs(copy_board, i, cost + 2, ny, nx, 0, isvisit, total - target)
                ctrl(copy_board, i, cost + 2, ny, nx, 0, isvisit, total - target)
        else:  # 타겟을 만나지 못했으면 계속 탐색
            for i in range(4):
                dfs(board, i, cost + 1, ny, nx, target, isvisited, total)
                ctrl(board, i, cost + 1, ny, nx, target, isvisited, total)

    return answer


# 컨트롤 키 눌러서 가는 경우
def ctrl(board, direction, cost, y, x, target, isvisited, total):
    global answer
    isvisited[y][x] = True
    # 탐색이 끝난 경우
    if total == 0:
        print(answer)
        answer = min(answer, cost)
        return

    ny = y
    nx = x
    while True:
        ny += d[direction][0]
        nx += d[direction][1]

        # 보드 끝에 도달한 경우
        if not check(ny, nx):
            ny -= d[direction][0]
            nx -= d[direction][1]
            break

        # 카드를 만나는 경우
        if board[ny][nx] != 0:
            break

    # 이미 이 사이클에서 반복한 적이 있으면
    if isvisited[ny][nx]:
        return

    # 타겟이 없을 때 카드를 만나면 그걸 타겟으로 삼고 탐색
    if target == 0:
        if board[ny][nx] != 0:
            target = board[ny][nx]
            copy_board = copy.deepcopy(board)
            copy_board[ny][nx] = 0
            isvisit = [[False] * 4 for _ in range(4)]  # 타겟 새로 만들어 줬으니, 새로 방문여부 만들어서 넣어준다.
            for i in range(4):
                dfs(copy_board, i, cost + 2, ny, nx, target, copy.deepcopy(isvisit), total - target)
                ctrl(copy_board, i, cost + 2, ny, nx, target, copy.deepcopy(isvisit), total - target)
        else:
            # 타겟도 없고 맵 끝에 닿은 경우 계속 탐색
            for i in range(4):
                dfs(board, i, cost + 1, ny, nx, target, copy.deepcopy(isvisited), total)
                ctrl(board, i, cost + 1, ny, nx, target, copy.deepcopy(isvisited), total)
    else:

        # 타겟이랑 만난 카드랑 같은 경우 뒤집어서 없앤다.
        if target == board[ny][nx]:
            copy_board = copy.deepcopy(board)
            copy_board[ny][nx] = 0
            isvisit = [[False] * 4 for _ in range(4)]
            for i in range(4):
                dfs(copy_board, i, cost + 2, ny, nx, 0, copy.deepcopy(isvisit), total - target)
                ctrl(copy_board, i, cost + 2, ny, nx, 0, copy.deepcopy(isvisit), total - target)
        else:  # 타겟이 있는데 다른 카드거나 카드가 없는 경우 계속 탐색
            for i in range(4):
                dfs(board, i, cost + 1, ny, nx, target, copy.deepcopy(isvisited), total)
                ctrl(board, i, cost + 1, ny, nx, target, copy.deepcopy(isvisited), total)

    return answer


b = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
print(solution(b, 1, 0))
