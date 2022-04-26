## ----- 테케는 다 통과하는데 틀리는 코드 -----

# (x,y)의 온도가 k만큼 상승하면,
# (x-1,y+1), (x,y+1), (x,y+1), (x+1,y+1)의 온도도 k-1만큼 상승
# 한 번 바람이 도착해서 온도가 상승하면 다른 바람에는 영향 x


R, C, K = map(int, input().split())

room = []
machine = []
surv = []
for _ in range(R):
    room.append(list(map(int, input().split())))

for i in range(R):
    for j in range(C):
        if room[i][j] == 0:
            continue

        if room[i][j] == 5:  # 조사해야하는 방의 온도 좌표 저장
            surv.append([i, j])
            room[i][j] = 0
        else:  # 온풍기 좌표와 방향 저장
            machine.append([i, j, room[i][j]])
            room[i][j] = 0

W = int(input())

wall = [[[] for _ in range(C)] for _ in range(R)]

def check(xpos, ypos):
    if 0 <= xpos < R and 0 <= ypos < C:
        return True

    return False
# 왼 위 오 아 -> 0,1,2,3 벽
for _ in range(W):
    x, y, t = map(int, input().split())
    if t == 0:
        if check(x-1,y-1):
            wall[x - 1][y - 1].append(1)
            if check(x-2,y-1):
                wall[x - 2][y - 1].append(3)
    elif t == 1:
        if check(x-1,y-1):
            wall[x - 1][y - 1].append(2)
        if check(x-1,y):
            wall[x - 1][y].append(0)


# 온풍기와 벽 입력 다 완료




def left(xx, yy):
    global room
    isvisited = [[False] * C for _ in range(R)]  # 바람이 지나간곳 체크
    room[xx][yy - 1] += 5  # 온풍기 바로 오른쪽 온도 증가
    temp = 4
    isvisited[xx][yy - 1] = True
    for dy in range(1, 5):  #
        cur_y = yy - dy
        ny = cur_y - 1

        # 더 이상 왼쪽으로 못감
        if not check(xx, ny):
            break

        for dx in range(dy):
            cur_x = xx - dx
            if check(cur_x, cur_y):
                # ---- 위로 이동 ----
                # 현재칸 기준으로 바람 이동시키는 건데, 현재 칸이 바람 없으면 탐색 x
                if not isvisited[cur_x][cur_y]:
                    continue

                # 바로 왼쪽 칸 먼저 확인
                if 0 not in wall[cur_x][cur_y] and not isvisited[cur_x][ny]:
                    # 바람이 자나갈 수 있으므로 온도 증가.
                    isvisited[cur_x][ny] = True
                    room[cur_x][ny] += temp

                # 왼쪽 위에 한칸
                if check(cur_x - 1, ny):
                    if 1 not in wall[cur_x][cur_y] and 0 not in wall[cur_x - 1][cur_y] and not isvisited[cur_x - 1][ny]:
                        isvisited[cur_x - 1][ny] = True
                        room[cur_x - 1][ny] += temp

                # 왼쪽 아래 한칸
                if check(cur_x + 1, ny):
                    if 3 not in wall[cur_x][cur_y] and 0 not in wall[cur_x + 1][cur_y] and not isvisited[cur_x + 1][ny]:
                        isvisited[cur_x + 1][ny] = True
                        room[cur_x + 1][ny] += temp

            # ---- 아래로 이동 ----
            cur_x = xx + dx
            if check(cur_x, cur_y):
                # 현재칸 기준으로 바람 이동시키는 건데, 현재 칸이 바람 없으면 탐색 x
                if not isvisited[cur_x][cur_y]:
                    continue

                # 바로 왼쪽 칸 먼저 확인
                if 0 not in wall[cur_x][cur_y] and not isvisited[cur_x][ny]:
                    # 바람이 자나갈 수 있으므로 온도 증가.
                    isvisited[cur_x][ny] = True
                    room[cur_x][ny] += temp

                # 왼쪽 위에 한칸
                if check(cur_x - 1, ny):
                    if 1 not in wall[cur_x][cur_y] and 0 not in wall[cur_x - 1][cur_y] and not isvisited[cur_x - 1][
                        ny]:
                        isvisited[cur_x - 1][ny] = True
                        room[cur_x - 1][ny] += temp

                # 왼쪽 아래 한칸
                if check(cur_x + 1, ny):
                    if 3 not in wall[cur_x][cur_y] and 0 not in wall[cur_x + 1][cur_y] and not isvisited[cur_x + 1][
                        ny]:
                        isvisited[cur_x + 1][ny] = True
                        room[cur_x + 1][ny] += temp

        temp -= 1


