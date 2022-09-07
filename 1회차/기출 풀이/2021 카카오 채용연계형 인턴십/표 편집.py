# Linked List 이용하여 해결

class Node:
    def __init__(self, idx):
        self.data = idx
        self.left = None
        self.right = None


class LinkedList:
    def __init__(self, node):
        self.head = node
        self.curNode = node  # 현재 행
        self.delete_nodes = []
        self.ans = [0] * 1000000

    def init(self, idx):  # curNode를 k번째 노드로 만들어준다.
        cur_node = self.head
        while cur_node.data != idx:
            cur_node = cur_node.right
        self.curNode = cur_node

    def insert(self, idx):
        new_node = Node(idx)
        cur_node = self.curNode
        cur_node.right = new_node
        new_node.left = cur_node
        self.curNode = new_node

    def up(self, idx):
        cur_node = self.curNode
        while idx > 0:
            if cur_node.left is None:
                break
            cur_node = cur_node.left
            idx -= 1
        self.curNode = cur_node

    def down(self, idx):
        cur_node = self.curNode
        while idx > 0:
            if cur_node.right is None:
                break
            cur_node = cur_node.right
            idx -= 1
        self.curNode = cur_node

    def delete(self):  # C
        cur_node = self.curNode
        if cur_node.right is None:  # 가장 마지막 행
            self.curNode = cur_node.left
        else:
            self.curNode = cur_node.right

        if cur_node == self.head:
            self.head = cur_node.right
            self.head.left = None
        else:
            cur_node.left.right = cur_node.right

        if cur_node.right is not None:
            cur_node.right.left = cur_node.left

        self.delete_nodes.append(cur_node)

    def recover(self):  # Z
        recover_node = self.delete_nodes.pop()
        if recover_node.left is None:
            self.head.left = recover_node
            self.head = recover_node
        else:
            recover_node.left.right = recover_node

        if recover_node.right is not None:
            recover_node.right.left = recover_node

    def finish(self):
        cur_node = self.head
        while cur_node is not None:
            self.ans[cur_node.data] = 1
            cur_node = cur_node.right


def solution(n, k, cmd):
    answer = ''
    init_node = Node(0)
    linked_list = LinkedList(init_node)
    for i in range(1, n):  # 0 ~ n까지 노드 삽입
        linked_list.insert(i)

    linked_list.init(k)
    for command in cmd:
        c = command.split(' ')
        if c[0] == 'D':
            idx = int(c[1])
            linked_list.down(idx)
        elif c[0] == 'C':
            linked_list.delete()
        elif c[0] == 'U':
            idx = int(c[1])
            linked_list.up(idx)
        elif c[0] == 'Z':
            linked_list.recover()

    linked_list.finish()
    for i in range(n):
        if linked_list.ans[i] == 1:
            answer += 'O'
        else:
            answer += 'X'

    return answer


# 정확성은 통과
# 시간 초과는 어떻게 해결하지..? insert, delete를 쓰지 말라는 건가?

def solution(n, k, cmd):
    answer = ''
    table = [i for i in range(n)]
    ans = [0 for _ in range(n)]
    delete = []
    # k를 화살표로 사용한다.
    for c in cmd:
        if c == 'Z':
            idx, val = delete.pop()
            if idx <= k:
                k += 1
            table.insert(idx, val)
        elif c == 'C':
            delete.append([k, table[k]])
            del table[k]
            if k == len(table):  # 마지막 행인경우
                k -= 1
        elif c[0] == 'U':
            k -= int(c[2:])
        elif c[0] == 'D':
            k += int(c[2:])

    for idx, val in delete:
        ans[val] = 1

    for a in ans:
        if a == 0:
            answer += 'O'
        else:
            answer += 'X'
    return answer
