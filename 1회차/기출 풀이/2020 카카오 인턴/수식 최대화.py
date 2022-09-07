# 테케 4번 5번 통과 못하는중
# 4,5번 틀린 이유 : remove를 썼었는데, 그렇게 쓰면 뒤에 숫자가 안지워져서 통과하지 못한다.
# 소요시간 : 약 1시간
def solution(expression):
    calc_list = []
    num_list = []
    num = ''
    answer = 0
    for e in expression:
        if e == '+':
            calc_list.append(e)
            num_list.append(int(num))
            num = ''
        elif e == '-':
            calc_list.append(e)
            num_list.append(int(num))
            num = ''
        elif e == '*':
            calc_list.append(e)
            num_list.append(int(num))
            num = ''
        else:
            num += e

    calc = list(set(calc_list))  # 연산자 개수
    num_list.append(int(num))
    one_len = [0]
    two_len = [[0, 1], [1, 0]]
    three_len = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

    fact = []
    if len(calc) == 1:
        fact = one_len
    elif len(calc) == 2:
        fact = two_len
    else:
        fact = three_len

    if len(calc) == 1:
        idx = 0
        while idx < len(calc_list):
            if calc[0] == '-':
                num_list[idx + 1] = num_list[idx] - num_list[idx + 1]
            elif calc[0] == '+':
                num_list[idx + 1] = num_list[idx] + num_list[idx + 1]
            else:
                num_list[idx + 1] = num_list[idx] * num_list[idx + 1]
            idx += 1

        answer = max(abs(num_list[len(calc_list)]), answer)
    else:
        for f in fact:  # 연산자 경우 별로 따지는 곳
            cl = calc_list.copy()
            nl = num_list.copy()
            for op in f:  # 연산자 우선 순위 보이는 곳
                # 우선 순위에 따라서 탐색.
                idx = 0
                pop_list = []
                while idx < len(cl):
                    if cl[idx] == calc[op]:  # 우선 순위가 맞으면
                        if calc[op] == '-':
                            val = nl[idx] - nl[idx + 1]
                        elif calc[op] == '+':
                            val = nl[idx] + nl[idx + 1]
                        else:
                            val = nl[idx] * nl[idx + 1]
                        pop_list.append(idx)
                        nl[idx + 1] = val
                    idx += 1

                pop_list.sort()
                minus = 0
                for p in pop_list:
                    del nl[p - minus]
                    del cl[p - minus]
                    minus += 1

            answer = max(abs(nl[0]), answer)

    return answer