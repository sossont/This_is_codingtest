N,M,K = map(int,input().split())


# (r행, c열)
# [r][c]
balls = []
for _ in range(M):
    balls.append(list(map(int,input().split())))

graph = [[[]for _ in range(N)] for _ in range(N)]

for r,c,m,s,d in balls:
    graph[r-1][c-1].append([m,s,d])

def check(r,c):
    if 0<=r<N and 0<=c<N:
        return True

# 0번 부터 7번까지 방향
delta = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

def move_fireball():
    global graph
    global N

    temp = [[[]for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if graph[x][y]:
                # 비어 있지 않으면
                while graph[x][y]:
                    m,s,d = graph[x][y].pop()

                    dy = abs(delta[d][1] * s) % N
                    dx = abs(delta[d][0] * s) % N
                    if delta[d][1] < 0:
                        ny = y - dy
                    else:
                        ny = y + dy

                    if delta[d][0] < 0:
                        nx = x - dx
                    else:
                        nx = x + dx

                    if ny <= -1:    # 연결되어 있으니까
                        ny += N

                    if nx <= -1:
                        nx += N

                    if ny >= N:
                        ny -= N

                    if nx >= N:
                        nx -= N

                    temp[nx][ny].append([m,s,d])
                    # 이동 한다.

    for x in range(N):
        for y in range(N):
            if len(temp[x][y]) >= 2:
                sm = 0
                ss = 0
                count = 0
                prime = temp[x][y][0][2]
                sd = 0 # 모두 같으면 0
                while temp[x][y]:
                    m,s,d = temp[x][y].pop()
                    sm += m
                    ss += s
                    count += 1
                    if prime % 2 != d % 2:
                        sd = 1  # 그렇지 않으면 1

                sm = sm // 5
                ss = ss // count
                if sm == 0:
                    continue
                for i in range(4):
                    temp[x][y].append([sm,ss, 2*i+sd])

    graph = temp


for _ in range(K):
    move_fireball()

answer = 0

for x in range(N):
    for y in range(N):
        while graph[x][y]:
            v, _, _ = graph[x][y].pop()
            answer += v

print(answer)

