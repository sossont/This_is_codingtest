# 해맸던 이유 : 상어가 갔던 곳을 재방문하는 경우를 나는 생각을 못했었다.
# 그리고 깔끔하게 배열 이용해서 풀면되는데, 번호 매기는 이상한 방법을 생각해버림,,

import heapq

# 가장 왼쪽위는 (1,1) 오른쪽 아래 (4,4)
# 물고기 M마리
# 이동방향 : 8가지 방향

# 0. 복제 마법 시전. (물고기 현재 저장해뒀다가, 나중에 생성한다.)
# 1. 모든 물고기 한 칸 이동.  물고기들은 이동할 수 있을 때 까지 45도 회전, 이동할 수 있는 칸이 없으면 이동 x
# 물고기가 이동할 수 없는 칸 :
# 1) 격자의 범위를 벗어나는 칸
# 2) 상어가 있는 칸
# 3) 물고기의 냄새가 있는 칸


# 2. 상어가 현재 칸에서 상하좌우 인접한 칸으로 3칸 이동한다. 물고기 만나면 물고기 아웃 그리고 냄새를 남긴다.
# 3. 두 번 전 연습에서 생긴 물고기 냄새가 사라진다.
# 4. 0번에서 시전한 복제가 완료되어서, 복제한 위치와 방향을 그대로 붙여넣는다.

# 1부터 순서대로 반시계 방향  (y,x)
delta = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
M, S = map(int, input().split())

graph = [[[] for _ in range(5)] for _ in range(5)]  # graph[y][x] : 이 칸에 들어있는 물고기 번호 집합

# 상어가 움직일 수 있는 모든 경우의 수. 상 좌 하 우 순서. (y,x)
dir_list = [(0, -1), (-1, 0), (0, 1), (1, 0)]
shark_case = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            shark_case.append([dir_list[i], dir_list[j], dir_list[k]])


# 맵 벗어나는지 확인하는 함수
def check(check_x, check_y):
    if 1 <= check_x <= 4 and 1 <= check_y <= 4:
        return True

    return False


fish_smell = [[0] * 5 for _ in range(5)]  # 이 칸에 물고기 냄새가 몇턴 전에 있던 냄새인지.

# 처음 입력 받기
for _ in range(M):
    fx, fy, d = map(int, input().split())
    graph[fx][fy].append(d - 1)

shark_x, shark_y = map(int, input().split())


# ---------------입력 끝 함수 시작-------------


# 0. 물고기 복사
def magic():
    fish_copy = [[[] for _ in range(5)] for _ in range(5)]
    global graph
    for yy in range(1, 5):
        for xx in range(1, 5):
            for dd in graph[xx][yy]:
                fish_copy[xx][yy].append(dd)
    return fish_copy


# 1. 물고기 이동
def move_fish():
    global graph
    global fish_smell
    move_temp = [[[] for _ in range(5)] for _ in range(5)]
    for xx in range(1, 5):
        for yy in range(1, 5):
            while graph[xx][yy]:
                dd = graph[xx][yy].pop()
                move_flag = True
                for count in range(8):
                    nd = (dd - count) % 8
                    ny = yy + delta[nd][0]
                    nx = xx + delta[nd][1]

                    if not check(nx, ny):  # 1. 격자 밖을 나가는 경우
                        continue

                    if shark_x == nx and shark_y == ny:  # 2. 상어가 있는 칸인 경우
                        continue

                    if fish_smell[nx][ny] > 0:  # 3. 냄새가 있는 칸인 경우
                        continue

                    # 그 외의 경우는 이동할 수 있다.
                    move_temp[nx][ny].append(nd)
                    move_flag = False
                    break

                if move_flag:  # 움직일 수 없는 경우
                    move_temp[xx][yy].append(dd)

    return move_temp


# 2. 상어가 이동
def move_shark():
    global shark_y
    global shark_x
    q = []  # 상어 이동 경로 찾기 위해서,, 우선순위큐를 역순으로 사용할 것
    case = 0
    for shark_dir in shark_case:
        isvisited = [[False for _ in range(5)] for _ in range(5)]
        eat_fishnum = 0
        flag = True
        shark_ny = shark_y
        shark_nx = shark_x
        for dir_y, dir_x in shark_dir:  # 각 경우 별로 움직이는 것
            shark_nx += dir_x
            shark_ny += dir_y
            if not check(shark_nx, shark_ny):  # 격자를 벗어나는 경우, 상어는 움직이지 못하므로 제외
                flag = False
                break

            if not isvisited[shark_nx][shark_ny]:
                eat_fishnum += len(graph[shark_nx][shark_ny])
                isvisited[shark_nx][shark_ny] = True

        if flag:  # 격자를 안벗어난 경우
            heapq.heappush(q, (-eat_fishnum, case, shark_dir))  # case가 사전순이므로, case로 넣어서 사전 순 판별.
            case += 1

    c, cc, moves = heapq.heappop(q)  # 제일 많이 없어진 경우 뽑아온다. 그래서 상어 움직여 줘야 한다.
    for dir_y, dir_x in moves:
        shark_y += dir_y  # 상어 움직인다.
        shark_x += dir_x
        if graph[shark_x][shark_y]:  # 물고기가 있는 경우
            fish_smell[shark_x][shark_y] = 3  # 냄새를 남기고
            graph[shark_x][shark_y].clear()


# 3. 냄새가 사라진다.
def remove_smell():
    global fish_smell
    for sy in range(1, 5):
        for sx in range(1, 5):
            if fish_smell[sx][sy] > 0:  # 0이 아니면 냄새가 있는 것이므로, 1씩 줄어든다. 처음에 2일 것이므로, 2->1->0 이런식
                fish_smell[sx][sy] -= 1


# 4. 복제 완료
def copy_complete(copy_fish):
    for yy in range(1, 5):
        for xx in range(1, 5):
            while copy_fish[xx][yy]:
                dd = copy_fish[xx][yy].pop()
                graph[xx][yy].append(dd)


for _ in range(S):
    # 0. 복제 마법 시전 -> 복제할 리스트에 물고기 저장
    cf = magic()
    graph = move_fish()
    move_shark()
    remove_smell()
    copy_complete(cf)

answer = 0
for y in range(1, 5):
    for x in range(1, 5):
        answer += len(graph[x][y])

print(answer)
