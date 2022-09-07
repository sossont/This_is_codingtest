# 5분 컷!

def solution(record):
    answer = []
    userdic = {}  # {userid : name} 의 딕셔너리
    for rec in record:
        inp = rec.split(' ')
        op = inp[0]
        uid = inp[1]
        if op == "Enter":
            nickname = inp[2]
            userdic[uid] = nickname
        elif op == "Change":
            nickname = inp[2]
            userdic[uid] = nickname

    for rec in record:
        inp = rec.split(' ')
        op = inp[0]
        uid = inp[1]
        if op == "Enter":
            log = userdic[uid] + "님이 들어왔습니다."
            answer.append(log)
        elif op == "Leave":
            log = userdic[uid] + "님이 나갔습니다."
            answer.append(log)

    return answer