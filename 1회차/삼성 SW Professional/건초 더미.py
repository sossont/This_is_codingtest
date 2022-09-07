T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    total = 0
    for _ in range(N):
        dummy = int(input())
        total += dummy
        arr.append(dummy)

    target = total // N
    arr.sort()
    answer = 0
    for d in arr:
        if d > target:
            break
        answer += target - d

    print("#" + str(test_case) + " " + str(answer))
