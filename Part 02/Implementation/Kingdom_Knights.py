dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

two_words = list(input())

x = int(ord(two_words[0]) - ord('a') + 1)
y = int(two_words[1])
answer = 0
for i in range(8):
    if (x+dx[i]) < 1 or (y+dy[i]) < 1 or (x+dx[i]) > 8 or (y+dy[i]) > 8:
        continue
    answer += 1

print(answer)