# 오른쪽으로 바람 부는 것
def right(xx, yy):
    global room
    isvisited = [[False] * C for _ in range(R)]  # 바람이 지나간곳 체크
    room[xx][yy + 1] += 5  # 온풍기 바로 오른쪽 온도 증가
    temp = 4  # 증가하는 온도
    isvisited[xx][yy + 1] = True
    for dy in range(1, 5):  #
        cur_y = yy + dy
        ny = cur_y + 1

        # 더 이상 오른쪽으로 못감
        if not check(xx, ny):
            break

        for dx in range(dy):
            cur_x = xx - dx
            # ---- 위로 이동 ----
            # 현재칸 기준으로 바람 이동시키는 건데, 현재 칸이 바람 없으면 탐색 x
            if check(cur_x, cur_y):
                if not isvisited[cur_x][cur_y]:
                    continue

                # 바로 오른쪽칸 먼저 확인
                if 2 not in wall[cur_x][cur_y] and not isvisited[cur_x][ny]:
                    # 바람이 자나갈 수 있으므로 온도 증가.
                    isvisited[cur_x][ny] = True
                    room[cur_x][ny] += temp

                # 오른쪽 위에 한칸
                if check(cur_x - 1, ny):
                    if 1 not in wall[cur_x][cur_y] and 2 not in wall[cur_x - 1][cur_y] and not isvisited[cur_x - 1][ny]:
                        isvisited[cur_x - 1][ny] = True
                        room[cur_x - 1][ny] += temp

                # 오른쪽 아래 한칸
                if check(cur_x + 1, ny):
                    if 3 not in wall[cur_x][cur_y] and 2 not in wall[cur_x + 1][cur_y] and not isvisited[cur_x + 1][ny]:
                        isvisited[cur_x + 1][ny] = True
                        room[cur_x + 1][ny] += temp

            # ---- 아래로 이동 ----
            cur_x = xx + dx

            if check(cur_x, cur_y):
                # 현재칸 기준으로 바람 이동시키는 건데, 현재 칸이 바람 없으면 탐색 x
                if not isvisited[cur_x][cur_y]:
                    continue

                # 바로 옆칸 먼저 확인
                if 2 not in wall[cur_x][cur_y] and not isvisited[cur_x][ny]:
                    # 바람이 자나갈 수 있으므로 온도 증가.
                    isvisited[cur_x][ny] = True
                    room[cur_x][ny] += temp

                # 오른쪽 위에 한칸
                if check(cur_x - 1, ny):
                    if 1 not in wall[cur_x][cur_y] and 2 not in wall[cur_x - 1][cur_y] and not isvisited[cur_x - 1][
                        ny]:
                        isvisited[cur_x - 1][ny] = True
                        room[cur_x - 1][ny] += temp

                # 오른쪽 아래 한칸
                if check(cur_x + 1, ny):
                    if 3 not in wall[cur_x][cur_y] and 2 not in wall[cur_x + 1][cur_y] and not isvisited[cur_x + 1][
                        ny]:
                        isvisited[cur_x + 1][ny] = True
                        room[cur_x + 1][ny] += temp

        temp -= 1

def down(xx, yy):
    global room
    isvisited = [[False for _ in range(C)] for _ in range(R)]  # 바람이 지나간곳 체크
    room[xx + 1][yy] += 5  # 온풍기 바로 아래쪽 온도 증가
    temp = 4  # 증가하는 온도
    isvisited[xx + 1][yy] = True
    for dx in range(1, 5):  #
        cur_x = xx + dx
        nx = cur_x + 1

        # 더 이상 아래쪽으로 못감
        if not check(nx, yy):
            break

        for dy in range(dx):
            # --- 왼쪽 ---
            cur_y = yy - dy
            if check(cur_x, cur_y):
                if not isvisited[cur_x][cur_y]:
                    continue

                # 바로 아래
                if 3 not in wall[cur_x][cur_y] and not isvisited[nx][cur_y]:
                    isvisited[nx][cur_y] = True
                    room[nx][cur_y] += temp

                # 왼쪽 한칸
                if check(nx, cur_y - 1):
                    if 0 not in wall[cur_x][cur_y] and not 3 in wall[cur_x][cur_y - 1] and not isvisited[nx][cur_y - 1]:
                        isvisited[nx][cur_y - 1] = True
                        room[nx][cur_y - 1] += temp

                # 오른쪽 한칸
                if check(nx, cur_y + 1):
                    if 2 not in wall[cur_x][cur_y] and 3 not in wall[cur_x][cur_y + 1] and not isvisited[nx][
                        cur_y + 1]:
                        isvisited[nx][cur_y + 1] = True
                        room[nx][cur_y + 1] += temp

            # --- 오른쪽 ---
            cur_y = yy + dy

            if check(cur_x, cur_y):
                if not isvisited[cur_x][cur_y]:
                    continue

                # 바로 아래
                if 3 not in wall[cur_x][cur_y] and not isvisited[nx][cur_y]:
                    isvisited[nx][cur_y] = True
                    room[nx][cur_y] += temp

                # 오른쪽 한칸
                if check(nx, cur_y + 1):
                    if 2 not in wall[cur_x][cur_y] and 3 not in wall[cur_x][cur_y + 1] and not isvisited[nx][cur_y + 1]:
                        isvisited[nx][cur_y + 1] = True
                        room[nx][cur_y + 1] += temp

                # 왼쪽 한칸
                if check(nx, cur_y - 1):
                    if 0 not in wall[cur_x][cur_y] and not 3 in wall[cur_x][cur_y - 1] and not isvisited[nx][
                        cur_y - 1]:
                        isvisited[nx][cur_y - 1] = True
                        room[nx][cur_y - 1] += temp

        temp -= 1


