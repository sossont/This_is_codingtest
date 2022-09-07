def solution(s):
    answer = len(s)
    slen = len(s)
    for i in range(1, len(s) - 1):  # 1~1000개 단위로 문자열을 자른다.
        num = 0
        arr = []
        while True:
            if num >= slen:
                if s[num:] == "":
                    break

                arr.append(s[num:])
                break

            arr.append(s[num:num + i])
            num += i

        total = 0
        count = 1

        for j in range(1, len(arr)):
            if arr[j] == arr[j - 1]:  # 이전거랑 같으면 카운트 증가
                count += 1
            else:  # 다를때
                if count != 1:  # 이전에 압축이 되는 거면 숫자 길이만큼 넣어주기
                    total += len(str(count))
                count = 1
                total += i  # 이전 문자열 추가해주기

        total += len(arr[len(arr) - 1])
        if count != 1:
            total += len(str(count))

        answer = min(answer, total)
    return answer