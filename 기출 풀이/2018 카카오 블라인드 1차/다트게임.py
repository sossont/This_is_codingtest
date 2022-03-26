# 15분 정도

def solution(dartResult):
    num = ""
    answer = 0
    numarr = []
    idx = 0
    for s in dartResult:
        if s == "S":
            now = int(num)
            num = ""
            numarr.append(now)
            answer += now
        elif s == "D":
            now = int(num)
            now = now * now
            num = ""
            numarr.append(now)
            answer += now
        elif s == "T":
            now = int(num)
            now = now * now * now
            num = ""
            numarr.append(now)
            answer += now
        elif s == "*":  # 이전 점수랑 현재 점수 더하기
            answer += numarr[-1]
            numarr[-1] = numarr[-1] * 2
            if len(numarr) > 1:
                answer += numarr[-2]
                numarr[-2] = numarr[-2] * 2
        elif s == "#":
            answer -= numarr[-1] * 2
            numarr[-1] = numarr[-1] * -1
        else:
            num += s
        print(answer)
        idx += 1
    return answer

# 정규 표현식 써서 푼 코드

import re

def solution(dartResult):
    p = re.compile('[0-9]+[SDT][*#]?')
    scores = p.findall(dartResult)
    total = 0
    prev_num = 0
    for score in scores:
        r = re.compile('[0-9]+')
        num = int(r.match(score).group()) # 숫자
        if score[-1] == '*':
            if score[-2] == 'D':
                num = pow(num,2)
            elif score[-2] == 'T':
                num = pow(num,3)
            num = num * 2
            total += num + prev_num
        elif score[-1] == '#':
            if score[-2] == 'D':
                num = pow(num,2)
            elif score[-2] == 'T':
                num = pow(num,3)
            num = -num
            total += num
        else:
            if score[-1] == 'D':
                num = pow(num,2)
            elif score[-1] == 'T':
                num = pow(num,3)
            total += num
        prev_num = num
    return total