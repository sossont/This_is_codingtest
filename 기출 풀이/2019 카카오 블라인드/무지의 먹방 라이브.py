# 1차 시도 당연히 시간초과 날것 ( 정확성은 통과할 것 )
## 이 코드는 5분컷,, 시간 초과 어떻게 해결할까?

def solution(food_times, k):
    time = 0
    idx = 0
    answer = 0
    dic = {}
    while True:
        if idx == len(food_times):  # 끝에 도달
            idx = 0
            continue

        if food_times[idx] == 0:
            if len(dic) == len(food_times):
                return -1
            idx += 1
            dic[idx] = 1
            continue

        if time == k:
            answer = idx + 1
            break

        food_times[idx] -= 1
        time += 1
        idx += 1

    return answer

# 2차 시도
### 링크드 리스트로 2차 시도 해봤는데도 시간 줄이기 실패.

class Node:
    def __init__(self, time, idx):
        self.time = time
        self.idx = idx
        self.next = None
        self.prev = None



class LinkedList:
    def __init__(self, time, idx):
        node = Node(time, idx)
        self.head = node
        self.cur = node

    def insert(self, time, idx): # 링크드 리스트 끝에 추가
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        node = Node(time,idx)
        current_node.next = node
        node.prev = current_node

def solution(food_times, k):
    linked_list = LinkedList(food_times[0], 0)
    for i in range(1,len(food_times)):
        linked_list.insert(food_times[i],i)

    cur = linked_list.head
    while k>0:
        cur.time -= 1
        k -= 1

        if cur.time == 0:
            if cur == linked_list.head:
                if cur.next is None:    # 더 섭취할 음식이 없음
                    return -1
                linked_list.head = cur.next
            else:
                prev_node = cur.prev
                if cur.next is not None:    # 삭제 하는 과정
                    next_node = cur.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                else:
                    prev_node.next = None

        if cur.next is None:    # 다음 리스트로
            cur = linked_list.head
        else:
            cur = cur.next

    return cur.idx + 1

# 이분 탐색으로 풀어야 할 것 같은 느낌
# 3트
## 해설 보고 풀었다.
## 정렬 시켜서 묶어서 뺴는 방식으로 카운트 가짓 수를 크게 줄이는게 방법이다.
## 마지막에 인덱스 정렬하는 거를 캐치 못해서 오래걸렸다.

def solution(food_times, k):
    q = []
    for i in range(len(food_times)):
        q.append((food_times[i],i))
    q.sort()
    food_times.sort()
    times = list(set(food_times))
    times.sort()
    idx = 0
    qlen = len(q)

    for i in range(len(times)):
        while times[i] > q[idx][0]:
            idx += 1

        if i == 0:
            minus_time = times[0]
        else:
            minus_time = times[i] - times[i-1]

        k -= minus_time * (qlen - idx)   # 한 바퀴 쭉 먹어준다.
        if k < 0:   #만약 한 바퀴 쭉 돌았을 때 끝났으면,
            k += minus_time * (qlen - idx)
            idx_arr = []
            for j in range(idx,len(q)):
                idx_arr.append(q[j][1])
            idx_arr.sort()
            ans_idx = k % (qlen - idx)
            return idx_arr[ans_idx] + 1

    return -1
