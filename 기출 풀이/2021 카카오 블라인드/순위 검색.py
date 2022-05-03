## 2회차 풀이
import bisect

dic = {}

def solution(info, query):
    answer = []
    global dic
    for inf in info:
        string = inf.split(' ')
        score = int(string[-1])
        string = string[:-1]
        create_info(string[0], string, 1, score)
        create_info('-', string, 1, score)

    for key in dic.keys():
        dic[key].sort()

    for que in query:
        string = que.split(' ')
        tmp = []
        for s in string:
            if s == 'and':
                continue
            tmp.append(s)
        score = int(tmp[-1])
        string = tmp[:-1]
        real_query = ''.join(string)
        if real_query in dic:
            ans = bisect.bisect_left(dic[real_query], score)
            answer.append(len(dic[real_query]) - ans)
        else:
            answer.append(0)

    return answer


def create_info(string, arr, idx, score):
    global dic
    if idx == 4:
        if string in dic:
            dic[string].append(score)
        else:
            dic[string] = [score]
        return

    create_info(string + arr[idx], arr, idx + 1, score)
    create_info(string + '-', arr, idx + 1, score)

# 당연히 시간초과
# 정확성은 통과

def solution(info, query):
    people = []
    scores = []
    answer = []
    dic = {}
    for person in info:
        infos = person.split(' ')
        score = infos[-1]
        infos = infos[:-1]
        p = ''.join(infos)
        people.append(p)
        dic[p] = int(score)
        scores.append(int(score))

    for queries in query:
        att = []
        q = queries.split(' and ')
        q_end = q[-1].split(' ')
        lang = q[0]
        job = q[1]
        js = q[2]
        food = q_end[0]
        score = int(q_end[1])
        query1 = []
        query2 = []
        query3 = []
        query4 = []

        if job == '-':
            query2.append('backend')
            query2.append('frontend')
        else:
            query2.append(job)

        if lang == '-':
            query1.append('java')
            query1.append('cpp')
            query1.append('python')
        else:
            query1.append(lang)

        if js == '-':
            query3.append('junior')
            query3.append('senior')
        else:
            query3.append(js)

        if food == '-':
            query4.append('chicken')
            query4.append('pizza')
        else:
            query4.append(food)

        ans = 0

        for q1 in query1:
            for q2 in query2:
                for q3 in query3:
                    for q4 in query4:
                        sentence = q1 + q2 + q3 + q4
                        for i in range(len(people)):
                            if people[i] == sentence and score <= scores[i]:
                                ans += 1
                        print(sentence)
        answer.append(ans)

    return answer


## 해설 참고한 풀이
## 바로 통과하네..

def solution(info, query):
    dic = {}
    answer = []
    for person in info:
        infos = person.split(' ')
        lang, job, exp, food, score = infos[0], infos[1], infos[2], infos[3], int(infos[4])
        langs = [lang, '-']
        jobs = [job, '-']
        exps = [exp, '-']
        foods = [food, '-']
        for l in langs:
            for j in jobs:
                for e in exps:
                    for f in foods:
                        sentence = l + j + e + f
                        if sentence not in dic:
                            dic[sentence] = [score]
                        else:
                            dic[sentence].append(score)

    for key in dic.keys():
        dic[key] = sorted(dic[key])
    for q in query:
        q = q.split(' and ')
        score = int(q[3].split(' ')[1])
        sent = q[0] + q[1] + q[2] + q[3].split(' ')[0]
        if sent in dic:
            people = dic[sent]
            answer.append(len(people) - lower_bound(people, score))
        else:
            answer.append(0)

    return answer


def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right
