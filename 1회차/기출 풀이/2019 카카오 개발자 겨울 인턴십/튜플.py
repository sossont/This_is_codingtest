# String To Arr 함수 구현하는 부분이 시간이 제일 오래 걸렸다.
# 시간 단축하는 방법은 여럿 있겠지만 나는 isfind를 써서 DP처럼 할 수 있게 품
# 걸린 시간 : 15분?

def stringtoarr(inp):
    idx = 0
    num = []
    for c in range(len(inp)):
        if inp[c] == '{':
            continue
        elif inp[c] == '}':
            if idx != 0:
                num.append(int(inp[c - idx:c]))
                idx = 0
            if len(num) != 0:
                arr.append(num)
                num = []
        elif inp[c] == ',':
            if idx != 0:
                num.append(int(inp[c - idx:c]))
                idx = 0
        else:
            idx += 1


arr = []


def solution(s):
    stringtoarr(s)
    arr.sort(key=len)
    answer = []
    isfind = [0 for _ in range(100001)]
    for numarr in arr:
        for num in numarr:
            if isfind[num] == 0:
                isfind[num] = 1
                answer.append(num)

    return answer
