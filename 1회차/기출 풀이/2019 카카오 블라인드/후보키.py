# 거의 한시간..

import itertools

def solution(relation):
    col_len = len(relation[0])  # 컬럼 길이
    arrs = [i for i in range(col_len)]  # 0~n-1
    combs = []
    answers = []
    for i in range(1, col_len + 1):
        comb_list = list(itertools.combinations(arrs, i))
        if not comb_list:
            continue
        combs.append(comb_list)

    for comb in combs:  # 조합에 접근하려면 삼중 for문 실환가..
        for idx in comb:  # (1,2), (1,2,3) # col 경우별로 따지기
            dic = {}  # 후보 키 따지기 위한 딕셔너리
            is_ck = True  # 후보키인가

            for rel in relation:  # row 별로
                string = ""
                for i in idx:
                    string += rel[i] + ","

                if string in dic or string == "":  # 중복 식별
                    is_ck = False
                    break
                else:
                    dic[string] = 1

            if is_ck:  # 일단 유일하게 구별이 되는 경우
                answer_string = ""

                for i in idx:
                    answer_string += str(i)

                is_answer = False

                if len(answers) == 0:  # 비어 있는 경우
                    is_answer = True
                else:
                    for string in answers:  # 더 적게 들어간 것이랑 비교해서 최소성 판단
                        is_answer = False

                        for i in range(len(string)):
                            if string[i] not in answer_string:
                                is_answer = True
                                break

                        if not is_answer:
                            break

                if is_answer:
                    answers.append(answer_string)

    return len(answers)