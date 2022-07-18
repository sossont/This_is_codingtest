T = int(input())

def calc(n, array, place):
    while n > 0:
        x = n % 10
        array[x] += place
        n = n // 10

for test_case in range(1, T+1):
    start, end = map(int,input().split())
    arr = [0] * 10
    div = 1
    while start <= end:
        while start % 10 != 0 and start <= end:
            calc(start, arr, div)
            start += 1

        if start > end:
            break

        while end % 10 != 9 and start <= end:
            calc(end, arr, div)
            end -= 1

        for k in range(1, 10):
            arr[k] += (end // 10 - start // 10 + 1) * div

        div *= 10
        start = start // 10
        end = end // 10


    answer = 0
    for k in range(1, 10):
        answer += arr[k] * k
    print("#" + str(test_case) + " " + str(answer))


#7개 맞는 시간초과 나는 코드
T = int(input())
for test_case in range(1, T+1):
    A, B = map(int,input().split())
    arr = [0] * 10
    for k in range(A,B+1):
        num = str(k)
        for idx in range(len(num)):
            arr[int(num[idx])] += 1

    answer = 0
    for k in range(1, 10):
        answer += arr[k] * k
    print("#" + str(test_case) + " " + str(answer))