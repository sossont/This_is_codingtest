'''
- 0.5솔, 효율성은 다 시간 초과. 정확성 통과.
- 딱봐도 시간 초과 날 것 같았음
- 시간 초과 해결하는 방법은 뭐가있을까

def solution(stones, k):

    if len(stones) == k:
        answer = max(stones)
        return answer
    if k == 1:
        answer = min(stones)
        return answer
    arr = []
    for idx in range(len(stones)):
        num = [stones[idx], idx]
        arr.append(num)

    arr.sort()  # 정렬은 한번만 하면 된다.
    before = 0
    answer = 0
    idxarr = [0 for _ in range(len(arr))]

    for num in arr:
        if before != num[0]:    # 숫자가 커졌음
            cont = 1
            for i in range(len(arr) - 1):
                if idxarr[i] != 0 and idxarr[i+1] != 0:
                    cont += 1
                else:
                    cont = 1
                if cont == k:
                    return answer

            before = num[0]
            answer = num[0]

        idxarr[num[1]] = 1

'''