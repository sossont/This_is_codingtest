import math

n = int(input())
nodes = []
def calc(x1,y1,x2,y2):  # 두 점 사이의 거리
    return math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))

def findparent(p):
    if p == parent[p]:
        return p
    else:
        parent[p] = findparent(parent[p])
        return parent[p]

for i in range(n):
    x,y = map(float,input().split())
    nodes.append([x,y])

dist = []
for i in range(len(nodes)):
    x1 = nodes[i][0]
    y1 = nodes[i][1]
    for j in range(i+1,len(nodes)):
        x2,y2 = nodes[j][0],nodes[j][1]
        result = calc(x1,y1,x2,y2)
        dist.append([result,i,j])

dist.sort()
parent = [i for i in range(n)]
answer = 0

for dis in dist:
    cost,node1,node2 = dis[0],dis[1],dis[2]
    parent1 = findparent(node1)
    parent2 = findparent(node2)
    if parent1 != parent2:
        parent[parent2] = parent1
        answer += cost

print(format(answer,".2f"))
