# 48분 컷

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

# y행, x열

# alpha : 45%
def check(xx,yy):
    if 0<=xx<N and 0<=yy<N:
        return True

    return False


def left(cx,cy):
    global graph
    alpha = [0,-1]
    queue = [[-1,-1,0.1],[-1,0,0.07], [-2,0,0.02],[-1,1,0.01],[1,1,0.01],[1,0,0.07],[2,0,0.02],[1,-1,0.1],[0,-2,0.05]]
    current_dust = graph[cy][cx]
    total_dust = current_dust
    graph[cy][cx] = 0
    out_dust = 0
    for q in queue:
        ny, nx, p = cy + q[0], cx + q[1], q[2]
        value = int(current_dust * p)
        total_dust -= value
        #밖으로 나가면
        if check(nx,ny):
            graph[ny][nx] += value
        else:
            #아니면
            out_dust += value


    ny = cy + alpha[0]
    nx = cx + alpha[1]
    if check(nx,ny):
        graph[ny][nx] += total_dust
    else:
        out_dust += total_dust
    return out_dust




def right(cx,cy):
    alpha = [0,1]
    queue = [[1,1,0.1],[-1, 0, 0.07], [-2, 0, 0.02], [1, -1, 0.01], [-1, -1, 0.01], [1, 0, 0.07], [2, 0, 0.02], [-1, 1, 0.1], [0, 2, 0.05]]
    current_dust = graph[cy][cx]
    total_dust = current_dust
    graph[cy][cx] = 0
    out_dust = 0
    for q in queue:
        ny, nx, p = cy + q[0], cx + q[1], q[2]
        value = int(current_dust * p)
        total_dust -= value
        # 밖으로 나가면
        if check(nx, ny):
            graph[ny][nx] += value
        else:
            # 아니면
            out_dust += value

    ny = cy + alpha[0]
    nx = cx + alpha[1]
    if check(nx, ny):
        graph[ny][nx] += total_dust
    else:
        out_dust += total_dust

    return out_dust


def down(cx,cy):
    alpha = [1, 0]
    queue = [[0,-1,0.07],[0,-2,0.02],[-1,-1,0.01],[-1,1,0.01],[0,1,0.07],[0,2,0.02],[1,1,0.1],[2,0,0.05],[1,-1,0.1]]
    current_dust = graph[cy][cx]
    total_dust = current_dust
    graph[cy][cx] = 0
    out_dust = 0
    for q in queue:
        ny, nx, p = cy + q[0], cx + q[1], q[2]
        value = int(current_dust * p)
        total_dust -= value
        # 밖으로 나가면
        if check(nx, ny):
            graph[ny][nx] += value
        else:
            # 아니면
            out_dust += value

    ny = cy + alpha[0]
    nx = cx + alpha[1]
    if check(nx, ny):
        graph[ny][nx] += total_dust
    else:
        out_dust += total_dust

    if cy == 3 and cx == 2:
        print(total_dust)
        print(out_dust)
        print(current_dust)

    return out_dust

def up(cx,cy):
    alpha = [-1,0]
    queue = [[0,-1,0.07],[0,-2,0.02],[1,1,0.01],[1,-1,0.01],[0,1,0.07],[0,2,0.02],[-1,1,0.1],[-2,0,0.05],[-1,-1,0.1]]
    current_dust = graph[cy][cx]
    total_dust = current_dust
    graph[cy][cx] = 0
    out_dust = 0
    for q in queue:
        ny, nx, p = cy + q[0], cx + q[1], q[2]
        value = int(current_dust * p)
        total_dust -=  value
        # 밖으로 나가면
        if check(nx, ny):
            graph[ny][nx] += value
        else:
            # 아니면
            out_dust += value

    ny = cy + alpha[0]
    nx = cx + alpha[1]
    if check(nx, ny):
        graph[ny][nx] += total_dust
    else:
        out_dust += total_dust

    return out_dust

# 1, 2, 3, 4: 왼 아 오 위
def init_tor():
    arr = []
    init_y = (N-1)//2
    init_x = (N-1)//2
    cur_y = init_y
    cur_x = init_x
    for n in range(3,N+1):
        if n % 2 == 0:
            continue

        cur_x -= 1
        arr.append([cur_y,cur_x,1])
        for _ in range(n-2):
            cur_y += 1
            arr.append([cur_y,cur_x,2])

        for _ in range(n-1):
            cur_x += 1
            arr.append([cur_y,cur_x,3])

        for _ in range(n-1):
            cur_y -= 1
            arr.append([cur_y,cur_x,4])

        for _ in range(n-1):
            cur_x -= 1
            arr.append([cur_y,cur_x,1])

    return arr



tor = init_tor()    # 토네이도의 이동 방향, 좌표가 담겨있는 함수

answer = 0
for y,x,d in tor:
    if d == 1:
        answer += left(x,y)
    elif d == 2:
        answer += down(x,y)
    elif d == 3:
        answer += right(x,y)
    elif d == 4:
        answer += up(x,y)
print(answer)
