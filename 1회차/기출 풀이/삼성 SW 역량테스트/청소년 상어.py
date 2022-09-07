# 물고가가 이동할 수 없는 칸 : 상어가 있는 칸이나 맵 밖
# 45도 씩 방향 -> 방향이 무려 8개
# Process를 정리해 보자.
# 1. 물고기 번호가 작은 순서대로 이동 -> 그러면 지도가 바뀌어있겠지?
# 2. 상어가 (0,0)으로 온다. 물고기를 잡아먹었다. 방향을 얻었다.
# ---- 여기까지는 불변하는 과정 ----
# 1. move_shark(1~3) (1~3칸 이동하냐에 따라 결과가 다르다.) 이동하는 것엔 잡아먹는 것과 방향 흡수하는 것 포함
# 이 때 상어가 몇 칸 이동하냐에 따라 지도가 달라져있다. 이 지도 마다 구해야 한다.
# move_shark(1)
# 2. 다시 물고기 번호가 작은 순서대로 이동한다. -> 지도 바뀌어있겠지
## 다시 1번 과정으로 돌아간다.
import copy

a = [0] * 16
b = [0] * 16

for i in range(4):
    a[i * 4], b[i * 4], a[i * 4 + 1], b[i * 4 + 1], \
    a[i * 4 + 2], b[i * 4 + 2], a[i * 4 + 3], b[i * 4 + 3] = \
        map(int, input().split())

pos = []
graph_dir = []

# (y,x) 로 0번부터 7번까지 방향
directions = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
fishes = [[0, 0, 0] for _ in range(17)]  # 0~16. 0은 안쓸 것
for i in range(4):
    lis1 = []
    lis2 = []
    for j in range(4):
        lis1.append(a[i * 4 + j])
        lis2.append(b[i * 4 + j] - 1)

    pos.append(lis1)
    graph_dir.append(lis2)

# graph : graph[y][x]에 물고기 번호가 저장되어있음
# fish_dir[y][x]에 거기에 존재하는 물고기의 방향이 저장되어 있음

# fishes 번호 별로 좌표랑 방향 저장
for y in range(4):
    for x in range(4):
        fish_num = pos[y][x]
        fishes[fish_num] = [y, x, graph_dir[y][x]]


# 맵 밖으로 나가는 지 확인
def check(check_y, check_x):
    if 0 <= check_y < 4 and 0 <= check_x < 4:
        return True

    return False


# 샤크 포지션, 방향, 먹은 물고기 번호합

####### 여기까지 입력 정리함 #######

# -1 : 상어, 0 : 빈칸으로 정한다.
## 상어가 0,0으로 들어옴
# 물고기 이동 함수

def move_fish(fish, graph):
    for fishnum in range(1, 17):
        fish_y, fish_x, direct = fish[fishnum]
        if fish_y == -1:  # 이 번호의 물고기는 더 이상 존재하지 않는다.
            continue

        for direct_num in range(8):  # 그냥 이동 ~ 반시계 방향 회전
            direction = direct + direct_num
            if direction >= 8:
                direction -= 8
            ny = fish_y + directions[direction][0]
            nx = fish_x + directions[direction][1]

            if not check(ny, nx):  # 그 방향으로 못가면
                continue

            if graph[ny][nx] == -1:  # 그 위치에 상어가 있으면
                continue

            # 위치를 바꿀 물고기 번호
            dest_fishnum = graph[ny][nx]
            dest_fish_dir = fish[dest_fishnum][2]  # 바꿀 물고기의 방향
            fish[dest_fishnum] = [fish_y, fish_x, dest_fish_dir]
            graph[fish_y][fish_x] = dest_fishnum
            fish[fishnum] = [ny, nx, direction]
            graph[ny][nx] = fishnum
            break


# 상어 이동 함수
# 상어 이동 칸 수 별로 계산해야 하는데, 이거 딥카피해서 넣어야하나..?
def move_shark(copy_fish, copy_graph, shark_pos, shark_direction, ans):
    answe = ans
    for mul in range(1, 4):  # 여러칸 이동 가능하니까, 1칸 이동 ~ 3칸 이동 판단 하기
        ny = shark_pos[0] + directions[shark_direction][0] * mul
        nx = shark_pos[1] + directions[shark_direction][1] * mul

        if not check(ny, nx):  # 못 움직이면, 집으로 돌아간다. 어차피 mul이 더커져도 못 움직이는 건 똑같다.
            return answe

        if copy_graph[ny][nx] == 0:  # 물고기가 없는 칸은 못간다.
            continue

        c_graph = copy.deepcopy(copy_graph)
        c_fish = copy.deepcopy(copy_fish)

        num = c_graph[ny][nx]  # 그 위치에 있는 물고기 번호
        next_dir = copy_fish[num][2]  # 방향 흡수
        c_fish[num] = [-1, -1, -1]  # 물고기 잡아 먹힘
        tmp = c_graph[ny][nx]

        c_graph[ny][nx] = -1  # 상어가 (ny,nx)로 간다!
        c_graph[shark_pos[0]][shark_pos[1]] = 0  # 상어 있던 곳은 비어야함
        move_fish(c_fish, c_graph)
        answe = max(answe, move_shark(c_fish, c_graph, [ny, nx], next_dir, ans + tmp))

    return answe


answer = 0
# 시작
# 상어가 0,0 잡아먹음

fish_num = pos[0][0]
shark_dir = fishes[fish_num][2]
answer += fish_num
fishes[fish_num] = [-1, -1, -1]
pos[0][0] = -1  # 0,0에 상어가 있다.
move_fish(fishes, pos)
## 본격 재귀 시작
answer = max(answer, move_shark(fishes, pos, [0, 0], shark_dir, answer))
print(answer)
