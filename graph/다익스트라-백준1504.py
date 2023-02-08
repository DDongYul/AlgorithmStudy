#다익스트라를 3번 1-> v1 -> v2 -> N / 1 -> v2 -> v1 -> N
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    heap = []
    heappush(heap,(0,start))
    while heap:
        w,d = heappop(heap)
        if w>dist[d]:
            continue
        for ww,dd in edges[d]:
            if dist[dd] > w+ww:
                dist[dd] = w + ww
                heappush(heap,[w+ww,dd])
    return dist

N,E = map(int,input().split())
edges = [[] for _ in range(N+1) for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    edges[a].append((c,b))  
    edges[b].append((c,a))
v1,v2 = map(int,input().split())

l1 = dijkstra(1)
lv1 = dijkstra(v1)
lv2 = dijkstra(v2)

if l1[v1] == INF or l1[v2] == INF or l1[N] == INF:
    print(-1)
else:
    print(min((l1[v1]+lv1[v2]+lv2[N]),(l1[v2]+lv2[v1]+lv1[N])))