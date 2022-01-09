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
