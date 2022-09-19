def solution(s):
    answer = float('inf')
    MAX = len(s) // 2  # 자를 수 있는 최대
    if len(s) < 4:
        return len(s)
    for length in range(1, MAX + 1):
        arr = []
        start = 0
        while start + length < len(s):
            string = s[start:start + length]
            arr.append(string)
            start += length

        if start < len(s):
            arr.append(s[start:])

        count = 1
        string = ""
        for idx in range(1, len(arr)):
            if arr[idx] == arr[idx - 1]:
                count += 1
            else:
                if count == 1:
                    string += arr[idx - 1]
                else:
                    string += str(count) + arr[idx - 1]
                    count = 1

        if count == 1:
            string += arr[len(arr) - 1]
        else:
            string += str(count) + arr[len(arr) - 1]

        answer = min(answer, len(string))

    return answer