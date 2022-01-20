N,M = map(int,input().split())
icebox = []
for i in range(N):
    icebox.append(list(map(int,input())))

dy = [0,1,0,-1]
dx = [1,0,-1,0]
answer = 0

def check(x,y):
    if 0 <= x < M and 0 <= y < N:
        return True

    return False


def DFS(x, y):
    icebox[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if check(nx,ny) and icebox[ny][nx] == 0:
            DFS(nx, ny)


for y in range(N):
    for x in range(M):
        if icebox[y][x] == 0:
            DFS(x, y)
            answer += 1

print(answer)
