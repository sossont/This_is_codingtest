def solution(board, skill):
    N = len(board)
    M = len(board[0])
    graph = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for t,r1,c1,r2,c2,d in skill:
        # 공격일 경우
        if t == 1:
            graph[r1][c1] -= d
            graph[r1][c2+1] += d
            graph[r2+1][c1] += d
            graph[r2+1][c2+1] -= d
        # 회복일 경우
        else:
            graph[r1][c1] += d
            graph[r1][c2+1] -= d
            graph[r2+1][c1] -= d
            graph[r2+1][c2+1] += d

    for dx in range(M+1):
        for dy in range(1, N+1):
            graph[dy][dx] += graph[dy-1][dx]

    for dy in range(N+1):
        for dx in range(1,M):
            graph[dy][dx] += graph[dy][dx-1]
    answer = 0

    for y in range(N):
        for x in range(M):
            if board[y][x] +graph[y][x] > 0:
                answer += 1

    return answer