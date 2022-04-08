# 문제를 잘못이해해서 30~40분 걸린듯

def solution(orders, course):
    answer = []
    dic = {}
    for order in orders:
        binary = []

        for i in range(1, pow(2, len(order))):  # 2진수로 모든 경우를 나타낸다.
            binar = '{0:10b}'.format(i)
            binary.append(binar.replace(' ', '0')[-len(order):])

        for b in binary:
            string = ""
            for c in range(len(b)):
                if b[c] == '1':
                    string += order[c]
            if len(string) == 1:
                continue

            string = ''.join(sorted(string))

            if string in dic:
                dic[string] += 1
            else:
                dic[string] = 1

    test = [[] for _ in range(11)]

    for count in course:
        for key in dic.keys():
            if len(key) == count and dic[key] > 1:
                test[len(key)].append([dic[key], key])

    for t in test:
        if len(t) == 0:
            continue

        t.sort(reverse=True)

        for m in t:
            if m[0] == t[0][0]:
                answer.append(m[1])

    answer.sort()
    return answer
