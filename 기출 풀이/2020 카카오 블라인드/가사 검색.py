# 트라이 구현해서 통과!!

## 와일드 카드 문자가 존재함.
## 단어 길이별로 트라이를 만들면 될 것 같다.

class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}  # 아래 노드들 연결
        self.count = 0 # 이 다음에 와일드 카드가 올 것을 대비해 여기 아래로 단어가 몇개 있는지 확인.

class Trie:
    def __init__(self):
        self.head = Node(None)
        self.count = 0

    def insert(self, string):
        current_node = self.head
        for char in string:
            current_node.count += 1
            if char not in current_node.children:   # abc가 들어왔을때, b가 child에 없으면 b를 아래에 넣는 것.
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]

    def isin(self, string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

    def search(self, string):   # 있다는 걸 전제로 찾는다.
        current_node = self.head
        for char in string:
            current_node = current_node.children[char]
        return current_node.count

    def total(self):    # 이 길이의 트라이 총 문자열 개수
        current_node = self.head
        for key in current_node.children:
            print(key)
            self.count += current_node.children[key].count





def solution(words, queries):
    # 길이 별로 트라이를 어떠게 나눌것인가?
    front_trie = {}
    back_trie = {}
    for word in words:  # 트라이에 문자 삽입
        word_len = len(word)
        if word_len not in front_trie:
            front_trie[word_len] = Trie()
            back_trie[word_len] = Trie()
        front_trie[word_len].insert(word)
        back_trie[word_len].insert(word[::-1])

    # 길이별 총 문자열 수 업데이트
    for key in front_trie:
        front_trie[key].total()
        back_trie[key].total()

    answer = []
    for query in queries:
        query_len = len(query)

        if query_len not in front_trie:
            answer.append(0)
            continue

        if query[0] == '?': # 첫 문자가 와일드카드면
            reversed_query = query[::-1].split('?')[0]
            print(reversed_query)
            if reversed_query == '':   # 그냥 쿼리 전체가 와일드카드면
                answer.append(back_trie[query_len].count)
            else:
                if back_trie[query_len].isin(reversed_query):
                    answer.append(back_trie[query_len].search(reversed_query))
                else:
                    answer.append(0)

        elif query[-1] == '?':  # 마지막 문자가 와일드 카드면
            front_query = query.split('?')[0]
            if front_trie[query_len].isin(front_query):
                answer.append(front_trie[query_len].search(front_query))
            else:
                answer.append(0)
        else: # 그낭 full 문자면
            if front_trie[query_len].isin(query):
                answer.append(1)
            else:
                answer.append(0)

    return answer

# 효율성 1,2,3번 통과 못함
# 0.5솔

def solution(words, queries):
    answer = []
    for query in queries:
        match = 0
        for word in words:
            if len(word) != len(query):
                continue
            ismatch = True
            for i in range(len(query)
                           ):
                if query[i] == '?' or word[i] == query[i]:
                    continue
                else:
                    ismatch = False
                    break

            if ismatch:
                match += 1
        answer.append(match)

    return answer

