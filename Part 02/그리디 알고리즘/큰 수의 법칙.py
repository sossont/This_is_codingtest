n,m,k = map(int, input().split())
num = list(map(int,input().split()))
num.sort(reverse=True) # 내림차순 정렬

first_num = num[0]
second_num = num[1]

answer = 0
plus_limit = 0
for i in range(0,m):
    if plus_limit == k:
        answer += second_num
        plus_limit = 0
    else:
        answer += first_num
        plus_limit += 1

print(answer)