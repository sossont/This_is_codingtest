"""
테스트 14, 19, 21, 22에서 시간 초과 발생.
"""

def solution(words):
    dic = {}
    answer = 0
    # 단어 별로 딕셔너리에 개수 넣어놓기.
    for word in words:
        for i in range(len(word) + 1):
            if word[0:i] in dic:
                dic[word[0:i]] += 1
            else:
                dic[word[0:i]] = 1

    for word in words:
        for i in range(1, len(word) + 1):
            if dic[word[0:i]] == 1:
                answer += i
                break

            if i == len(word):
                answer += i
                break

    return answer