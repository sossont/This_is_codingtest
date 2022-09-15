def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield arr[i]
        else:
            for nxt in combination(arr[i+1:], r-1):
                yield arr[i] + nxt

def solution(orders, course):
    dic = {}

    for order in orders:
        order = ''.join(sorted(order))
        for length in range(1, len(order)+1):
            if length not in course:
                continue

            for comb in combination(order, length):
                if comb in dic:
                    dic[comb] += 1
                else:
                    dic[comb] = 1


    MAX = [2] * 11
    for key in dic.keys():
        if MAX[len(key)] < dic[key]:
            MAX[len(key)] = dic[key]

    answer = []
    for key in dic.keys():
        if dic[key] == MAX[len(key)]:
            answer.append(key)

    answer.sort()
    return answer