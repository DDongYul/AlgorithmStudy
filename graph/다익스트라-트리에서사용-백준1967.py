#dijkstra 2번 -> 임의의 점에서 가장 먼 점을 찾음, 그 점에서 가장 먼 점이 지름
#임의의 점에서 거리가 같은 두 점이 있을 때, 세 점으로 원을 만들 수 있고 원의 지름보다 거리가 긴 점은 나올 수 없음 -> 나오면 가장 먼 점이 바뀜
#따라서 거리가 같은 점이 여러개 있어도 상관없다!
import sys
input = sys.stdin.readline
from heapq import heappop,heappush
INF = sys.maxsize

def dijkstra(start):
    dist = [0]+[INF]*n
    dist[start] = 0
    heap = []
    heappush(heap,(start,0))
    while heap:
        s,w = heappop(heap)
        if w>dist[s]:
            continue
        else:
            for d,ww in edge[s]:
                if dist[d]> w+ww:
                    dist[d] = w+ww
                    heappush(heap,(d,w+ww))
    return dist

n = int(input())
if n==1:
    print(0)
    exit(0)
edge = [[]for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    edge[a].append((b,c))
    edge[b].append((a,c))

dist1 = dijkstra(1)
idx = dist1.index(max(dist1))
print(max(dijkstra(idx)))