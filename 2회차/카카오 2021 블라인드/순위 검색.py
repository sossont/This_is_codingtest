from collections import defaultdict

def solution(info, query):
    dic = defaultdict(list)
    bar = '-'
    for i in info:
        arr = i.split(' ')
        dfs('', dic, 0, arr)

    for key in dic.keys():
        dic[key].sort()

    answer = []
    for q in query:
        arr = q.split('and')
        second_q = arr[3].split(' ')
        target_num = int(second_q[2])
        quer = ''.join(arr[:3]).replace(' ', '') + second_q[1]
        answer.append(lower_bound(dic[quer], target_num))

    return answer


def lower_bound(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return len(arr) - left


def dfs(string, dic, idx, arr):
    if idx == 4:
        dic[string].append(int(arr[4]))
        return

    dfs(string + '-', dic, idx + 1, arr)
    dfs(string + arr[idx], dic, idx + 1, arr)