# 기둥이 설치 가능한 경우
# 1. 내 아래 기둥이 있다. 2. 내 아래 보가 있다. 3. 내 아래가 바닥이다.

def check_tower(bo,tower,x,y): # 이 (x,y) 좌표에 타워가 설 수 있는지.
    if y == 2:  # y = 2이면, 아래가 바닥이므로 참이다.
        return True

    if tower[y-1][x] == 1:  # 아래에 기둥이 있으므로 세울 수 있다.
        return True

    if bo[y][x] == 1 or bo[y][x-1] == 1:    #아래에 보가 있다.
        return True

    return False

# 보가 설치 가능한 경우
# 1. 왼쪽 아래에 기둥이 있다. 2, 오른쪽 아래에 기둥이 있다. 3. 양 옆에 보가 있다.
def check_bo(bo,tower,x,y): # 이 (x,y) 좌표에 보가 설 수 있는지.
    if tower[y-1][x] == 1:  # Case 1
        return True

    if tower[y-1][x+1] == 1:    # Case 2
        return True

    if bo[y][x-1] == 1 and bo[y][x+1] == 1: # Case 3
        return True

    return False

# 타워를 삭제할 수 있는 경우
# 1. 위에 타워가 있는 경우, 타워가 서있을 수 있어야 한다.
# 2. 위에 보가 있는 경우, 보가 서있을 수 있어야 한다.


def solution(n, build_frame):
    answer = []
    bo = [[0 for _ in range(n + 4)] for _ in range(n + 4)]
    tower = [[0 for _ in range(n + 4)] for _ in range(n + 4)]

    # 좌표를 2씩 더해서, -2 +2 연산을 자유롭게 하자.
    # 기둥의 경우를 y 좌표를 세로 직선으로 하자.
    # 보는 x좌표를 가로 직선으로 하자

    for frame in build_frame:
        x = frame[0] + 2
        y = frame[1] + 2
        a = frame[2]
        b = frame[3]

        if b == 1:  # 설치하는 경우
            if a == 0 and check_tower(bo,tower,x,y): #기둥인 경우
                tower[y][x] = 1
            elif a == 1 and check_bo(bo,tower,x,y): # 보인 경우
                bo[y][x] = 1

        else:   # 삭제하는 경우
            if a == 0:  # 타워을 삭제하는 경우
                tower[y][x] = 0 # 일단 삭제해본다.
                if tower[y+1][x] == 1 and not check_tower(bo,tower,x,y+1):  # 위에 타워가 있는 경우
                    tower[y][x] = 1 # 삭제 못함
                    continue

                if bo[y+1][x] == 1 and not check_bo(bo, tower, x, y+1):# 위에 보가 오른쪽으로 있는 경우
                    tower[y][x] = 1  # 삭제 못함
                    continue

                if bo[y+1][x-1] == 1 and not check_bo(bo, tower, x-1, y+1):  # 보가 왼쪽으로 있는 경우
                    tower[y][x] = 1  # 삭제 못함
                    continue
            elif a == 1:    #보를 삭제하는 경우
                bo[y][x] = 0    # 일단 삭제한다.
                if tower[y][x] == 1 and not check_tower(bo,tower,x, y): # 왼쪽 위에 타워가 있는 경우
                    bo[y][x] = 1
                    continue

                if tower[y][x+1] == 1 and not check_tower(bo,tower,x+1,y):  # 오른쪽 위에 타워가 있는 경우
                    bo[y][x] = 1
                    continue

                if bo[y][x-1] == 1 and not check_bo(bo,tower,x-1,y):
                    bo[y][x] = 1
                    continue

                if bo[y][x+1] == 1 and not check_bo(bo,tower,x+1,y):
                    bo[y][x] = 1
                    continue

    for x in range(2, len(bo)):
        for y in range(2, len(bo)):
            if tower[y][x] == 1:
                answer.append([x - 2, y - 2, 0])

            if bo[y][x] == 1:
                answer.append([x - 2, y - 2, 1])

    return answer

