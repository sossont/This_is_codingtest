from collections import deque

N, M = map(int,input().split())
# N개의 줄. 그니까 행의 개수.

maze = []  # 1,1 부터 시작해야 한다. 고로 첫쨰줄은 이상한 수를 넣어놓는다.

for i in range(N):
    maze.append(list(map(int,(input()))))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))

    return maze[N-1][M-1]

print(maze)
print(BFS(0,0))
