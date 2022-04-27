# 아 한칸 이동 하는 거 못봐서 1시간...

N, K = map(int,input().split())
belt = list(map(int,input().split()))

# 0번부터 2n-1번까지 있는데,
# 0번부터 2n-2번은 한칸 앞으로 이동, 2n-1번은 0번으로 이동
# 0번 칸이 있는 위치, 올리는 위치 , n-1번 칸이 있는 위치 : 내리는 위치

uc = [0] * N    # 위에 컨테이너,
dc = [0] * N    # 아래 컨테이너

for i in range(len(belt)):
    if i < N:
        uc[i] = belt[i]
    else:
        dc[i-N] = belt[i]


# True : 탈 수 있음
uc_robot = [True] * N

# 회전 하는 함수
def rotate():
    global uc
    global dc
    global uc_robot

    tmp_ucr = [True]
    tmp_uc = [dc[N-1]]
    tmp_dc = [uc[N-1]]
    for n in range(N-1):
        tmp_uc.append(uc[n])
        tmp_dc.append(dc[n])
        tmp_ucr.append(uc_robot[n])

    if not tmp_ucr[N-1]:    # 내리는 위치 도달하면 내린다.
        tmp_ucr[N-1] = True

    uc = tmp_uc
    dc = tmp_dc
    uc_robot = tmp_ucr

def move(idx):
    bef_idx = idx
    global uc_robot
    global uc
    nxt = idx + 1
    if uc_robot[nxt] and uc[nxt] >= 1:
        # 움직일 수 있을 때 만큼 움직임
        uc_robot[bef_idx] = True
        uc[nxt] -= 1
        uc_robot[nxt] = False
    # 내리는 위치에 도달하면 내린다.
    if nxt == N-1:
        uc_robot[N-1] = True

def new_robot():
    global uc_robot
    global uc
    if uc[0] >= 1:
        uc_robot[0] = False
        uc[0] -= 1


answer = 0
while True:
    answer += 1
    rotate()
    # 가장 먼저 벨트에 올라간 로봇부터
    for i in range(N - 2, 0, -1):
        if not uc_robot[i]:
            move(i)
    new_robot()
    count = 0
    for i in range(len(uc)):
        if uc[i] == 0:
            count += 1

        if dc[i] == 0:
            count += 1

    if count >= K:
        break


print(answer)