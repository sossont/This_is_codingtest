N = int(input())

dp = [0] * 1001 # dp[x]는 가로가 x일 때 바닥을 채우는 모든 경우의 수
# dp[x] = dp[x-1] + dp[x-2] * 2
dp[1] = 1
dp[2] = 3

for i in range(3,N+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796

print(dp[N])