def solution(board, skill):
    graph = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    answer = 0
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            graph[r1][c1] -= d
            graph[r1][c2 + 1] += d
            graph[r2 + 1][c1] += d
            graph[r2 + 1][c2 + 1] -= d
        else:
            graph[r1][c1] += d
            graph[r1][c2 + 1] -= d
            graph[r2 + 1][c1] -= d
            graph[r2 + 1][c2 + 1] += d

    for dx in range(len(graph[0])):
        for dy in range(1, len(graph)):
            graph[dy][dx] += graph[dy - 1][dx]

    for dy in range(len(board)):
        for dx in range(len(board[0])):
            if dx >= 1:
                graph[dy][dx] += graph[dy][dx - 1]

            if board[dy][dx] + graph[dy][dx] >= 1:
                answer += 1

    return answer