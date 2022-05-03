green_block = [[0] * 4 for _ in range(6)]
blue_block = [[0]*6 for _ in range(4)]
answer = 0
# 점수 나는 일 없는 지 확인
def check_green():
    global answer
    global green_block

    push_count = 0
    for xx in range(2,6):
        flag = True
        for yy in range(4):
            # 점수 날 일이 없는 경우
            if green_block[xx][yy] == 0:
                flag = False
                break

        # 점수 나는 경우 한줄을 다 비워주고 점수 추가
        if flag:
            for yy in range(4):
                green_block[xx][yy] = 0
            answer += 1
            push_count += 1
    push_green(push_count)
    # 연한 칸에 블록이 있는 경우
    special_count = 0
    for xx in range(2):
        for yy in range(4):
            if green_block[xx][yy] != 0:
                special_count += 1
                push_count += 1
                break

    for dx in range(special_count):
        for yy in range(4):
            # 연한 칸에 블록이 있는 행만큼 비워준다.
            green_block[5-dx][yy] = 0

    push_green(special_count)

# 체크 다 끝났으면, 바닥으로 모든 블록 밀어주기
def push_green(count):
    for _ in range(count):
        for dx in range(5,0,-1):
            flag = True
            for dy in range(4):
                if green_block[dx][dy] != 0:
                    flag = False
                    break

            if flag:
            # 만약 바닥이 비어서 미루는 경우, 위 아래를 바꿔준다.
                for dy in range(4):
                    green_block[dx][dy], green_block[dx-1][dy] = green_block[dx-1][dy], green_block[dx][dy]


def green(y,tt):
    global green_block
    if tt == 1: # 1*1 블록을 x,y에 놓은 경우
        green_block[0][y] = 1
        cx = 0
        for _ in range(1,6):
            nx = cx + 1
            # 블록이나 끝에 닿을 때까지 한 칸씩 밀기
            if green_block[nx][y] == 0:
                green_block[cx][y], green_block[nx][y] = 0, 1
            else:
                break
            cx += 1

    elif tt == 2:   # 1*2 블록
        green_block[0][y], green_block[0][y+1] = 1,1
        cx = 0
        for _ in range(1,6):
            nx = cx + 1
            if green_block[nx][y] == 0 and green_block[nx][y+1] == 0:
                green_block[cx][y], green_block[nx][y] = 0, 1
                green_block[cx][y+1], green_block[nx][y+1] = 0, 1
            else:
                break

            cx += 1
    else:   # 2*1 블록
        green_block[0][y], green_block[1][y] = 1,1
        cx = 1
        for _ in range(4):
            nx = cx + 1
            if green_block[nx][y] == 0:
                green_block[nx][y], green_block[cx][y] = 1,1
                green_block[cx-1][y] = 0
            else:
                break
            cx += 1
    check_green()

def blue(x,tt):
    global blue_block
    # 오른쪽으로 갈 수 있을 때 까지 쭉쭉
    if tt == 1:
        blue_block[x][0] = 1
        cy = 0
        for _ in range(5):
            ny = cy + 1
            if blue_block[x][ny] == 0:
                blue_block[x][ny], blue_block[x][cy] = 1,0
            else:
                break
            cy += 1

    elif tt == 2:
        blue_block[x][0] = 1
        blue_block[x][1] = 1
        cy = 1
        for _ in range(4):
            ny = cy + 1
            if blue_block[x][ny] == 0:
                blue_block[x][ny], blue_block[x][cy-1] = 1,0
            else:
                break
            cy += 1

    else:
        blue_block[x][0],blue_block[x+1][0] = 1,1
        cy = 0
        for _ in range(5):
            ny = cy + 1
            if blue_block[x][ny] == 0 and blue_block[x+1][ny] == 0:
                blue_block[x][ny], blue_block[x][cy] = 1, 0
                blue_block[x+1][ny], blue_block[x+1][cy] = 1, 0
            else:
                break
            cy += 1

    check_blue()


def check_blue():
    global blue_block
    global answer

    push_count = 0
    for yy in range(2,6):
        flag = True
        for xx in range(4):
            if blue_block[xx][yy] == 0:
                flag = False
                break
        # 점수 나는 경우
        if flag:
            for xx in range(4):
                blue_block[xx][yy] = 0
            answer += 1
            push_count += 1
    push_blue(push_count)
    special_count = 0
    # 연한 칸에 블록이 있는 경우
    for yy in range(2):
        for xx in range(4):
            if blue_block[xx][yy] != 0:
                special_count += 1
                push_count += 1
                break

    for dy in range(special_count):
        for xx in range(4):
            blue_block[xx][5-dy] = 0

    push_blue(special_count)


def push_blue(count):
    global blue_block

    for _ in range(count):
        for yy in range(5,0,-1):
            flag = True
            for xx in range(4):
                # 비어있지 않아서 못바꾸는 칸
                if blue_block[xx][yy] != 0:
                    flag = False
                    break

            if flag:
                for xx in range(4):
                    blue_block[xx][yy], blue_block[xx][yy-1] = blue_block[xx][yy-1], blue_block[xx][yy]

N = int(input())
for _ in range(N):
    t,ix,iy = map(int,input().split())
    green(iy,t)
    blue(ix,t)

print(answer)
bc = 0
for kx in range(6):
    for ky in range(4):
        if green_block[kx][ky] != 0:
            bc += 1

        if blue_block[ky][kx] != 0:
            bc += 1

print(bc)