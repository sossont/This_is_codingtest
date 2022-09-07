# 30분 정도?

R,C,M = map(int,input().split())
sharks = []
graph = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    graph[r-1][c-1].append([s,d,z])

# 상어 입력 : (r,c)랑 속력, 이동방향, 크기


def check(cc,rr):
    if 0<=cc<C and 0<=rr<R:
        return True

    return False

answer = 0

def catch_shark():
    global answer
    global graph
    global cur_x
    for ny in range(R):
        if len(graph[ny][cur_x]) != 0:
            s,d,z = graph[ny][cur_x].pop()
            answer += z
            break


def shark_move():
    global graph
    temp_graph = [[[] for _ in range(C)] for _ in range(R)]
    delta = [[0,0],[-1,0], [1,0], [0,1],[0,-1]]
    for y in range(R):
        for x in range(C):
            # 비어있으면 지나간다.
            if len(graph[y][x]) == 0:
                continue

            while graph[y][x]:
                s,d,z = graph[y][x].pop()
                shark_y = y
                shark_x = x
                # 속력 만큼 이동
                for _ in range(s):
                    shark_y += delta[d][0]
                    shark_x += delta[d][1]

                    # 방향이 다를 경우 뒤집어준다.
                    if not check(shark_x,shark_y):
                        if d == 1:
                            d = 2
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 4
                        elif d == 4:
                            d = 3

                        shark_y += delta[d][0] * 2
                        shark_x += delta[d][1] * 2

                if temp_graph[shark_y][shark_x]:
                    if temp_graph[shark_y][shark_x][0][2] > z:
                        continue
                    temp_graph[shark_y][shark_x].pop()

                temp_graph[shark_y][shark_x].append([s,d,z])
    graph = temp_graph

cur_x = -1   # 낚시왕 x좌표

for _ in range(C):
    cur_x += 1
    catch_shark()
    shark_move()


print(answer)