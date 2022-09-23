def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in permutation(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + nxt


def solution(n, weak, dist):
    tmp_weak = weak[:]
    for w in weak:
        tmp_weak.append(n+w)

    answer = []
    for i, start in enumerate(weak):
        for case in permutation(dist, len(dist)):
            count = 1
            pos = start
            for friend in case:
                pos += friend
                if pos < tmp_weak[i+len(weak)-1]:
                    count += 1
                    for w in tmp_weak[i+1:]:
                        if w > pos:
                            pos = w
                            break
                else:
                    answer.append(count)
                    break

    answer.sort()
    if len(answer) == 0:
        return -1
    else:
        return answer[0]