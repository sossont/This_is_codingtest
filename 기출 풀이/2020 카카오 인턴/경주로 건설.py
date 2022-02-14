d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# (y,x)
isvisited = [[0 for _ in range(26)] for _ in range(26)]  # 방문 여부
dp = [[987654321 for _ in range(26)] for _ in range(26)]
answer = 987654321


# 왜 자꾸 무한루프 돌지?

def solution(board):
    isvisited[0][0] = 1
    isvisited[0][1] = 1
    dfs(0, 1, 0, 100, board)
    isvisited[0][1] = 0
    isvisited[1][0] = 1
    dfs(1, 0, 1, 100, board)
    return answer


def dfs(y, x, pre_dir, value, board):
    if board[y][x] == 1:
        return

    # 이거 추가하니까 풀리넹?

    if dp[y][x] >= value:
        dp[y][x] = value
    else:
        return

    end = len(board) - 1
    global answer

    if y == end and x == end:
        answer = min(answer, value)
        print(answer)
        return

    for direct in range(4):
        ny = y + d[direct][0]
        nx = x + d[direct][1]
        if 0 <= ny < len(board) and len(board) > nx >= 0:  # 맵 안에 들어와 있을 때
            if isvisited[ny][nx] == 0 and board[ny][nx] == 0:
                isvisited[ny][nx] = 1
                if pre_dir == direct:  # 직진
                    dfs(ny, nx, direct, value + 100, board)
                else:  # 꺾는다
                    dfs(ny, nx, direct, value + 600, board)
                isvisited[ny][nx] = 0