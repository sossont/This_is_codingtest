N,M = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

money.sort()    # 내림차순으로 입력받는다는 보장이 없으므로 정렬 한번 해준다.
dp = [10001] * 10001

for bill in money:
    dp[bill] = 1    # 1가지 씩만 쓰는경우를 초기화 해준다.

for i in range(M+1):
    for bill in money:
        if i > bill:    # 화폐 단위보다 작으면 안되기 때문.
            dp[i] = min(dp[i-bill] + 1, dp[i])
        else:
            break

if dp[M] != 10001:
    print(dp[M])
else:
    print("-1")