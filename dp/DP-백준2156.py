import sys
input = sys.stdin.readline

n = int(input())
grape = []
for _ in range(n):
    grape.append(int(input()))

if n == 1:
    print(grape[0])
elif n == 2:
    print(grape[0]+grape[1])
elif n == 3:
    print(max((grape[0] + grape[1]), (grape[0] + grape[2]), (grape[1] + grape[2])))
else:
    dp = [0 for _ in range(n)]
    dp[0] = grape[0]
    dp[1] = grape[0]+grape[1]
    dp[2] = max((grape[0] + grape[1]), (grape[0] + grape[2]), (grape[1] + grape[2]))
    for i in range(3,n):
        dp[i] = max((grape[i] + grape[i-1] + dp[i-3]),(dp[i-2] + grape[i]),(dp[i-1]))
    print(max(dp))