# 위로 바람분다.
def up(xx, yy):
    global room
    isvisited = [[False] * C for _ in range(R)]  # 바람이 지나간곳 체크
    room[xx - 1][yy] += 5  # 온풍기 바로 위쪽 온도 증가
    temp = 4  # 증가하는 온도
    isvisited[xx - 1][yy] = True
    for dx in range(1, 5):  #
        cur_x = xx - dx
        nx = cur_x - 1

        # 더 이상 위쪽으로 못감
        if not check(nx, yy):
            break

        for dy in range(dx):
            # --- 왼쪽 ---
            cur_y = yy - dy

            if check(cur_x, cur_y):
                if not isvisited[cur_x][cur_y]:
                    continue
                # 바로 위
                if 1 not in wall[cur_x][cur_y] and not isvisited[nx][cur_y]:
                    isvisited[nx][cur_y] = True
                    room[nx][cur_y] += temp

                # 위 + 왼쪽 한칸
                if check(nx, cur_y - 1):
                    if 0 not in wall[cur_x][cur_y] and 1 not in wall[cur_x][cur_y - 1] and not isvisited[nx][cur_y - 1]:
                        isvisited[nx][cur_y - 1] = True
                        room[nx][cur_y - 1] += temp

                # 위 + 오른쪽 한칸
                if check(nx, cur_y + 1):
                    if 2 not in wall[cur_x][cur_y] and 1 not in wall[cur_x][cur_y + 1] and not isvisited[nx][
                        cur_y + 1]:
                        isvisited[nx][cur_y + 1] = True
                        room[nx][cur_y + 1] += temp

            # --- 오른쪽 ---
            cur_y = yy + dy

            if check(cur_x, cur_y):
                if not isvisited[cur_x][cur_y]:
                    continue

                # 바로 위
                if 1 not in wall[cur_x][cur_y] and not isvisited[nx][cur_y]:
                    isvisited[nx][cur_y] = True
                    room[nx][cur_y] += temp

                # 위 + 왼쪽 한칸
                if check(nx, cur_y - 1):
                    if 0 not in wall[cur_x][cur_y] and 1 not in wall[cur_x][cur_y - 1] and not isvisited[nx][
                        cur_y - 1]:
                        isvisited[nx][cur_y - 1] = True
                        room[nx][cur_y - 1] += temp

                # 오른쪽 한칸
                if check(nx, cur_y + 1):
                    if 2 not in wall[cur_x][cur_y] and 1 not in wall[cur_x][cur_y + 1] and not isvisited[nx][cur_y + 1]:
                        isvisited[nx][cur_y + 1] = True
                        room[nx][cur_y + 1] += temp

        temp -= 1


def adjust():
    delta = [[-1, 0], [0, -1], [1,0], [0,1]]  # 왼쪽위부터 오른쪽아래로 탐색
    q = []
    global room
    for xx in range(R):
        for yy in range(C):
            for k in range(len(delta)):
                ny = yy + delta[k][0]
                nx = xx + delta[k][1]
                if not check(nx,ny):
                    continue

                if k in wall[xx][yy]:
                    continue

                if room[xx][yy] >= room[nx][ny]:
                    value = (room[xx][yy] - room[nx][ny]) // 4
                    if value == 0:
                        continue
                    q.append([xx,yy,-value])
                else:
                    value = (room[nx][ny] - room[xx][yy]) // 4
                    if value == 0:
                        continue
                    q.append([xx,yy,value])

    while q:
        xx, yy, v = q.pop()
        room[xx][yy] += v

# 바깥쪽 온도조절
def out():
    for yy in range(C):
        if room[0][yy] > 0:
            room[0][yy] -= 1

        if room[R - 1][yy] > 0:
            room[R - 1][yy] -= 1

    for xx in range(1, R - 1):
        if room[xx][0] > 0:
            room[xx][0] -= 1

        if room[xx][C - 1] > 0:
            room[xx][C - 1] -= 1


# 온풍기에서 바람이 나온다.

answer = 0
while True:
    answer += 1
    for mac in machine:
        x, y, d = mac  # 온풍기 x,y좌표와 방향
        k = 5
        if d == 1:  # 방향이 오른쪽인 경우
            right(x, y)
        elif d == 2:
            left(x, y)
        elif d == 3:
            up(x, y)
        elif d == 4:
            down(x, y)

    adjust()
    out()
    flag = True
    for sur in surv:
        surx, sury = sur
        if room[surx][sury] < K:
            flag = False
            break
    if flag:
        break

    if answer > 100:
        break

if answer > 100:
    answer = 101

'''
7 8 5
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 2
0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
3
4 4 1
5 4 0
5 6 0
'''
print(answer)
