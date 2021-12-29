n = int(input())
plan = input().split()
x,y = 1,1
dy = [-1,1,0,0]
dx = [0,0,-1,1]
move_type = ['L','R','U','D']

for move in plan:
    for i in range(4):
        if move_type[i] == move:
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 1 or nx < 1 or ny > n or nx > n:
                break

            y = ny
            x = nx


print(x,y)
