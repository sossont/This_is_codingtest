'''
- 0.5솔, 효율성은 다 시간 초과. 정확성 통과.
- 딱봐도 시간 초과 날 것 같았음
- 시간 초과 해결하는 방법은 뭐가있을까
'''
def solution(stones, k):
    answer = 0
    left = 0
    right = max(stones)
    while left <= right:
        mid = int( (left+right) / 2)
        arr = []
        count = 0
        for stone in stones:
            arr.append(stone - mid)
        print(arr)

        for num in arr:
            if count < k:
                if num <= 0:
                    count += 1
                else:
                    count = 0

        if count < k:  # 가능
            left = mid+1
        else: # 불가능
            right = mid-1
            answer = mid

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))