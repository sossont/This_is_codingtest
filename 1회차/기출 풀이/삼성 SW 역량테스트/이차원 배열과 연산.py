# 1시간 정도..?

r,c,k = map(int,input().split())
arr = []
for _ in range(3):
    arr.append(list(map(int,input().split())))

# 수의 등장 횟수가 커지는 순, 수가 커지는 순
def R(array):
    max_len = 0
    # 0행부터 r-1행 까지
    tmp_arr = []
    for i in range(len(array)):
        tmp = []
        q = []
        count_arr = [0] * 101  # 1부터 100까지
        for num in array[i]:
            # 한 행의 개수 조사
            count_arr[num] += 1

        for num in range(1,101):
            if count_arr[num] == 0:
                continue
            # 수의 등장횟수와 수가 커지는 순서로
            q.append([count_arr[num],num])

        q.sort()
        while q:
            count,num = q.pop(0)
            tmp.append(num)
            tmp.append(count)
            # 100을 넘어가는 경우 나머지는 버린다.
            if len(tmp) == 0:
                break
        max_len = max(max_len,len(tmp))
        tmp_arr.append(tmp)

    for t in tmp_arr:
        while len(t) < max_len:
            t.append(0)

    return tmp_arr

def C(array):
    # 행 열을 바꿔줄 함수
    tmp_arr = [[0] * len(array) for _ in range(len(array[0]))]

    # 행 열을 바꾼다.
    for y in range(len(array)):
        for x in range(len(array[0])):
            tmp_arr[x][y] = array[y][x]


    tmp_arr = R(tmp_arr)
    ret_arr = [[0] * len(tmp_arr) for _ in range(len(tmp_arr[0]))]

    for y in range(len(tmp_arr)):
        for x in range(len(tmp_arr[0])):
            ret_arr[x][y] = tmp_arr[y][x]

    return ret_arr

answer = 0
while True:
    if r-1 < len(arr) and c-1 < len(arr[0]) and arr[r-1][c-1] == k:
        break
    if len(arr) < len(arr[0]):
        arr = C(arr)
    else:
        arr = R(arr)

    answer += 1
    if answer > 100:
        answer = -1
        break

print(answer)