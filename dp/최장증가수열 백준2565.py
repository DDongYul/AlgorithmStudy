#교차하지 않으려면 나보다 번호가 큰 전기줄이 내가 연결된 번호보다 큰 번호여야한다 -> 최장증가수열
import sys
input = sys.stdin.readline

N = int(input())
graph = []

for _ in range(N):
    a,b = map(int,input().split())
    graph.append((a,b))

graph.sort()
dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(0, i):
        if graph[j][1] < graph[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N-max(dp))
