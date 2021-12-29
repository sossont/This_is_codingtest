N = int(input())

hour = 0
minute = 0
seconds = 0
answer = 0
for hour in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(hour) + str(m) + str(s):
                answer += 1

print(answer)
