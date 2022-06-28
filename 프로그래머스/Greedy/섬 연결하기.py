parent = [0] * 100

def find(p):
    global parent
    if parent[p] != p:
        parent[p] = find(parent[p])
    return parent[p]

def union(n1, n2):
    p1 = find(n1)
    p2 = find(n2)
    if p1 <= p2:
        parent[p2] = p1
    else:
        parent[p1] = p2

def solution(n, costs):
    for i in range(n):
        parent[i] = i

    edges = []
    for a, b, c in costs:
        edges.append((c,b,a))

    edges.sort()
    answer = 0
    for cost, a, b in edges:
        if find(a) != find(b):
            union(a,b)
            print(a,b,cost)
            answer += cost

    return answer