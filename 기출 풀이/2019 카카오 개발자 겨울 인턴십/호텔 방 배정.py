# 시간 초과 날 것 같았음..
# 정확성 만점, 효율성 0점. -> 0.5점 짜리.

def solution(k, room_number):
    rooms = [i for i  in range(k+2)]    # 1번 부터 k번 방까지 가장 작은 번호를 가리키도록. k값이 뭐든 런타임 에러가 안나기 위해 k+1까지 초기화.
    answer = []
    for num in room_number:
        n = num
        visit = [n]
        if num == rooms[num]:
            answer.append(num)
            rooms[num] = rooms[num+1]
        else:
            while num != rooms[num]:
                n = rooms[n]
                visit.append(n)
            answer.append(n)
            for v in visit:
                rooms[v] = n+1
    return answer

# 2트
# 이렇게 하니까 효율성 5~7번이 시간초과 뜬다.
# 배열로 선언해놓고 하면 배열만 탐색이 안되므로, 딕셔너리를 써서 값을 저장하는 게 맞는 것 같다.
def solution(k, room_number):
    rooms = [i for i  in range(k+2)]    # 1번 부터 k번 방까지 가장 작은 번호를 가리키도록. k값이 뭐든 런타임 에러가 안나기 위해 k+1까지 초기화.
    answer = []
    for num in room_number:
        n = num
        visit = [n]
        if num == rooms[num]:
            answer.append(num)
            rooms[num] = rooms[num+1]
        else:
            while n != rooms[n]:
                n = rooms[n]
                visit.append(n)
            answer.append(n)
            for v in visit:
                rooms[v] = n+1
    return answer

# 정답 코드
# 내 코드랑 조금 느낌이 같은 듯 다른데, 딕셔너리를 써서 바로 보내주는게 핵심이다.
# 그리고 쫓아가는게 아니라, 정답을 갖고 다 업데이트 해주는 것.
def solution(k, room_number):
    rooms = {}
    answer = []
    for num in room_number:
        n = num
        visit = [n]
        while n in rooms:
            n = rooms[n]
            visit.append(n)
        answer.append(n)
        for v in visit:
            rooms[v] = n+1
    return answer