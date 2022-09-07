# 소요시간 : 30분

def solution(new_id):
    answer = ''
    low_id = new_id.lower()  # 1단계 : 소문자로 치환
    sec_id = ""  # 2단계
    for s in low_id:
        if '0' <= s <= '9' or 'a' <= s <= 'z' or s == '-' or s == '_' or s == '.':
            sec_id += s

    for i in range(len(sec_id)):
        sec_id = sec_id.replace('..', '.')  # 3단계

    # 4단계
    if len(sec_id) == 0:
        pass
    elif sec_id[0] == '.':
        if len(sec_id) <= 1:
            sec_id = ""
        else:
            sec_id = sec_id[1:]

    print(sec_id)
    if len(sec_id) == 0:
        pass
    elif sec_id[-1] == '.':
        if len(sec_id) <= 1:
            sec_id = ""
        else:
            sec_id = sec_id[:-1]

    # 5단계
    if len(sec_id) == 0:
        answer = 'a'
    else:
        answer = sec_id

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
    elif len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer
