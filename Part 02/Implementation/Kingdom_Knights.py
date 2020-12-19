"""
1. 플레이어의 반시계 방향으로 90도 회전한 방향부터 차례때로 갈 곳을 정함.
2. 그 방향에 아직 가보지 않은 칸이 존재한다면 그쪽으로 한 칸을 전진한다. 가보지 않은 칸이 없다면, 회전한 채로 1단계로 돌아감.
3. 네방향 모두가보거나 바다면, 그래도 뒤로 감. 뒤가 바다면 멈춘다.
"""

N, M = map(int,input().split())     #  첫째 줄에 N,M을 공백으로 구분하여 입력.
character = list(map(int,input().split()))
map1 = []
for i in range(N):
    map2 = list(map(int,input().split()))
    map1.append(map2)

print(character, map1)

