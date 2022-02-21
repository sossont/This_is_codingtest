# 정확성은 통과
# 시간 초과는 어떻게 해결하지..? insert, delete를 쓰지 말라는 건가?

def solution(n, k, cmd):
    answer = ''
    table = [i for i in range(n)]
    ans = [0 for _ in range(n)]
    delete = []
    # k를 화살표로 사용한다.
    for c in cmd:
        if c == 'Z':
            idx, val = delete.pop()
            if idx <= k:
                k += 1
            table.insert(idx,val)
        elif c == 'C':
            delete.append([k,table[k]])
            del table[k]
            if k == len(table): # 마지막 행인경우
                k -= 1
        elif c[0] == 'U':
            k -= int(c[2:])
        elif c[0] == 'D':
            k += int(c[2:])

    for idx, val in delete:
        ans[val] = 1

    for a in ans:
        if a == 0:
            answer += 'O'
        else:
            answer += 'X'
    return answer