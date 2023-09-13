import sys
input = sys.stdin.readline

N= int(input())
sch = [(0,0)]
for i in range(N):
    sch.append((map(int,input().split())))
DP = [0 for _ in range(N+1)]

for i in range(N+1):
    t,p = sch[i]
    if i+t-1<=N:
        DP[i+t-1] = max(DP[i+t-1],DP[i-1]+p)
    DP[i] = max(DP[i],DP[i-1])

print(DP[N])
