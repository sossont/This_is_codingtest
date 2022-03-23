# 6,7번 런타임 에러? -> 재귀 한도 문제였다.
# 이건 시간안에 못풀고 번외로 푼 것.
import sys

sys.setrecursionlimit(20000)
pre_nodes = []
post_nodes = []


class Node:
    def __init__(self, x, idx):
        self.left = None
        self.right = None
        self.x = x
        self.idx = idx


class Tree:
    def __init__(self, root):
        self.root_node = root
        self.current_node = None

    def insert(self, x, idx):
        self.current_node = self.root_node
        while True:
            if self.current_node.x < x:  # x값이 더 크니까 오른쪽으로 간다.
                if self.current_node.right is not None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(x, idx)
                    break
            else:  # 왼쪽으로 간다.
                if self.current_node.left is not None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(x, idx)
                    break

    def preOrder(self, node):
        pre_nodes.append(node.idx)
        if node.left is not None:
            self.preOrder(node.left)
        if node.right is not None:
            self.preOrder(node.right)

    def postOrder(self, node):
        if node.left is not None:
            self.postOrder(node.left)
        if node.right is not None:
            self.postOrder(node.right)
        post_nodes.append(node.idx)


def solution(nodeinfo):
    # 길이가 1인 경우
    if len(nodeinfo) == 1:
        return [[1], [1]]

    nodes = []
    for i in range(len(nodeinfo)):
        x = nodeinfo[i][0]
        y = nodeinfo[i][1]
        nodes.append((y, x, i + 1))

    nodes.sort(reverse=True)  # y값 큰 순으로 정렬.

    tree = Tree(Node(nodes[0][1], nodes[0][2]))

    for i in range(1, len(nodes)):
        tree.insert(nodes[i][1], nodes[i][2])

    answer = []

    tree.preOrder(tree.root_node)
    tree.postOrder(tree.root_node)
    answer.append(pre_nodes)
    answer.append(post_nodes)
    return answer