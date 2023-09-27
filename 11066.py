#마지막은 항상 두 개의 합 -> 그룹을 두 개로 나눠서 합쳣을 때 합
#10개면 1/9 2/8 3/7 4/6 5/5 6/4 7/3 8/2 9/1
# 9 8 7 6 5 4 3 2 1 8 7 6 5 4 3 2 1 7 6 5 4 3 2 1 -> 결과 값을 배열에 저장해둔다면 재귀 줄일 수 있을듯
# 1/9 -> 1/1/8 이랑 2/8에서 8은 동일하다.

# dp[0][3] = min((dp[0][1] + dp[1][3]), (dp[0][2] + dp[2][3]))
import sys
input = sys.stdin.readline
INF = sys.maxsize

def sol(s,e):
    if dp[s][e] != INF:
        return dp[s][e]
    curr = INF
    if e == s:
        return file[e]
    if e-s == 1:
        dp[s][e] = file[s]+file[e]
        return file[s]+file[e]
    if e-s == 2:
        dp[s][e] = min(((file[s]+file[s+1])*2+file[e]), (file[s] + (file[s+1]+file[e])*2))
        return dp[s][e]
    for i in range(0,e-s):
        print((s,s+i) , (s+i+1,e) , (dp[0][3]))
        curr =  min(curr,(sol(s,s+i)+sol(s+i+1,e))*2)
    dp[s][e] = curr
    return curr


T = int(input())
for _ in range(T):
    K = int(input())
    file = list(map(int,input().split()))
    dp = [[INF for _ in range(K)] for _ in range(K)]
    for i in range(K):
        dp[i][i] = file[i]
    print(sol(0,K-1))
    print(dp)
