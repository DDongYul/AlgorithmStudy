#첫 풀이:플로이드 와샬 -> 벨만포드로 수정

import sys
input = sys.stdin.readline
INF = int(1e9)

def bellmanFord(start):
    dist = [INF]*(N+1)
    dist[start] = 0
    for i in range(N):
        for s, d, w in edges:
           if dist[d] > dist[s]+w:
                dist[d] = dist[s] + w
                if i == N-1:
                    return True
    return False

TC = int(input())
for _ in range(TC):
    N,M,W = map(int,input().split())
    edges = []

    for _ in range(M):
        S,E,T = map(int,input().split())
        edges.append((S,E,T))
        edges.append((E,S,T))

    for _ in range(W):
        S,E,T = map(int, input().split())
        edges.append((S,E,-T))

    flag = bellmanFord(1)
    if flag:
        print("YES")
    else:
        print("NO")

#########플로이드 와샬###########3
    # N,M,W = map(int,input().split())
    # graph = [[INF for _ in range(N)]for _ in range(N)]
    # for _ in range(M):
    #     S,E,T = map(int,input().split())
    #     graph[S-1][E-1] = min(graph[S-1][E-1],T)
    #     graph[E-1][S-1] = min(graph[E-1][S-1],T)
    # for _ in range(W):
    #     S, E, T = map(int, input().split())
    #     graph[S-1][E-1] = min(graph[S-1][E-1],-T)
    #
    # flag = False
    # for i in range(N):
    #     if flag: break
    #     for j in range(N):
    #         if flag: break
    #         for k in range(N):
    #             graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])
    #             if j == k and graph[j][k]<0:
    #                 flag = True
    #                 break
    #
    # if flag:
    #     print("YES")
    # else:
    #     print("NO")