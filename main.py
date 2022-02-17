
def solution(gems):
    jewelry = list(set(gems))  # 보석의 종류
    answer = [0, 99999]
    if len(jewelry) == 1:
        answer = [1, 1]
    else:
        left = 0
        right = 0
        prev_right = -1
        dic = {}
        while right < len(gems) and left < len(gems):
            if prev_right != right:
                if gems[right] not in dic:
                    dic[gems[right]] = 1
                else:
                    dic[gems[right]] += 1
                prev_right = right

            if len(dic) == len(jewelry): # 보석의 종류가 충분할 때
                if right - left < answer[1] - answer[0]:    # 더 작은 경우면
                    answer = [left+1,right+1]
                dic[gems[left]] -= 1
                if dic[gems[left]] == 0:
                    dic.pop(gems[left])
                left += 1
            else:
                right += 1
    return answer

g = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(g))