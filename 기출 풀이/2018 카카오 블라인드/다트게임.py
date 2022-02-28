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