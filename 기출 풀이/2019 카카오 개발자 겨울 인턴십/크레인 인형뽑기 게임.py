from collections import deque


def solution(board, moves):
    answer = 0
    stack = deque()
    for move in moves:
        move -= 1
        for n in range(0,len(board)):
            if board[n][move] != 0: # 인형이 있는 경우
                doll = board[n][move]
                board[n][move] = 0 # 인형을 꺼낸다
                stack.append(doll)  # 스택에 인형을 담는다.
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()  # 인형 두 개 터트린다.
                    stack.pop()
                    answer += 2
                break
    return answer

# 실수 때문에 30분 걸림
# 인형 터트리는 경우만 break 해버리는 어이없는 실수..