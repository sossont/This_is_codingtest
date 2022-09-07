# 소요시간 : 15분

def solution(p):
    return recursion(p)


def recursion(p):
    if len(p) == 0:
        return ""  # 빈문자열이면 빈문자열 반환
    else:
        left = 0
        right = 0
        idx = 0
        while True:
            if left == right and left != 0:  # 균형잡힌 문자열이면
                break
            else:
                if p[idx] == '(':
                    left += 1
                elif p[idx] == ')':
                    right += 1
            idx += 1
        u = p[:idx]
        v = p[idx:]
        left = 0
        right = 0
        isright = True  # 올바른 괄호 문자열인지
        for i in range(len(u)):
            if right > left:
                isright = False
                break

            if u[i] == '(':
                left += 1
            elif u[i] == ')':
                right += 1

        if isright:  # v에 대해 1단계부터 다시 수행
            return u + recursion(v)
        else:
            empty = '('
            empty += recursion(v)
            empty += ')'
            remove_u = u[1:len(u) - 1]
            ret = ""
            for i in range(len(remove_u)):
                if remove_u[i] == '(':  # 뒤집기
                    ret += ')'
                else:
                    ret += '('
            return empty + ret