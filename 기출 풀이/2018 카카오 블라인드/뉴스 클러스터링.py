# 소요시간 : 25분 정도
# copy로 찾는 로직이 필요했다.

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    length1 = len(str1)
    length2 = len(str2)
    set1 = []
    set2 = []
    con_set = []
    for i in range(length1-1):
        if 'a' <= str1[i] <= 'z' and 'a' <= str1[i+1] <= 'z':
            set1.append(str1[i:i+2])

    for i in range(length2-1):
        if 'a' <= str2[i] <= 'z' and 'a' <= str2[i + 1] <= 'z':
            set2.append(str2[i:i + 2])

    set1_copy = set1.copy()
    set2_copy = set2.copy()
    for s1 in set1:
        if s1 in set2.copy():
            con_set.append(s1)
            set2_copy.remove(s1)
            set1_copy.remove(s1)

    union = set1_copy + set2_copy + con_set
    a1 = len(con_set)
    a2 = len(union)
    if a2 == 0:
        return 65536
    print(union)
    print(con_set)
    print(set1_copy,set2_copy)
    answer = float(a1) / float(a2) * 65536
    return int(answer)

solution("aabbc","abbde")