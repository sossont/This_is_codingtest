def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = []
    bin_arr2 = []
    for num in arr1:
        bin_num = pow(2, n - 1)  # 2의 n-1승
        bin_str = ""
        while True:
            if num >= bin_num:  # 1인 경우
                num -= bin_num
                bin_str += "#"
            else:
                bin_str += " "

            bin_num = bin_num / 2  # 2로 나눈다
            if bin_num == 1:
                if num == 1:
                    bin_str += "#"
                else:
                    bin_str += " "
                break
        bin_arr1.append(bin_str)

    for num in arr2:
        bin_num = pow(2, n - 1)  # 2의 n-1승
        bin_str = ""
        while True:
            if num >= bin_num:  # 1인 경우
                num -= bin_num
                bin_str += "#"
            else:
                bin_str += " "

            bin_num = bin_num / 2  # 2로 나눈다
            if bin_num == 1:
                if num == 1:
                    bin_str += "#"
                else:
                    bin_str += " "
                break
        bin_arr2.append(bin_str)

    for i in range(len(bin_arr1)):
        idx = 0
        ans_str = ""
        while idx < n:
            if bin_arr1[i][idx] == "#" or bin_arr2[i][idx] == "#":
                ans_str += "#"
            else:
                ans_str += " "
            idx += 1

        answer.append(ans_str)

    return answer


# 비트 연산 풀이

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        string = ''
        ans = bin(arr1[i] | arr2[i])
        ans = ans[2:]
        if len(ans) != n:
            tmp = " " * (n - len(ans))
            ans = tmp + ans
        for a in ans:
            if a == '1':
                string += '#'
            else:
                string += ' '
        answer.append(string)

    return answer