N = int(input())
parent = [i for i in range(N+1)]

costs = []
for i in range(1,N+1):
    w = int(input())
    costs.append((w,0,i))

table = [list(range(N+1))]
for _ in range(N):
    t = list(map(int,input().split()))
    t.insert(0,0)
    table.append(t)

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

for i in range(1,N+1):
    for j in range(i+1,N+1):
        if i != j:
            costs.append((table[i][j],i,j))

answer = 0
costs.sort()
for c in costs:
    cost, non1, non2 = c
    if find_parent(non1) != find_parent(non2):
        union(non1,non2)
        answer += cost

print(answer)
