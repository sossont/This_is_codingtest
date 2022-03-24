# 짝수일때 -> 0~2/n-1
# 홀수일때 -> 0~2/n


# 왼쪽 위가 0,0
# 오른쪽 아래가 n-1,n-1

## 2*(lock-1) + len(key)  가로 세로 길이
## (lock, lock) -> 0, 0
## (lock + len(key-1), lock + len(key)-1) -> n-1,n-1

def solution(key, lock):
    answer = True
    rotkey = key
    for _ in range(4):  # 4번 돌린다.
        ex_key = [[0 for _ in range(2 * len(lock) + len(key) - 2)] for _ in range(2 * len(lock) + len(key) - 2)]
        rotkey = rotateKey(rotkey)
        for i in range(2 * len(lock) + len(key) - 2):
            for j in range(2 * len(lock) + len(key) - 2):
                if len(lock) - 1 <= i <= len(lock) + len(key) - 2 and len(lock) - 1 <= j <= len(lock) + len(key) - 2:
                    ex_key[i][j] = rotkey[i - (len(lock) - 1)][j - (len(lock) - 1)]
                else:
                    ex_key[i][j] = 0

        for py in range(len(key) + len(lock) - 1):
            for px in range(len(key) + len(lock) - 1):
                print(py, px)
                flag = False
                for y in range(len(lock)):
                    if flag:
                        break
                    for x in range(len(lock)):
                        if lock[y][x] == 0 and ex_key[py + y][px + x] == 0:  # lock이 비어있는 공간에 무조건 맞아야 한다.
                            flag = True
                            break
                        if lock[y][x] == 1 and ex_key[py + y][px + x] == 1:
                            flag = True
                            break
                if not flag:
                    return True

    return False


def rotateKey(key):
    nkey = [[0 for _ in range(len(key))] for _ in range(len(key))]
    # (x,y) -> (y(x), x(y))
    for y in range(len(key)):
        for x in range(len(key)):
            # 1행 1열은 1행 n열로
            # n행 1열은 1행 1열로

            # 1행 n열은 n행 1열로
            # n행 n열은 n행 1열로
            nkey[x][len(key) - y - 1] = key[y][x]

    return nkey