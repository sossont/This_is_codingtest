# 풀이 시간 : 25분?

def solution(msg):
    dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                  "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
                  "X": 24, "Y": 25, "Z": 26}
    dict_idx = 27  # 다음 색인될 사전 번호
    answer = []
    msg_len = 1  # 메세지 길이
    idx = 0
    max_len = 0
    while idx + msg_len <= len(msg):
        if msg[idx:idx + msg_len] in dictionary:  # 사전에 있는 경우 색인 출력
            msg_len += 1
        else:
            answer.append(dictionary[msg[idx:idx + msg_len - 1]])
            dictionary[msg[idx:idx + msg_len]] = dict_idx
            dict_idx += 1
            idx = idx + msg_len - 1
            msg_len = 1

    # 마지막에 추가 못한 문자열 추가
    if msg_len != 1:
        answer.append(dictionary[msg[idx:idx + msg_len - 1]])
    return answer