import sys
input = sys.stdin.readline
from heapq import heappush,heappop
INF = int(1e10)

def dijkstra(start,end):
    dist = [INF for _ in range(n+1)]
    dist[start] = 0
    heap = [(0,start)]
    path = [0 for _ in range(n+1)]  #가장 가까운 노드
    while heap:
        w,d = heappop(heap)
        if w>dist[d]:
            continue
        for ww,dd in edge[d]:
            if dist[dd]>w+ww:
                heappush(heap,(w+ww,dd))
                dist[dd] = w+ww
                path[dd]=d
    print(dist[end])
    rst = [end]
    while end != start: #end부터 start까지 역추적
        end = path[end]
        rst.append(end)
    print(len(rst))
    for i in (rst[::-1]):
        print(i,end=" ")

n = int(input())
m = int(input())
edge = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    edge[a].append((c,b))

start1,end1 = map(int,input().split())

dijkstra(start1,end1)