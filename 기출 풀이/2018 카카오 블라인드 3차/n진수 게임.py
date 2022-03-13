def solution(n, t, m, p):
    answer = ''
    turn = 1  # turn : 1~m
    prev_num = 0  #
    num = 0
    numbers = [0]

    while len(answer) < t:
        if prev_num != num:  # 숫자가 바뀌었으면 정답을 다시 구해야한다.
            prev_num = num
            div_num = num
            numbers.append(div_num % n)
            while div_num >= n:
                div_num = int(div_num / n)
                numbers.append(div_num % n)

        # numbers에 정답 들어 있음.
        if len(numbers) == 0:
            num += 1
            continue

        next_answer = numbers.pop()
        # 튜브 턴이면
        if turn == p:
            ans = str(next_answer)
            if next_answer == 10:
                ans = 'A'
            elif next_answer == 11:
                ans = 'B'
            elif next_answer == 12:
                ans = 'C'
            elif next_answer == 13:
                ans = 'D'
            elif next_answer == 14:
                ans = 'E'
            elif next_answer == 15:
                ans = 'F'
            answer += ans

        # 다음 턴으로 넘긴다.
        turn += 1
        # 숫자 넘어가면 조정해준다.
        if turn > m:
            turn -= m

    return answer