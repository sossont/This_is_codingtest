"""
1. 플레이어의 반시계 방향으로 90도 회전한 방향부터 차례때로 갈 곳을 정함.
2. 그 방향에 아직 가보지 않은 칸이 존재한다면 그쪽으로 한 칸을 전진한다. 가보지 않은 칸이 없다면, 회전한 채로 1단계로 돌아감.
3. 네방향 모두가보거나 바다면, 그래도 뒤로 감. 뒤가 바다면 멈춘다.
"""

N, M = map(int,input().split())     #  첫째 줄에 N,M을 공백으로 구분하여 입력.
A,B,d = map(int,input().split())    # B가 x좌표, A가 y좌표.
dx = [0,1,0,-1] # 북, 동, 남, 서 d 순서대로.
dy = [1,0,-1,0]
isvisited = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]

map1 = []
for i in range(N):
    map2 = list(map(int,input().split()))
    map1.append(map2)   # map1 을 2차원 리스트로 만들어버리기! map2는 안쓰고 map1만 쓸거임.

answer = 0
nocount = 0
d -= 1  # 현재 방향을 기준으로 왼쪽 방향부터 살피니까.

while True:
    if nocount == 4:    # 카운트가 4면 갈데가 없는거. 뒤로 가야함
        newd = d - 2
        if newd < 0:    # 뒤로 갈라고
            newd + 4

        if map1[A+dy[newd]][B+dx[newd]] == 1:    # 뒤로 갔는데 바다인 경우면 종료.
            print(answer)
            exit()  # 종료

        answer += 1
        A = A+dy[newd]
        B = B+dx[newd]
        continue

    if d < 0:
        d = 3   # 북쪽에서 서쪽으로 넘어가는것.

    newy, newx = A+dy[d], B+dx[d]

    if map1[newy][newx] == 0 and not isvisited[newy][newx]: # 움직일 수 있는 경우(방문안했고, 육지임). 이동하자.
        answer += 1
        isvisited[newy][newx] = True
        A = newy    # 케릭터가 있는 좌표 업데이트.
        B = newx
        nocount = 0 # 움직였으니까 다시 카운트 0으로 만들어야함.
        continue


    d -= 1  # 가보지 않은 칸이 없으니까 왼쪽 방향으로 회전만 하고 다시 돌아가!
    nocount += 1