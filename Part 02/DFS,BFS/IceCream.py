# 세로 길이 N , 가로 길이 M.

N,M = map(int,input().split())

teul = []

for i in range(N):
    teul.append(list(map(int,input())))      # 입력 받기

isvisted = []   # 방문 여부 따지는 배열
for i in range(N):
    nlist = []
    for j in range(M):
        nlist.append(False)
    isvisted.append(nlist)


# 인접해있다는 것 ? => x,y좌표가 1 이하만큼 차이가 나는 것.

def DFS(x,y):
    # 범위를 벗어나는 경우.
    if x < 0 or x >= N or y < 0 or y >= M:  # 사실 순서만 중요하고 x,y는 별로 안중요한듯.
        return False

    if not isvisted[x][y] and teul[x][y] == 0:
        isvisted[x][y] = True
        DFS(x-1,y)
        DFS(x,y-1)
        DFS(x+1,y)
        DFS(x,y+1)
        return True

    return False

result = 0

for i in range(N):
    for j in range(M):
        if DFS(i, j):
            result += 1

print(result)