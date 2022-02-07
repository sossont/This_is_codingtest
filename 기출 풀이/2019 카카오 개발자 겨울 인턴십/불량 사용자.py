# 테스트케이스 1,5,6,9 통과 못함
# 마지막에 중복 없애주면서 처리 했는데, 왜 안되지?


banned_star = []
ans = []


def solution(user_id, banned_id):
    # *이 아닌 idx를 담아 두어서, 아이디랑 비교하려고 함.
    for ban in banned_id:
        num = []
        for idx in range(len(ban)):

            if ban[idx] != '*':
                num.append(idx)

        banned_star.append(num)

    # 0번 BAN_ID를 둘러본다.
    usr_idx = 0
    isfound = [0 for _ in range(len(user_id))]
    for usr in user_id:  # User 아이디 순회 하면서
        if len(usr) == len(banned_id[0]):  # 길이가 같으면 대조해본다.
            flag = False
            if len(banned_star[0]) == 0:  # *로만 되어있는 불량 아이디
                flag = True
            else:
                for num in banned_star[0]:
                    if usr[num] != banned_id[0][num]:  # 대조하는 중에 다른 아이디면 멈춤
                        flag = False
                        break
                    else:
                        flag = True

            if isfound[usr_idx] == 0 and flag:
                isfound[usr_idx] = 1
                count(banned_id, user_id, 1, isfound, 1)  # 다음 아이디를 찾는다.
                isfound[usr_idx] = 0

        usr_idx += 1

    # 똑같이 생긴 Ban ID가 존재하는 경우, 중복 되는 경우를 체크 하기 때문에 중복 처리를 해준다. Set으로.
    answer = len(set(list(map(tuple, ans))))
    return answer


def count(banned_id, user_id, banidx, isfound, cnt):
    # 종료 조건(끝까지 탐색한 경우)
    if banidx == len(banned_star):
        if cnt == len(banned_star):
            answer = isfound[:]
            ans.append(answer)
        return

    usr_idx = 0

    for usr in user_id:  # User 아이디 순회 하면서
        if len(usr) == len(banned_id[banidx]):  # 길이가 같으면 대조해본다.
            flag = False
            if len(banned_star[banidx]) == 0:  # *로만 되어있는 불량 아이디
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

        usr_idx += 1