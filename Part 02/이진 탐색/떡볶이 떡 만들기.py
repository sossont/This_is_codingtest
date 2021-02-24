N, M = map(int, input().split())
height = list(map(int, input().split()))

start = 0
end = max(height)
result = 0

while start<=end:
    total = 0
    mid = (start + end) // 2
    for x in height:
        if x > mid:
            total += x - mid

    if total < M:
        end = mid -1
    else:
        start = mid + 1
        result = mid

print(result)