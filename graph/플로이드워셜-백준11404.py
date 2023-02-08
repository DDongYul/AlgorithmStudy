import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
edge = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    edge[i][i] = 0

for _ in range(m):
    a,b,c, = map(int,input().split())
    edge[a][b] = min(edge[a][b],c)

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            edge[j][k] = min(edge[j][i]+edge[i][k],edge[j][k])

for i in range(1,n+1):
    for j in range(1,n+1):
        if edge[i][j] == INF:
            edge[i][j] = 0
        print(edge[i][j],end=' ')
    print()
