import sys
input = sys.stdin.readline
from itertools import combinations
INF = 1e9

N,M = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
chicken = []

house = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append((i,j))
        elif graph[i][j] == 1:
            house.append((i,j))
comb = list(combinations(chicken,M))

result = INF
for c in comb:
    temp = [INF for _ in range(len(house))]
    for dx,dy in c:
        for index,h in enumerate(house):
            temp[index] = min(temp[index],(abs(dx-h[0])+abs(dy-h[1])))
    result = min(result,sum(temp))

print(result)