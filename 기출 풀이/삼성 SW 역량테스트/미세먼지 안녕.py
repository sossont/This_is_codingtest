
# 1. 미세먼지 확산, 모든 칸에서 동시에 일어난다. 인접한 네 방향

# 2. 공기 청정기 작동
# 공기청정기는 항상 1번 열, 크기는 두 행이다.
# 공기 청정기는 두 행 짜리니까, 윗행은 반 시계 방향, 아랫행은 시계 방향으로 순환
# 27분 컷

R,C,T = map(int,input().split())
machine = []
room = []
for _ in range(R):
    room.append(list(map(int,input().split())))

for yy in range(R):
    for xx in range(C):
        if room[yy][xx] == -1:
            machine.append([yy,xx])
            break

# 맵 안에 있는가

def check(x,y):
    if 0<=x<C and 0<=y<R:
        return True

    return False


# 미세먼지 확산하는 함수
def dust():
    global room
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    temp = []
    for y in range(R):
        for x in range(C):
            # 공기청정기는 따지지 않는다.
            if room[y][x] == -1:
                continue

            count = 0 # 확산된 방향의 개수
            value = room[y][x] // 5 # 확산되는 양
            for d in delta:
                ny = y + d[0]
                nx = x + d[1]
                if not check(nx,ny):
                    continue

                # 인접한 칸이 공기청정기 인 경우
                if room[ny][nx] == -1:
                    continue

                count += 1
                temp.append([ny,nx,value])

            if count == 0:
                continue
            else:
                room[y][x] -= value * count

    while temp:
        y,x,v = temp.pop()
        room[y][x] += v


def wind():
    global machine
    up_y = machine[0][0] # 위쪽 공기 청정기 y,x 좌표
    up_x = machine[0][1]
    down_y = machine[1][0]
    down_x = machine[1][1]

    cur_x = up_x + 1
    cur_y = up_y
    # 첫 번째 공기는 미세먼지 0이다.
    bef = room[cur_y][cur_x]
    room[cur_y][cur_x] = 0

    for dx in range(2,C):
        cur_x += 1
        tmp = room[cur_y][cur_x]
        room[cur_y][cur_x] = bef
        bef = tmp

    # 오른쪽 끝에 도달함
    for dy in range(up_y):
        cur_y -= 1
        tmp = room[cur_y][cur_x]
        room[cur_y][cur_x] = bef
        bef = tmp

    # 오른쪽 위에 끝에 도달함
    for dx in range(1,C):
        cur_x -= 1
        tmp = room[cur_y][cur_x]
        room[cur_y][cur_x] = bef
        bef = tmp

    for dy in range(up_y):
        cur_y += 1
        if cur_y == up_y:
            break
        tmp = room[cur_y][cur_x]
        room[cur_y][cur_x] = bef
        bef = tmp

    # --- 이제 아래쪽 ---
    cur_x = down_x + 1
    cur_y = down_y
    # 첫 번째 공기는 미세먼지 0이다.
    bef = room[cur_y][cur_x]
    room[cur_y][cur_x] = 0
    for dx in range(2,C):
        cur_x += 1
        tmp = room[cur_y][cur_x]
        room[cur_y][cur_x] = bef
        bef = tmp

    # 오른쪽 끝에 도달함
    for dy in range(R-1-down_y):
        cur_y += 1
        tmp = room[cur_y][cur_x]
        room[cur_y][cur_x] = bef
        bef = tmp

    # 오른쪽 아래 끝에 도달함
    for dx in range(1,C):
        cur_x -= 1
        tmp = room[cur_y][cur_x]
        room[cur_y][cur_x] = bef
        bef = tmp

    for dy in range(R-1-down_y):
        cur_y -= 1
        if cur_y == down_y:
            break
        tmp = room[cur_y][cur_x]
        room[cur_y][cur_x] = bef
        bef = tmp


while T>0:
    dust()
    wind()
    T -=1

answer = 0
for y in range(R):
    for x in range(C):
        if room[y][x] == -1:
            continue
        answer += room[y][x]

print(answer)
