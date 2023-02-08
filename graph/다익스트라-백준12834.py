import sys
from heapq import heappush,heappop
input = sys.stdin.readline
INF = 1e9

def dijkstra(s):
    cost = [INF for _ in range(V)]
    cost[s] = 0
    heap = []
    heappush(heap,[0,s])
    while heap:
        w,n = heappop(heap)
        if w>cost[n]:
            continue
        for ww,nn in graph[n]:
            new_cost = w + ww
            if new_cost < cost[nn]:
                cost[nn] = new_cost
                heappush(heap, [new_cost, nn])
    return cost


N,V,E = map(int,input().split())
graph = [[] for _ in range(V)for _ in range(V)]
A,B = map(int,input().split())
Node = list(map(int,input().split()))
for _ in range(E):
    x,y,l = map(int,input().split())
    graph[x-1].append((l,y-1))
    graph[y-1].append((l,x-1))

A_list = dijkstra(A-1)
B_list = dijkstra(B-1)
cnt = 0
for i in Node:
    if A_list[i-1] == INF:
        cnt+=-1
    else:
        cnt+= A_list[i-1]
        if B_list[i - 1] == INF:
            cnt += -1
        else:
            cnt+= B_list[i-1]
print(cnt)














#     graph[x-1][y-1] = l
#     graph[y-1][x-1] = l
#
# for i in range(V):
#     graph[i][i] = 0
#
#
# for i in range(V):
#     for j in range(V):
#         for k in range(V):
#             graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])
#
#
# cnt = 0
# for i in Node:
#     if graph[i-1][A-1] == 105:
#         cnt+=-1
#     else:
#         cnt += graph[i-1][A-1]
#         if graph[i-1][B-1] == 105:
#             cnt += -1
#         else:
#             cnt += graph[i-1][B-1]
# print(cnt)