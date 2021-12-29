N = int(input())
warehouse = list(map(int,input().split()))

#최소한 한칸 이상 떨어져있어야한다? 그렇다면 X(n) = max ( X(n-1), X(n-2) + n )

warehouse.insert(0,0)   # 인덱스 1부터 사용하려고~

dp = [0] * 101
dp[1] = warehouse[1]


for i in range(2,N+1):
    dp[i] = max(dp[i-1], dp[i-2] + warehouse[i])

print(dp[N])