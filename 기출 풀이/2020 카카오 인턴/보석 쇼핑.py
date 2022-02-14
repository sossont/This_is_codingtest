"""
1트 : 정확성은 통과, 효율성은 통과 못함
효율성 통과 못할 줄 알았음..이거 완전 노가다로 푼거라
일단은 0.5솔, 소요시간 : 15분
"""

def solution(gems):
    jewelry = list(set(gems))
    answer = [0, 99999]
    if len(jewelry) == 1:
        answer = [1, 1]
    else:
        for idx in range(len(gems)):
            l = jewelry.copy()
            for j in range(idx, len(gems)):
                if gems[j] in l:
                    l.remove(gems[j])
                if len(l) == 0:
                    if answer[1] - answer[0] > j - idx:
                        answer = [idx+1, j+1]
                    break


    return answer

"""
2트 : 딕셔너리 타입을 사용해보니 확실히 시간이 많이 줄었다. 정확성 코드는 22ms가 제일 오래걸리는것일정도(1트때는 3300까지감)
근데 이것도 시간초과가 뜨네.. (테케 5,7,8,10,11,12,13,14,15)

결론은 sort 횟수를 줄여아 하는 것 같다.

"""

def solution(gems):
    jewelry = list(set(gems))  # 보석의 종류
    answer = [0, 99999]
    if len(jewelry) == 1:
        answer = [1, 1]
    else:
        dic = {}
        for idx in range(len(gems)):
            dic[gems[idx]] = idx

            if len(dic) == len(jewelry):
                # 길이가 일치하고, 제일 작았던 인덱스놈에게 변화가 있으면
                sorted_dic = sorted(dic.items(), key=lambda item: item[1])
                if sorted_dic[len(dic) - 1][1] - sorted_dic[0][1] < answer[1] - answer[0]:
                    answer = [sorted_dic[0][1] + 1, sorted_dic[len(dic) - 1][1] + 1]
                    dic.pop(sorted_dic[0][0])

    return answer