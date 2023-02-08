import sys
input = sys.stdin.readline
INF = int(1e9)

N,M = map(int,input().split())
edges = []

for _ in range(M):
    A,B,C = map(int,input().split())
    edges.append((A,B,C))

def bf(start):
    dist = [0] + [INF] * N
    dist[start] = 0
    for i in range(N):
        for s, d, w in edges:
            if dist[s] != INF and dist[d] > dist[s] + w:
                if i == N - 1:
                    return False
                dist[d] = dist[s] + w
    return dist

if not bf(1):
    print(-1)
else:
    dist = bf(1)
    for i in range(2,N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
