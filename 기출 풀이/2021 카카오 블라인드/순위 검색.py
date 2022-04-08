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
