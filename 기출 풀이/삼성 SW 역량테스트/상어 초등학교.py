from collections import deque
import heapq

N = int(input())

students = deque([])

# N번 학생이 선호하는 친구들 저장
student = [[] for _ in range(N * N + 1)]
for _ in range(N * N):
    inp = list(map(int, input().split()))
    students.append(inp)
    student[inp[0]].append(inp[1:])

# N * N 짜리 격자
graph = [[0 for _ in range(N)] for _ in range(N)]
# 인접한 학생 번호 넣어두기
adj_graph = [[[] for _ in range(N)] for _ in range(N)]
# 인접한 칸
delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
blank_count = [[0 for _ in range(N)] for _ in range(N)]


def check(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True

    return False


# 빈칸 개수
for y in range(N):
    for x in range(N):
        for d in delta:
            ny = y + d[0]
            nx = x + d[1]
            if not check(nx, ny):
                continue

            blank_count[y][x] += 1

while students:
    # 학생의 번호, 좋아하는 학생의 번호들
    student_num, num1, num2, num3, num4 = students.popleft()
    q = []
    for y in range(N):
        for x in range(N):
            if graph[y][x] != 0:
                continue
            count = 0
            if num1 in adj_graph[y][x]:
                count += 1

            if num2 in adj_graph[y][x]:
                count += 1

            if num3 in adj_graph[y][x]:
                count += 1

            if num4 in adj_graph[y][x]:
                count += 1

            blank = blank_count[y][x]
            heapq.heappush(q, [-count, -blank, y, x])

    count, blank, y, x = heapq.heappop(q)
    graph[y][x] = student_num
    for d in delta:
        ny = y + d[0]
        nx = x + d[1]
        if not check(nx, ny):
            continue
        adj_graph[ny][nx].append(student_num)
        blank_count[ny][nx] -= 1

answer = 0

for y in range(N):
    for x in range(N):
        num = graph[y][x]
        count = 0
        num1, num2, num3, num4 = student[num][0]

        if num1 in adj_graph[y][x]:
            count += 1

        if num2 in adj_graph[y][x]:
            count += 1

        if num3 in adj_graph[y][x]:
            count += 1

        if num4 in adj_graph[y][x]:
            count += 1

        if count == 1:
            answer += 1
        elif count == 2:
            answer += 10
        elif count == 3:
            answer += 100
        elif count == 4:
            answer += 1000

print(answer)
