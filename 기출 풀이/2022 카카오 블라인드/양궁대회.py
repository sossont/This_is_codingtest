# 푸는 시간 : 38분 정도

answer = []
tms = 0

def solution(n, info):
    global answer
    score = 0
    for i in range(len(info)):
        if info[i] != 0:
            score += (10 - i)

    calc(info, 0, n, 0, [], score)
    if len(answer) == 0:
        answer = [-1]
    return answer


def calc(info, idx, arrow_count, total, arrows, score):
    global tms
    global answer

    if arrow_count < 0:
        return

    if idx == len(info):  # 끝에 도달한 경우
        if arrow_count != 0:
            arrows[idx-1] += arrow_count

        if score < total:
            if len(answer) == 0:
                tms = total - score
                answer = arrows
                return

            if tms > total - score: # 점수 차가 더 작다.
                return
            elif tms < total - score:
                tms = total - score
                answer = arrows
            else:   #  점수 차가 같을 경우
                for i in range(9, -1, -1):
                    if answer[i] == arrows[i]:
                        continue
                    elif answer[i] < arrows[i]:
                        answer = arrows
                        break
                    else:
                        break
        return

    new_arrows = arrows.copy()
    pass_arrows = arrows
    new_arrows.append(info[idx] + 1)
    pass_arrows.append(0)

    next_score = score
    if info[idx] != 0:
        next_score -= (10-idx)

    calc(info, idx + 1, arrow_count - (info[idx] + 1), total + 10 - idx, new_arrows, next_score)  # 이번에 점수를 획득한 경우
    calc(info, idx + 1, arrow_count, total, pass_arrows, score)  # 이번에 획득하지 않고 다음으로 넘어간 경우


