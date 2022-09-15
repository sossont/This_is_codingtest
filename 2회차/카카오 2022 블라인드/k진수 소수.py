# 약 10분

import math

def checkPrime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    arr = []
    answer = 0
    current = n
    count = 0
    while current > 0:
        current, mod = divmod(current, k)
        arr.append(mod)
    arr.reverse()
    string = ''
    for n in arr:
        string += str(n)

    spl = string.split('0')
    for num in spl:
        if len(num) == 0:
            continue
        if checkPrime(int(num)):
            answer += 1

    return answer