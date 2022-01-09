# 처음에는 발전소를 체크하는 함수를 따로 만들어주었다.
# 그렇게 하니 시간 초과 발생.
# 발전소를 0번 노드라고 생각하고, 발전소에 연결 된 것은 다 parent = 0 이 되게하면 된다.
N,M,K = map(int,input().split())
g = list(map(int,input().split()))
gen = list(range(N+1))
cables = []
parent = [i for i in range(N+1)]

for i in g:
    parent[i] = 0

def find_parent(p):
    if p != parent[p]:
        parent[p] = find_parent(parent[p])
    return parent[p]

def union(n1,n2):
    p1 = find_parent(n1)
    p2 = find_parent(n2)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2

for _ in range(M):
    u,v,w = map(int,input().split())
    cables.append([w, u, v])

cables.sort()
answer = 0
for cable in cables:
    cost, city1, city2 = cable[0],cable[1],cable[2]
    if find_parent(city1) != find_parent(city2):
        union(city1,city2)
        answer += cost

print(answer)
