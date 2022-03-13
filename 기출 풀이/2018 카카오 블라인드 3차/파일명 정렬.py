def solution(files):
    idx = 0
    heads = []
    head_dic = {}
    numbers = []
    tails = []
    index = 0
    answer = []
    org_num = []
    org_heads = []
    # HEAD / NUMBER / TAIL 분류
    for file in files:
        idx = 0
        num_flag = False
        head = ""
        number = ""
        tail = ""
        while idx < len(file):
            if "0" <= file[idx] <= "9":
                if not num_flag:
                    num_flag = True
                number += file[idx]
            else:
                if num_flag:
                    break
                else:
                    head += file[idx]
            idx += 1

        low_head = head.lower()
        heads.append((low_head, index))
        org_heads.append(head)
        if low_head in head_dic:
            head_dic[low_head] += 1
        else:
            head_dic[low_head] = 1

        org_num.append(number)
        numbers.append((int(number), index))

        tails.append(file[idx:])

        index += 1

    print(numbers)
    # 풀이 시작
    heads.sort()  # head 정렬
    head_idx = 0
    print(heads)
    while head_idx < len(heads):
        head, idx = heads[head_idx]
        count = head_dic[head]
        nums = []
        for i in range(head_idx, head_idx+count):
            j = heads[i][1]
            print(j)
            nums.append(numbers[j])
        # nums = numbers[idx:idx + count]  # 같은 문자열끼리 숫자 비교하게 숫자 가져오기
        nums.sort()  # 숫자 정렬
        print(count, nums)
        for num, ind in nums:
            string = org_heads[ind] + org_num[ind] + tails[ind]
            answer.append(string)

        head_idx += count

    return answer