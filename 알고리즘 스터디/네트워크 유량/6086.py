from collections import deque

MAX = 126
INF = 987654321
N = int(input())

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


for _ in range(N):
    pipe1, pipe2, velocity = input().split()
    pipe1, pipe2 = atoi(pipe1), atoi(pipe2)
    velocity = int(velocity)
    capacity[pipe1][pipe2] += velocity
    capacity[pipe2][pipe1] += velocity

x1, x2 = atoi('A'), atoi('Z')
print(networkFlow(x1,x2))

