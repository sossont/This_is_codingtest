# 위에서 부터 탐색을 하는 것
# 가로가 왼쪽부터 0 ~ n-1
# 세로가 위에부터 0 ~ m-1
# 그럼 왼쪽위에서부터 기준으로 오른쪽, 아래, 오른쪽대각선아래 이렇게 세개만 계속 판단하면 된다.

d = [(0,1), (1,0), (1,1)] # 이거를 왼쪽부터 n-2, m-2까지만 하면 범위 판단할 필요도 없음.

def solution(m, n, board):
    answer = 0
    board2 = []
    for b in board:
        board2.append(list(b))

    board = board2

    while True:
        count = 0
        pop_list = []

        # Board 순회
        for y in range(m-1):
            for x in range(n-1):
                if board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1] and board[y][x] != " ":
                    count +=1
                    pop_list.append((y,x))
                    pop_list.append((y, x+1))
                    pop_list.append((y+1, x))
                    pop_list.append((y+1, x+1))
        if count == 0:  # 더 이상 터트릴 게 없으면
            break

        pop_list = list(set(pop_list)) # 중복 제거
        answer += len(pop_list) # 지워질 블록의 개수 정답에 더하기

        # 블록 지우기
        for (y,x) in pop_list:
            board[y][x] = " "

        # 위에 있는 블록이 아래로 떨어지도록 한다.
        for x in range(n):
            for y in range(m-1,-1,-1):
                if board[y][x] == " ":  # 밑으로 내리기
                    # 빈칸일 때.
                    for k in range(y-1, -1,-1):
                        if board[k][x] != " ": # 빈칸이 아니면 내려준다.
                            board[y][x] = board[k][x]
                            board[k][x] = " "
                            break

    return answer

solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])