from collections import deque

N,M = map(int,input().split())
miro = []
for _ in range(N):
    miro.append(list(map(int,input())))

isvisited = [[0 for _ in range(M)] for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def check(x,y):
    if 0 <= x < M and 0 <= y < N:
        return True
    return False

def BFS(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if check(nx,ny) and miro[ny][nx] == 1:
                queue.append((nx,ny))
                miro[ny][nx] = miro[y][x] + 1


BFS(0,0)
print(miro[N-1][M-1])