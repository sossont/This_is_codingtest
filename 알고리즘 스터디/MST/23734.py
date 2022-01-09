N,M = map(int,input().split())
warp = []
parent = [i for i in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    warp.append([c,a,b])

ext = list(map(int,input().split())) # 비상 탈출구 설치에 드는 시간

for i in range(1,N+1):
    warp.append([ext[i-1],0,i])

warp.sort() # 오름차순 정렬

answer = 0

def find_parent(p):
    if p != parent[p]:
        parent[p] = find_parent(parent[p])
    else:
        return parent[p]

def union(n1,n2):
    p1 = find_parent(n1)
    p2 = find_parent(n2)
    parent[p1] = p2

for n1,n2,t in warp:
    if find_parent(n1) != find_parent(n2):
        union(n1,n2)
        answer += t

print(answer)
