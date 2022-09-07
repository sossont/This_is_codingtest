# 25분 정도

def solution(places):
    answer = []
    for place in places:    # place : 5*5 짜리 맵
        students = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    students.append([i,j])
        print(students)
        flag = True

        if len(students) <= 1:
            answer.append(1)
        else:
            for i in range(len(students)):
                if flag:
                    for j in range(i+1,len(students)):
                        base_y, base_x = students[i][0], students[i][1]
                        next_y, next_x = students[j][0], students[j][1]
                        if abs(next_x - base_x) + (next_y - base_y) > 2: # 멘헤튼 거리가 2 초과
                            continue
                        else:
                            if next_y - base_y == 2:
                                if place[base_y + 1][base_x] != 'X':    # 파티션이 없다!
                                    flag = False
                                    answer.append(0)
                                    break
                            elif next_x - base_x == 2:  # 파티션이 없다!
                                if place[base_y][base_x+1] != 'X':
                                    flag = False
                                    answer.append(0)
                                    break
                            else:
                                if place[base_y][next_x] == 'X' and place[next_y][base_x] == 'X':
                                    continue
                                else:
                                    flag = False
                                    answer.append(0)
                                    break
            if flag:
                answer.append(1)
    return answer