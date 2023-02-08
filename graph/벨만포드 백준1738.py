import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
edge= []
INF = sys.maxsize
for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().rstrip().split())
    edge.append((u,v,w))

def bellmanFord(start):
    path = [0 for _ in range(n+1)]
    dist = [-INF for _ in range(n+1)]
    dist[start] = 0

    for i in range(n):
       for s,d,c in edge:
        if dist[s] != -INF and dist[d]<dist[s]+c:
            dist[d] = dist[s]+c
            path[d] = s
            if i == n-1:
                dist[d] = INF
    rst = []
    curr = n
    if dist[n] == INF:
        print(-1)
        return
    while curr != 1:
        rst.append(curr)
        curr = path[curr]
    rst.append(curr)
    rst = rst[::-1]
    for i in rst:
        print(i,end=' ')
    return

bellmanFord(1)
