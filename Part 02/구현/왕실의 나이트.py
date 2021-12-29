now = input()
x = now[0]
y = int(now[1])

alpha = ['z','a','b','c','d','e','f','g','h']
for i in range(len(alpha)):
    if x == alpha[i]:
        x = i    # 숫자 좌표로 변환

answer = 0

first_dx = [2,-2]
first_dy = [1,-1]
second_dx = [1,-1]
second_dy = [2,-2]

for i in range(2):
    nx = x + first_dx[i]
    if 1 <= nx <= 8:
        for j in range(2):
            ny = y + first_dy[j]
            if 1 <= ny <= 8:
                answer += 1


for i in range(2):
    ny = y + second_dy[i]
    if 1 <= ny <= 8:
        for j in range(2):
            nx = x + second_dx[j]
            if 1 <= nx <= 8:
                answer += 1

print(answer)