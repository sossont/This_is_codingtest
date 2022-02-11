


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
        for j in visit:
            rooms[j] = n+1
    return answer

def solution(k, room_number):
    rooms = [i for i  in range(k+2)]    # 1번 부터 k번 방까지 가장 작은 번호를 가리키도록. k값이 뭐든 런타임 에러가 안나기 위해 k+1까지 초기화.
    answer = []
    for num in room_number:
        if num == rooms[num]:
            answer.append(num)
            rooms[num] = rooms[num+1]
        else:
            while num != rooms[num]:
                rooms[num] = rooms[num+1]
                num = rooms[num+1]
            answer.append(rooms[num])
            rooms[num] = rooms[num+1]
    return answer

'''
1. 1번방 배정. 1->2를 가리킴
2. 3번방 배정. 3->4를 가리킴
3. 4번방 배정. 4->5를 가리킴
4. 2번방 배정. 여기서 5번방을 가리키려면 어떻게 해야할까. 1->5를 가리켜야 한다.
5. 5번방 배정. 여기서 3->6을 가리켜야한다.

'''