# 택시비 절약 위해 같이 타고 가다, 특정 지점에서 헤어짐 -> 이 때 비용의 최소값
# 시작 지점 에서 어느 지점(공통 지점)까지 거리 다익스트라 한번, 그 지점에서 각 지점까지 다익스트라 각각, 현재,a,b합 최소
from heapq import heappop, heappush

INF = int(1e12)

def dijkstra(start, graph):
    dist = [INF for _ in range(len(graph))]
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        w, d = heappop(heap)
        if w > dist[d]:
            continue
        for ww, dd in graph[d]:
            if dist[dd] > w + ww:
                heappush(heap, (w + ww, dd))
                dist[dd] = w + ww
    return dist


def solution(n, s, a, b, fares):
    answer = INF
    graph = [[] for _ in range(n + 1)]
    for fare in fares:
        graph[fare[0]].append((fare[2], fare[1]))
        graph[fare[1]].append((fare[2], fare[0]))

    together = dijkstra(s, graph)
    for i in range(1, n + 1):
        if i == INF:
            continue
        aa = dijkstra(i, graph)[a]
        bb = dijkstra(i, graph)[b]
        answer = min(answer, (together[i] + aa + bb))
    return answer

