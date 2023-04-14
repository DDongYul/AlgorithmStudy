#백준:https://www.acmicpc.net/problem/1890

import sys
input = sys.stdin.readline

N = int(input())
grp = []
for _ in range(N):
    grp.append(list(map(int, input().split())))

def solution(graph):
    n = len(graph)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    d = graph[0][0]
    if 0 <= d < n:
        dp[0][d] = 1
        dp[d][0] = 1
    else:
        return 0

    for i in range(n):
        for j in range(n):
            d = graph[i][j]
            if d == 0 or dp[i][j] == 0:
                continue
            dx = j + d
            dy = i + d
            if 0 <= dx < n:
                dp[i][dx] = dp[i][dx] + dp[i][j]
            if 0 <= dy < n:
                dp[dy][j] = dp[dy][j] + dp[i][j]
    return dp[n - 1][n - 1]

print(solution(grp))