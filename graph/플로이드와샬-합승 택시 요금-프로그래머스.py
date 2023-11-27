# 플로이드 와샬
# 각 지점에서 B,A의 집까지의 거리 + 지점과 S 거리가 최소인것
# def solution(n, s, a, b, fares):
#     INF = 100001*n
#     dist = [[INF for _ in range(n)] for _ in range(n)]
#
#     for c, d, f in fares:
#         dist[c - 1][d - 1] = f
#         dist[d - 1][c - 1] = f
#
#     for i in range(0, n):
#         for j in range(0, n):
#             for k in range(0, n):
#                 dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
#
#     for i in range(n):
#         dist[i][i] = 0
#
#     answer = INF
#     for i in range(n):
#         da = dist[i][a - 1]
#         db = dist[i][b - 1]
#         ds = dist[i][s - 1]
#         answer = min(answer, da + db + ds)
#     return answer

#다익스트라
from heapq import heappush, heappop

INF = 100001 * 200
def solution(n, s, a, b, fares):
    dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
    edges = [[] for _ in range(n+1)]

    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f
        edges[c].append(d)
        edges[d].append(c)

    for i in range(n+1):
        dist[i][i] = 0

    ds = dijkstra(dist[s],edges,s)
    da = dijkstra(dist[a],edges,a)
    db = dijkstra(dist[b],edges,b)

    for i in dist[s]:
        print(i)
    answer = INF
    for i in range(n):
        answer = min(answer, da[i] + db[i] + ds[i])

    return answer


def dijkstra(dist,edges,start):
    heap = [(0, start)]
    while heap:
        w, d = heappop(heap)
        if w > dist[d]:
            continue
        for ww, dd in edges[d]:
            if dist[dd] > w + ww:
                dist[dd] = w + ww
                heappush(heap, [w + ww, dd])
    return dist



