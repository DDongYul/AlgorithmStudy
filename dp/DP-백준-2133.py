#어떤 경우에도 특별한 모양들은 "딱 2가지씩만" 존재한다!

N = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
dp[4] = 11

for i in range(6,N+1,2):
    idx = i-4
    dp[i] += dp[2] * dp[i - 2]
    dp[i] += 6 # dp[i-2] * dp[2]에서 겹치지 않는 고유문양
    while idx > 2:
        dp[i] += dp[idx] * 2
        idx-=2
    dp[i] += 2 #dp[i]의 고유문양

print(dp[N])