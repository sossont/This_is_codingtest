from collections import deque

MAX = 200
INF = 987654321
flow = [[0] * MAX for _ in range(MAX)]
capacity = [[0] * MAX for _ in range(MAX)]

def atoi(char):
    return ord(char) - ord('A')

def BFS(source, sink):
    queue = deque()
    queue.append(source)
    parent = [-1 for _ in range(MAX)]
    parent[source] = source
    while queue and parent[sink] == -1:
        here = queue.popleft()
        for there in range(MAX):
            if parent[there] == -1 and capacity[here][there] > flow[here][there]:
                queue.append(there)
                parent[there] = here
    return parent

def networkFlow(source, sink):
    ret = 0
    while True:
        parent = BFS(source,sink)
        if parent[sink] == -1:
            break
        amount = INF
        p = sink
        while p != source:
            amount = min(capacity[parent[p]][p] - flow[parent[p]][p], amount)
            p = parent[p]
        p = sink
        while p != source:
            flow[parent[p]][p] += amount
            flow[p][parent[p]] -= amount
            p = parent[p]
        ret += amount
    return ret

## Input Layer
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = []
for i in range(M):
    c = list(map(int,input().split()))
    C.append(c)



x1, x2 = atoi('A'), atoi('Z')
print(networkFlow(x1,x2))

