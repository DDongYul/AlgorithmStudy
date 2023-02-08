import sys
from heapq import heappush,heappop
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    dist = [INF for _ in range(V+1)]
    dist[start] = 0
    heap = []
    heappush(heap,[0,start])
    while heap:
        w,d = heappop(heap)
        if w>dist[d]:
            continue
        for ww,dd in edges[d]:
            if dist[dd] > w + ww:
                dist[dd] = w+ww
                heappush(heap,[w+ww,dd])
    for i in dist[1::]:
        if i == INF:
            print("INF")
        else:
            print(i)


V,E = map(int,input().split())
edges = [[] for _ in range(V+1)]
start_point = int(input())
for _ in range(E):
    u1,v1,w1 = map(int,input().split())
    edges[u1].append([w1,v1])

dijkstra(start_point)