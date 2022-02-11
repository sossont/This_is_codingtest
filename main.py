
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