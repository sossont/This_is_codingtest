# 소요시간 : 1시간?
# 10번 제발..
# 결국 굴복하고 정규 표현식 써서 풀었다.
import re
def solution(word, pages):
    answer = 0
    link_counts = []  # 외부 링크 수
    normal_counts = []  # 기본 점수
    link_idx = {}  # 링크 별 인덱스 값
    idx_link = {}
    linkToLink = [[] for _ in range(21)]
    word = word.lower()  # 소문자로만 비교하자.

    # 기본 점수
    for k in range(len(pages)):
        page = pages[k]
        word_len = len(word)
        score = 0

        for i in range(len(page) - word_len):
            if page[i].lower() == word[0]:  # 첫글자가 같을 때,

                if 'a' <= page[i - 1].lower() <= 'z':  # 앞에 연속된 문자가 있으면
                    continue

                is_same = True
                for j in range(word_len):
                    if word[j] != page[i + j].lower():
                        is_same = False
                        break

                if is_same:
                    if 'a' <= page[i + word_len].lower() <= 'z':  # 뒤에 연속된 문자가 있으면
                        continue
                    else:
                        score += 1  # 기본 점수 + 1
                        continue

        normal_counts.append(score)

    for k in range(len(pages)):
        page = pages[k]
        real_link = re.search(r'(<meta property.+content=")(https://.*)"/>', page).group(2)  # 현재 url검색
        link_idx[k] = real_link  # 링크 - 인덱스, 인덱스 - 링크 둘 다 저장
        idx_link[real_link] = k

    # 링크 점수 구하기
    for k in range(len(pages)):
        page = pages[k]
        real_link = re.findall(r'<a href="https://\S*">', page)  # 외부 링크 url 전부 검색
        link_counts.append(len(real_link))
        for link in real_link:
            l = link[9:-2]
            print(l)
            if l in idx_link:
                idx = idx_link[l]  # 연결된 링크의 인덱스 번호
                linkToLink[idx].append(k)

    scores = []
    for i in range(len(pages)):
        link_score = 0
        if len(linkToLink[i]) != 0:
            for idx in linkToLink[i]:  # 이 링크로 이어지는 링크들
                link_score += normal_counts[idx] / link_counts[idx]

        scores.append(link_score + normal_counts[i])

    max_score = max(scores)

    for i in range(len(pages)):
        if scores[i] == max_score:
            answer = i
            break

    return answer

"""
대체 왜 10번 테케만 통과를 못하는지 모르겠다.
def solution(word, pages):
    answer = 0
    link_counts = []  # 외부 링크 수
    normal_counts = []  # 기본 점수
    link_idx = {}  # 링크 별 인덱스 값
    idx_link = {}
    linkToLink = [[] for _ in range(21)]
    word = word.lower()  # 소문자로만 비교하자.

    # 기본 점수
    for k in range(len(pages)):
        page = pages[k]
        word_len = len(word)
        is_tag = False
        score = 0

        for i in range(len(page) - word_len):
            if page[i] == '<':  # <~~~~>는 태그 안에 있는 글이다.
                is_tag = True

            if page[i] == '>':
                is_tag = False

            if not is_tag:  # 태크 안에 있는게 아니면
                if page[i].lower() == word[0]:  # 첫글자가 같을 때,
                    if 'a' <= page[i - 1].lower() <= 'z':  # 앞에 연속된 문자가 있으면
                        continue

                    is_same = True
                    for j in range(word_len):
                        if word[j] != page[i + j].lower():
                            is_same = False
                            break

                    if is_same:
                        if 'a' <= page[i + word_len].lower() <= 'z':  # 뒤에 연속된 문자가 있으면
                            continue
                        else:
                            score += 1  # 기본 점수 + 1
                            continue

        normal_counts.append(score)

    for k in range(len(pages)):
        page = pages[k]
        string = page.split(' ')  # 공백 기준으로 나누기
        find_url = False  # 처음에 메타값에서 찾아야 한다.

        # 이 웹페이지 링크 구하기
        for p in string:
            if find_url:
                break

            if "content" in p and not find_url:
                new_link = p[9:]
                # 링크 구하기
                for i in range(len(new_link) - 2):
                    if new_link[i] == '\"' and new_link[i + 1] == "/" and new_link[i + 2] == ">":
                        real_link = new_link[:i]

                        if real_link in idx_link:  # 이거 추가하니까 9번 통과
                            continue

                        link_idx[k] = real_link  # 링크 - 인덱스, 인덱스 - 링크 둘 다 저장
                        idx_link[real_link] = k
                        find_url = True
                        break

    # 링크 점수 구하기
    for k in range(len(pages)):
        page = pages[k]
        link_count = 0  # 외부 링크 수
        string = page.split(' ')  # 공백 기준으로 나누기
        for p in string:
            if "href" in p:
                new_link = p[6:]
                # 링크 연결 시켜주기
                for i in range(len(new_link)):
                    if new_link[i] == '\"' and new_link[i + 1] == ">":
                        real_link = new_link[:i] # 이 웹페이지에 걸린 링크
                        link_count += 1
                        if real_link not in idx_link:
                            break
                        idx = idx_link[real_link]  # 연결된 링크의 인덱스 번호
                        if k in linkToLink[idx]:
                            break
                        linkToLink[idx].append(k)

        link_counts.append(link_count)  # 인덱스 별로 링크 카운트

    scores = []
    for i in range(len(pages)):
        link_score = 0
        if len(linkToLink[i]) != 0:
            for idx in linkToLink[i]:  # 이 링크로 이어지는 링크들
                link_score += normal_counts[idx] / link_counts[idx]

        scores.append(link_score + normal_counts[i])

    max_score = max(scores)

    for i in range(len(pages)):
        if scores[i] == max_score:
            answer = i
            break

    print(scores)
    return answer
"""