# 10분 걸림!

def solution(id_list, report, k):
    dic = {}
    base_dic = {}
    for r in report:
        ids = r.split(' ')
        base_id, report_id = ids[0], ids[1]
        if base_id in base_dic:
            if report_id not in base_dic[base_id]:
                base_dic[base_id].append(report_id)
        else:
            base_dic[base_id] = [report_id]

    for key in base_dic.keys():
        for report_id in base_dic[key]:
            if report_id in dic:
                dic[report_id] += 1
            else:
                dic[report_id] = 1
    answer = []

    for key in id_list:
        result = 0
        if key in base_dic:
            for report_id in base_dic[key]:
                if dic[report_id] >= k:
                    result += 1

        answer.append(result)

    return answer