def solution(p):
    return first(p)



def first(s):
    if s == '':
        return ''
    left = 0
    right = 0
    sum = 0
    u = s
    v = ''
    for word in s:
        if word == '(':
            left += 1
        else:
            right += 1
        sum += 1
        if left == right:
            u = s[:sum]
            v = s[sum:]
            break

    return third(u,v)

def third(u, v):
    left = 0
    right = 0
    for word in u:
        if word == '(':
            left += 1
        else:
            right += 1

        if right > left:
            string = '('
            string += first(v)
            string += ')'
            real_u = u[1:-1]
            for r in real_u:
                if r == '(':
                    string += ')'
                else:
                    string += '('

            return string
            # 올바른 문자열이 아님

    return u + first(v)
