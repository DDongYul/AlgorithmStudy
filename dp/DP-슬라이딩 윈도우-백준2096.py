import sys
input = sys.stdin.readline
N = int(input())

min_dp = [0,0,0]
max_dp = [0,0,0]

for i in range(N):
    x,y,z = map(int,input().split())
    mx0 = max(max_dp[0],max_dp[1])+x
    mx1 = max(max_dp) + y
    mx2 = max(max_dp[1],max_dp[2])+z
    max_dp[0] = mx0
    max_dp[1] = mx1
    max_dp[2] = mx2


    mn0 = min(min_dp[0], min_dp[1]) + x
    mn1 = min(min_dp) + y
    mn2 = min(min_dp[1], min_dp[2]) + z
    min_dp[0] = mn0
    min_dp[1] = mn1
    min_dp[2] = mn2

print(max(max_dp),min(min_dp))

