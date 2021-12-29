n, m = map(int, input().split())
A,B,d = map(int, input().split())

graph = []
isvisited = [[0] * (m) for _ in range(n)]
direction = [[0,-1], [1,0], [0,1], [-1,0]] # 북, 동, 남, 서
back_direction = [[0,1],[-1,0],[0,-1],[1,0]] # 뒤로 가는 방향!

isvisited[A][B] = 1 # 방문 처리.
for i in range(n):
    graph.append(list(map(int, input().split())))  # 그래프 그림

def rotate(where):  # 반시계 방향으로 회전하는 함수
    where -= 1
    if where < 0:
        where = 3
    return where

count = 0
answer = 1
while True:
    if count == 4:  # 한바퀴 돌았으면
        ny = A + back_direction[d][0]
        nx = B + back_direction[d][1]
        if isvisited[ny][nx] == 0 and graph[ny][nx] == 0:  # 움직인다.
            A = ny
            B = nx
            isvisited[A][B] = 1
            count = 0
            answer += 1
            continue
        else:
            break
    d = rotate(d)   # 1. 회전
    ny = A + direction[d][0]
    nx = B + direction[d][1]

    if isvisited[ny][nx] == 0 and graph[ny][nx] == 0: # 움직인다.
        A = ny
        B = nx
        isvisited[A][B] = 1
        count = 0
        answer += 1
    else:
        count += 1

print(answer)