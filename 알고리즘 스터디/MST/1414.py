N = int(input())
table = []
parent = [i for i in range(N+1)]
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

def atoi(char):
    if ord(char) >= ord('A'):
        if ord(char) >= ord('a'):
            return ord(char) - ord('a') + 1
        return ord(char) - ord('A') + 27

for _ in range(N):
    table.append(list(input()))

computer = []
total = 0

for i in range(0,N):
    for j in range(0,N):
        if table[i][j] == '0':
            continue
        computer.append((atoi(table[i][j]),i+1,j+1))
        total += atoi(table[i][j])

computer.sort()
for com in computer:
    length, first, second = com
    if find_parent(first) != find_parent(second):
        union(first,second)
        total -= length

supercom = parent[1]
flag = True
for i in range(2,N+1):
    if find_parent(i) != supercom:
        flag = False
        break

if flag:
    print(total)
else:
    print(-1)