import sys
input = sys.stdin.readline
INF = 1e10

N = int(input())
dist = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0
        else:
            dist[i][j] = INF

while True:
    a,b = map(int,input().split())
    if a==-1 and b ==-1:
        break
    dist[a-1][b-1] = 1
    dist[b-1][a-1] = 1

for i in range(0,N):
    for j in range(0,N):
        for k in range(0,N):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

score = []
for i in dist:
    score.append(max(i))
sc = min(score)
cnt = 0
ans = []
for i in range(len(score)):
    if score[i] == sc:
        cnt+=1
        ans.append(str(i+1))
print(sc,cnt)
print(" ".join(ans))

