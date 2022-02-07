# 테스트케이스 1,5,6,9 통과 못함
# 마지막에 중복 없애주면서 처리 했는데, 왜 안되지?


banned_star = []
ans = []

def solution(user_id, banned_id):
    for ban in banned_id:
        num = []
        for idx in range(len(ban)):

            if ban[idx] != '*':
                num.append(idx)

        banned_star.append(num)

    i = 0
    # ban id를 banidx 부터 순회하면서
    usr_idx = -1
    for usr in user_id: # User 아이디 순회 하면서
        isfound = [0 for _ in range(len(user_id))]
        usr_idx += 1
        flag = True

        if len(usr) == len(banned_id[i]):  # 길이가 같으면 대조해본다.
            flag = False
            for num in banned_star[i]:
                if usr[num] != banned_id[i][num]:  # 대조하는 중에 다른 아이디면 멈춤
                    flag = False
                    break
                else:
                    flag = True

            if isfound[usr_idx] == 0 and flag:
                isfound[usr_idx] = 1
                count(banned_id, user_id, 1, isfound, 1)  # 다음 아이디를 찾는다.


    answer = len(set(list(map(tuple ,ans))))
    return answer


def count(banned_id, user_id, banidx, isfound, cnt):
    if banidx == len(banned_star):
        if cnt == len(banned_star):
            answer = isfound[:]
            ans.append(answer)
        return

    usr_idx = -1
    for usr in user_id: # User 아이디 순회 하면서
        usr_idx += 1

        if len(usr) == len(banned_id[banidx]):  # 길이가 같으면 대조해본다.
            flag = False
            if len(banned_star[banidx]) == 0:
                flag = True
            else:
                for num in banned_star[banidx]:
                    if usr[num] != banned_id[banidx][num]:  # 대조하는 중에 다른 아이디면 멈춤
                        flag = False
                        break
                    else:
                        flag = True


            if isfound[usr_idx] == 0 and flag:
                isfound[usr_idx] = 1
                count(banned_id, user_id, banidx + 1, isfound, cnt + 1)  # 다음 아이디를 찾는다.
                isfound[usr_idx] = 0
