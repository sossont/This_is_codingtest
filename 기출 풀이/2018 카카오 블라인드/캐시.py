from collections import deque


def solution(cacheSize, cities):
    answer = 0
    lru = deque()

    if cacheSize == 0:
        return 5 * len(cities)

    # 대소문자 구분없이 만들기
    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    # lru 구현
    for city in cities:
        if city in lru:
            answer += 1
            lru.remove(city)
            lru.append(city)  # 맨 뒤로 보낸다
        else:
            answer += 5
            if len(lru) == cacheSize:
                lru.popleft()
            lru.append(city)

    return answer