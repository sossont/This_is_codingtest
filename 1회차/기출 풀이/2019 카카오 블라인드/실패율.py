# 정수로 배열 선언하니까 확률 정확도 문제 때문에 실패
# 따라서 이번에는 같은 확률들을 따로 구하는걸로하자.
# 제일 쉬운건데, 야매로 푸려다가 실패해서 30분이나 걸려버림..

def solution(N, stages):
    answer = []
    dic = {}
    for s in stages:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

    percents = []
    app = len(stages)
    for i in range(1, N + 1):  # 1~N Stage
        if i in dic:
            unclear = dic[i]
            percent = unclear / app
            app -= unclear
            percents.append((percent, i))
        else:
            percents.append((0, i))
    percents.sort(reverse=True)

    same = []
    for i in range(len(percents)):
        if i == 0:
            same.append(percents[i][1])
            continue

        if percents[i][0] == percents[i - 1][0]:  # 이전꺼랑 확률이 같으면
            same.append(percents[i][1])
        else:  # 다르면
            # 같은 것이 있었을 때, 확률이 같은 것을 역순으로 집어넣기
            while len(same) != 0:
                val = same.pop()
                answer.append(val)
            same.append(percents[i][1])

    while len(same) != 0:
        val = same.pop()
        answer.append(val)

    return answer
