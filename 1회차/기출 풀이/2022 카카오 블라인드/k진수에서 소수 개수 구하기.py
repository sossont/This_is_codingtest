# 15분 정도

import math

# 소수 판별 알고리즘
def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def convert(n, q):
    base = ''

    while n > 0:
        n, mod = divmod(n, q)
        base += str(mod)

    return base[::-1]


def solution(n, k):
    answer = 0
    int_list = []
    zero_idx = 0
    num = str(convert(n, k))

    for idx in range(len(num)):
        if num[idx] == '0':
            new_num = num[zero_idx:idx]
            zero_idx = idx + 1
            if len(new_num) == 0:
                continue
            int_list.append(int(new_num))

    new_num = num[zero_idx:len(num)]
    if len(new_num) != 0:
        int_list.append(int(new_num))

    for num in int_list:
        if is_prime(num):
            answer += 1
    return answer