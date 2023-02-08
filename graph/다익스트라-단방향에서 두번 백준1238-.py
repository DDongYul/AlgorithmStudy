import sys
from heapq import heappop,heappush
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start,edge):
    dist = [0] + [INF for _ in range(N)]
    dist[start] = 0
    heap = []
    heappush(heap,(0,start))
    while heap:
        w,s = heappop(heap)
        if w>dist[s]:
            continue
        else:
            for ss,ww in edge[s]:
                if dist[ss]>w+ww:
                    heappush(heap,(w+ww,ss))
                    dist[ss] = w+ww
    return dist

N,M,X = map(int,input().split())
edge1 = [[] for _ in range(N+1)]
edge2 = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    edge1[a].append((b,c))      #X에서 각 정점까지의 거리
    edge2[b].append((a,c))      #각 정점에서 X까지의 거리는 간선을 뒤집으면 X에서 각 정점까지의 거리와 같음

di1 = dijkstra(X,edge1)
di2 = dijkstra(X,edge2)
for i in range(0,N+1):
    di1[i]+=di2[i]
print(max(di1))