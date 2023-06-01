import sys
input = sys.stdin.readline
INF = int(1e10)
c,n = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))
DP = [INF for _ in range(1101)] #dp[n] = n명의 비용 최소값

for i in lst:
    DP[i[1]] = min(DP[i[1]],i[0])

for i in range(1101):
    for j in lst:
        if (i-j[1])>0:
            DP[i] = min((DP[i-j[1]] + j[0]),DP[i])

print(min(DP[c:]))
