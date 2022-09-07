import heapq

blen = 0


def check(x, y):
    return 0 <= x < blen and 0 <= y < blen


def solution(board):
    # 상하좌우 4방향
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    INF = 987654321
    global blen
    blen = len(board)
    # (y,x)
    # 로봇 시작 지점
    robot_pos = [(0, 0), (0, 1)]
    q = []
    heapq.heappush(q, [0, robot_pos])
    distance = [[INF] * (blen * blen) for _ in range(blen * blen)]
    distance[0][1] = 0
    while q:
        cost, robot = heapq.heappop(q)
        r1, r2 = robot
        if distance[r1[0] * blen + r1[1]][r2[0] * blen + r2[1]] < cost:
            continue

        # 상하좌우의 경우
        for d in delta:
            nr1_y, nr1_x = r1[0] + d[0], r1[1] + d[1]
            nr2_y, nr2_x = r2[0] + d[0], r2[1] + d[1]
            # 맵 밖을 벗어나면
            if not check(nr1_x, nr1_y) or not check(nr2_x, nr2_y):
                continue

            # 움직이지 못하는 경우
            if board[nr1_y][nr1_x] == 1 or board[nr2_y][nr2_x] == 1:
                continue

            n_robot = [(nr1_y, nr1_x), (nr2_y, nr2_x)]
            # 더 짧을 경우, 이동하는 것 추가.
            if distance[nr1_y * blen + nr1_x][nr2_y * blen + nr2_x] > cost + 1:
                distance[nr1_y * blen + nr1_x][nr2_y * blen + nr2_x] = cost + 1
                heapq.heappush(q, [cost + 1, n_robot])

        # y좌표가 같은 경우 -> 가로 일 때
        if r1[0] == r2[0]:
            # 왼쪽이 아래로 가는 경우
            nr1_y, nr1_x = r1[0] + 1, r1[1] + 1
            if check(nr1_x, nr1_y) and board[r1[0] + 1][r1[1]] == 0 and board[nr1_y][nr1_x] == 0:
                if distance[r2[0] * blen + r2[1]][nr1_y * blen + nr1_x] > cost + 1:
                    distance[r2[0] * blen + r2[1]][nr1_y * blen + nr1_x] = cost + 1
                    heapq.heappush(q, [cost + 1, [(r2[0], r2[1]), (nr1_y, nr1_x)]])

            # 왼쪽이 위로 가는 경우
            nr1_y, nr1_x = r1[0] - 1, r1[1] + 1
            if check(nr1_x, nr1_y) and board[r1[0] - 1][r1[1]] == 0 and board[nr1_y][nr1_x] == 0:
                if distance[nr1_y * blen + nr1_x][r2[0] * blen + r2[1]] > cost + 1:
                    distance[nr1_y * blen + nr1_x][r2[0] * blen + r2[1]] = cost + 1
                    heapq.heappush(q, [cost + 1, [(nr1_y, nr1_x), (r2[0], r2[1])]])

            # 오른쪽이 아래로 가는 경우
            nr2_y, nr2_x = r2[0] + 1, r2[1] - 1
            if check(nr2_x, nr2_y) and board[r2[0] + 1][r2[1]] == 0 and board[nr2_y][nr2_x] == 0:
                if distance[r1[0] * blen + r1[1]][nr2_y * blen + nr2_x] > cost + 1:
                    distance[r1[0] * blen + r1[1]][nr2_y * blen + nr2_x] = cost + 1
                    heapq.heappush(q, [cost + 1, [(r1[0], r1[1]), (nr2_y, nr2_x)]])

            # 오른쪽이 위로 가는 경우
            nr2_y, nr2_x = r2[0] - 1, r2[1] - 1
            if check(nr2_x, nr2_y) and board[r2[0] - 1][r2[1]] == 0 and board[nr2_y][nr2_x] == 0:
                if distance[nr2_y * blen + nr2_x][r1[0] * blen + r1[1]] > cost + 1:
                    distance[nr2_y * blen + nr2_x][r1[0] * blen + r1[1]] = cost + 1
                    heapq.heappush(q, [cost + 1, [(nr2_y, nr2_x), (r1[0], r1[1])]])

        else:
            # 위에가 왼쪽으로 가는 경우
            nr1_y, nr1_x = r1[0] + 1, r1[1] - 1
            if check(nr1_x, nr1_y) and board[r1[0]][r1[1] - 1] == 0 and board[nr1_y][nr1_x] == 0:
                if distance[nr1_y * blen + nr1_x][r2[0] * blen + r2[1]] > cost + 1:
                    distance[nr1_y * blen + nr1_x][r2[0] * blen + r2[1]] = cost + 1
                    heapq.heappush(q, [cost + 1, [(nr1_y, nr1_x), (r2[0], r2[1])]])

            # 위에가 오른쪽으로 가는 경우
            nr1_y, nr1_x = r1[0] + 1, r1[1] + 1
            if check(nr1_x, nr1_y) and board[r1[0]][r1[1] + 1] == 0 and board[nr1_y][nr1_x] == 0:
                if distance[r2[0] * blen + r2[1]][nr1_y * blen + nr1_x] > cost + 1:
                    distance[r2[0] * blen + r2[1]][nr1_y * blen + nr1_x] = cost + 1
                    heapq.heappush(q, [cost + 1, [(r2[0], r2[1]), (nr1_y, nr1_x)]])

            # 아래가 왼쪽으로 가는 경우
            nr2_y, nr2_x = r2[0] - 1, r2[1] - 1
            if check(nr2_x, nr2_y) and board[r2[0]][r2[1] - 1] == 0 and board[nr2_y][nr2_x] == 0:
                if distance[nr2_y * blen + nr2_x][r1[0] * blen + r1[1]] > cost + 1:
                    distance[nr2_y * blen + nr2_x][r1[0] * blen + r1[1]] = cost + 1
                    heapq.heappush(q, [cost + 1, [(nr2_y, nr2_x), (r1[0], r1[1])]])

            nr2_y, nr2_x = r2[0] - 1, r2[1] + 1
            if check(nr2_x, nr2_y) and board[r2[0]][r2[1] + 1] == 0 and board[nr2_y][nr2_x] == 0:
                if distance[r1[0] * blen + r1[1]][nr2_y * blen + nr2_x] > cost + 1:
                    distance[r1[0] * blen + r1[1]][nr2_y * blen + nr2_x] = cost + 1
                    heapq.heappush(q, [cost + 1, [(r1[0], r1[1]), (nr2_y, nr2_x)]])

    answer = min(distance[blen * (blen - 1) + blen - 2][blen * (blen - 1) + blen - 1],
                 distance[blen * (blen - 2) + blen - 1][blen * (blen - 1) + blen - 1])

    return answer