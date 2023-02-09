import sys
input = sys.stdin.readline
from itertools import combinations
INF = 1e9

def dist(x,y):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                rst[i][j] = min(rst[i][j],abs(x-i)+abs(y-j))

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

chicken = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append((i,j))
            graph[i][j] = 0

comb = list(combinations(chicken,M))

result = INF
for c in comb:
    rst = [[INF for _ in range(N)] for _ in range(N)]
    for dx,dy in c:
         dist(dx,dy)
    temp = 0
    for i in range(N):
        for j in range(N):
            if rst[i][j] != INF:
                temp+=rst[i][j]
    result = min(result,temp)

print(result)