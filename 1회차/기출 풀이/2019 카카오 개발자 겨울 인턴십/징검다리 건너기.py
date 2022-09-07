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

# 이분 탐색 이용해야 풀리는 문제
# 어렵다.
def solution(stones, k):
    answer = 0
    left = 0
    right = 200000000
    while left <= right:
        mid = int( (left+right) / 2)
        arr = []
        count = 0

        for stone in stones:
            num = stone - mid
            if count < k:
                if num <= 0:
                    count += 1
                else:
                    count = 0

        if count < k:  # 가능
            left = mid+1
            answer = mid + 1
        else: # 불가능
            right = mid-1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))