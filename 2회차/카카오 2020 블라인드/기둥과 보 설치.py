# 기둥 조건
# 1. 바닥 위이거나
# 2. 보의 한쪽 끝 부분 이거나
# 3. 다른 기둥 위에 있어야 한다.
def check_tower(tower, bo, x, y):
    # 1번 조건
    if y == 0:
        return True

    # 2번 조건
    if bo[y][x] == 1:
        return True
    elif x > 0 and bo[y][x-1] == 1:
        return True

    # 3번 조건
    if tower[y-1][x] == 0:
        return True

    return False

# 보 조건
# 1. 한쪽 끝 부분이 기둥 위에 있거나
# 2. 양쪽 끝 부분이 다른 보와 동시에 연결
def check_bo(tower, bo, x, y):
    # 1번 조건
    if tower[y-1][x] == 0 or tower[y-1][x+1] == 0:
        return True

    # 1번 조건이 안되는데 양쪽 벽면과 맞닿게 설치할 수 없음
    if x == 0 or x == len(tower):
        return False

    # 2번 조건
    if bo[y][x-1] == 1 and bo[y][x+1] == 1:
        return True

    return False


def solution(n, build_frame):
    tower = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    bo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    for x,y,a,b in build_frame:
        if b == 1: # 설치
            if a == 0 and check_tower(tower, bo, x, y):
                print("기둥 설치. X : ", x, "Y : ", y)
                tower[y][x] = 0
            elif a == 1 and check_bo(tower,bo, x, y):
                print("보 설치. X : ", x, "Y : ", y)
                bo[y][x] = 1
        elif b == 0:    # 삭제
            if a == 0:  # 기둥을 삭제하는 경우, 기둥 위에 기둥이나 보가 내가 없어도 되는지 확인
                tower[y][x] = -1
                if y < n and tower[y+1][x] == 0 and not check_tower(tower,bo,x,y+1):  # 기둥 위에 기둥이 있던 경우
                    tower[y][x] = 0
                    continue

                if x > 0 and bo[y+1][x-1] == 1 and not check_bo(tower,bo,x-1,y+1):
                    tower[y][x] = 0
                    continue

                if bo[y+1][x] == 1 and not check_bo(tower,bo, x, y+1):
                    tower[y][x] = 0
                    continue
            elif a == 1: # 보를 삭제하는 경우, 양쪽 끝에 보나 기둥이 있을 때 내가 없어도 되는 지 확인
                bo[y][x] = - 1
                # 기둥이 있는 경우
                if y < n and tower[y][x] == 0 and not check_tower(tower,bo, x, y):
                    bo[y][x] = 1
                    continue

                if y < n and tower[y][x+1] == 0 and not check_tower(tower,bo, x+1, y):
                    bo[y][x] = 1
                    continue

                if x > 0 and bo[y][x-1] == 1 and not check_bo(tower,bo, x-1, y):
                    bo[y][x] = 1
                    continue

                if x < n and bo[y][x+1] == 1 and not check_bo(tower,bo, x+1, y):
                    bo[y][x] = 1
                    continue


    answer = []
    for y in range(n+1):
        for x in range(n+1):
            if bo[y][x] != -1 :
                answer.append([x,y,bo[y][x]])

            if tower[y][x] != -1:
                answer.append([x,y,tower[y][x]])

    answer.sort()
    return answer


FRAME = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
solution(5,FRAME)
