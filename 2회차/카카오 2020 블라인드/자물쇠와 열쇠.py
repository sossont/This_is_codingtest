def solution(key, lock):
    M = len(key) # M*M
    N = len(lock) # N*N

    # 회전 해야 하니까 4번 시도
    for _ in range(4):
        key = rotate(key)
        ex_key = [[0 for _ in range(2*N+M-2)] for _ in range(2*N+M-2)]

        for y in range(N-1, M-1+N):
            for x in range(N-1, M+N-1):
                ex_key[y][x] = key[y-(N-1)][x-(N-1)]

        for sy in range(M+N-1):
            for sx in range(M+N-1):

                flag = False

                for y in range(N):
                    if flag:
                        break

                    for x in range(N):
                        if lock[y][x] == 0 and ex_key[sy+y][sx+x] == 0:
                            flag = True
                            break

                        if lock[y][x] == 1 and ex_key[sy+y][sx+x] == 1:
                            flag = True
                            break

                if not flag:
                    return True



    return False

# key 회전시켜서 return 해주는 함수
def rotate(arr):
    tmp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for y in range(len(arr)):
        for x in range(len(arr)):
            tmp[x][len(arr)-1-y] = arr[y][x]

    return tmp