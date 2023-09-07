N = int(input())

INF = 1000000000
dp = [[0 for _ in range(10)] for _ in range(100)]
for i in range(1,10):
    dp[0][i] = 1
for i in range(1,100):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] % INF
        elif j == 9:
            dp[i][j] = dp[i-1][8] % INF
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % INF

print(sum(dp[N-1])%INF)