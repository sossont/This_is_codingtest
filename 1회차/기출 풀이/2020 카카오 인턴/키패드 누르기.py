# 소요시간 : 25분
# Map을 1을 (1,1), 3은 (1,3), 9는 (3,3)으로 하자.

def distance(now, nex):
    y_dist = abs(now[0] - nex[0])
    x_dist = abs(now[1] - nex[1])
    return y_dist + x_dist


def solution(numbers, hand):
    left = [4, 1]  # (y,x)
    right = [4, 3]
    answer = ''
    for num in numbers:
        y = int(num / 3)
        x = num % 3
        if x == 0:
            x = 3
        else:
            y += 1

        if num == 0:
            y = 4
            x = 2
        nex = [y, x]
        print(nex)

        if num == 1 or num == 4 or num == 7:
            left = nex
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            right = nex
            answer += 'R'
        else:
            left_dist = distance(left, nex)
            right_dist = distance(right, nex)
            print("left dist : ",left_dist)
            print("right dist : ",right_dist)
            if left_dist > right_dist:
                right = nex
                answer += 'R'
            elif right_dist > left_dist:
                left = nex
                answer += 'L'
            else:
                if hand == 'right':
                    right = nex
                    answer += 'R'
                else:
                    left = nex
                    answer += 'L'
        print("left : ", left)
        print("right : ", right)


    return answer