import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
dp = [[1,1] for _ in range(n)]  # 0: 증가하는중 1: 감소하는중
for i in range(n):
    for j in range(i):
        if lst[i]>lst[j]:
            dp[i][0] = max(dp[i][0],dp[j][0]+1) #증가만 보면 됨
        elif lst[i]<lst[j]:
            dp[i][1] = max(dp[j][0]+1,dp[i][1],dp[j][1]+1)  #앞에서 증가하다 이번에 감소, 현재, 계속 감소하는중
        elif lst[i] == lst[j]:
            dp[i][0] = max(dp[i][0],dp[j][0])
            dp[i][1] =max(dp[i][1],dp[j][1])

result = 0
for i in dp:
    for j in i:
        result = max(result,j)
print(result)